import getpass
from os import system, name 

import tolls

T = tolls

system('clear')
print('<Login info>')
username = input('UserName:\033[96m ')
print('\033[0m\033[F')
password = getpass.getpass()
api, user_id = T.Login(username, password)
api.getUsernameInfo(user_id)
temp = api.LastJson['user']
FollowersC = temp['follower_count']
FollowingC = temp['following_count']

while True:
    system('clear')
    # print('<- UserName: \033[96m{}\033[0m ->\n'.format(username))
    print(f'<- UserName: \033[96m{username}\033[0m  ⇣\033[91m{FollowersC}\033[0m  ⇡\033[93m{FollowingC}\033[0m ->\n')
    print('1> List of followers')
    print('2> List of following')
    print('3> List of unfollowing')
    print('4> List of follow back')
    print('5> unfollowing')
    print('6> following')
    print('7> Check Users')
    print('\n0> Exit')
    print('---------------------------')

    i = input('> ')

    system('clear')

    if (i == '1'):
        print('<- List of followers ->')
        Followers = T.updatFollowers(api, user_id)
        print('\033[91m' + str(len(Followers)) + "\033[0m people following u.")
        answer = input("do you want see that? [y/n] ")
        if (answer == 'y'):
            for foll in Followers:
                print(foll['username'])
    elif (i == '2'):
        print('<- List of following ->')
        Following = T.updatFollowings(api, user_id)
        if Following == -1:
            input('continue')
            continue
        print('\033[91m' + str(len(Following)) + "\033[0m people u following.")
        answer = input("do you want see that? [y/n] ")
        if (answer == 'y'):
            for foll in Following:
                print(foll['username'])
    elif (i == '3'):
        print('<- List of unfollowing ->')
        T.Unfollowings(api, user_id)
    elif (i == '4'):
        print('<- List of follow back ->')
    elif (i == '5'):
        print('<- Unfollowing ->')
        T.Unfollow(api, user_id)
    elif (i == '6'):
        print('<- Following ->')
        T.TFollows(api, user_id)
    elif (i == '7'):
        print('<- Check Users ->')
        T.CheckUsers(api, user_id)
    elif (i == '0'):
        system('clear')
        break
    
    input('continue')
