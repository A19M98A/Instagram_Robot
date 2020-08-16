from InstagramAPI import InstagramAPI
import random
import threading
import time
import Database

database = Database

def Login(username, password):
    api = InstagramAPI(username, password)
    api.login()
    user_id = api.username_id
    return api, user_id

def Unfollow(api):
    ls = database.ReadFollowers()
    for l in ls:
        if l[1] == 'aminallahjanipoor':
            continue
        api.unfollow(l[0])
        print(l[1])

def PrintFollowers(api):
    print('<- Followers ->')
    ls = database.ReadFollowers()
    print(str(len(ls)) + " people following u.")
    answer = input("do you want see that? [y/n] ")
    if (answer == 'y'):
        for l in ls:
            print(str(l).replace("{{{{{}}}}}", "'"))

def PrintFollowings(api):
    print('<- Followings ->')
    ls = database.ReadFollowings()
    for l in ls:
        print(str(l).replace("{{{{{}}}}}", "'"))

def updatFollowers(api, user_id):
    followers = api.getTotalFollowers(user_id)
    for foll in followers:
        # print(foll['username'])
        database.INSERTFollowers(str(foll['pk']), str(foll['username']), str(foll['full_name']))
        # print('<---------------->')
    return followers

def updatFollowings(api, user_id):
    try:
        print('\033[91m\033[F')
        following = api.getTotalFollowings(user_id)
    except:
        print('\033[0m\033[F')
        return -1

    print('\033[0m\033[F')

    for foll in following:
        # print(foll['username'])
        # print(foll['username'])
        database.INSERTFollowing(str(foll['pk']), str(foll['username']), str(foll['full_name']))
        # print('<---------------->')
        # if foll['username'] == 'aminallahjanipoor':
        #     continue
        # api.unfollow(foll['pk'])
    return following

def Unfollow(api, user_id):
    following = api.getTotalFollowings(user_id)

    for foll in following:
        if foll['username'] == 'aminallahjanipoor':
            continue
        print(foll['username'])
        api.unfollow(foll['pk'])

def Unfollowings(api, user_id):
    fol = database.ReadFollowers()
    followers = api.getTotalFollowers(user_id)
    data = []
    for f in fol:
        # print(f[1])
        data.append(f[1])
    # print("<------------>")
    for d in followers:
        # print("<------------>")
        # print(d['username'])
        if (data.count(d['username']) > 0):
            data.remove(d['username'])
    print(str(len(data)) + " people unfollow u.")
    answer = input("do you want see that? [y/n] ")
    if (answer == 'y'):
        for un in data:
            print(un)
            
def Follow(api, user):
    L = database.Check(user['ak'])
    if api.follow(user['ak']) and len(L) < 1:
        s = ''
        if user['is_private'] != 'False':
            s = '\033[31m' + user['is_private']
        else:
            s = '\033[33m' + user['is_private']
        print(f"\033[96m {user['username']:{20}} {s}\033[0m")
    
    
def RFollows(api, user_id, stop):
    MyFollowers = api.getTotalFollowers(user_id)
    random.shuffle(MyFollowers)
    Ch = False
    for f in MyFollowers:
        if stop(): 
            break
        if Ch:
            for i in range(210):
                if stop(): 
                    break
                time.sleep(1)
            Ch = False
        s = ''
        if str(f['is_private']) == 'False':
           print('\033[33m' + f['username'] + '\033[0m')
        if str(f['is_private']) == 'False':
            L2 = []
            followers = []
            next_max_id = ''
            while len(followers) < 200:
                if stop(): 
                    break
                print('\033[91m\033[F')
                api.getUserFollowings(f['pk'], next_max_id)
                temp = api.LastJson

                if temp['status'] == 'fail':
                    print('\033[0m\033[F')
                    Ch = True
                    break
                print('\033[0m\033[F')
                
                for item in temp["users"]:
                    if database.CheckF(item['pk']):
                        followers.append(item)

                if temp["big_list"] is False:
                    break
                next_max_id = temp["next_max_id"]
            if stop(): 
                    break
            for foll in followers:
                # print(foll['username'])
                if stop(): 
                    break
                if len(L2) > 100:
                    break
                L2.append({
                'ak': str(foll['pk']),
                'username': str(foll['username']),
                'full_name': str(foll['full_name']),
                'is_private': str(foll['is_private'])
                })
            if stop(): 
                    break
            random.shuffle(L2)
            for j in range(10):
                if stop(): 
                    break
                if j < len(L2):
                    Follow(api, L2.pop())

def TFollows(api, user_id):
    stop_threads = False
    t1 = threading.Thread(target=RFollows, args=(api, user_id,lambda : stop_threads, ))
    t1.start()
    input()
    stop_threads = True
    t1.join()

def CheckUsers(api, user_id):
    followers = api.getTotalFollowers(user_id)
    for foll in followers:
        api.getUsernameInfo(foll['pk'])
        database.INSERTData(api.LastJson['user'])

database.CreateTable()
# updatFollowers()
# updatFollowings()
# PrintFollowers()
# PrintFollowings()
# Unfollow()
