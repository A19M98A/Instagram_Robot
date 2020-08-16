import sqlite3
import datetime

def CreateTable():
    conn = sqlite3.connect('test.db')
    conn.execute("CREATE  TABLE  IF NOT EXISTS Follower (" +
                " id TEXT," +
                " username TEXT," +
                " name TEXT," +
                " datetime TEXT" +
                ")");
    
    conn.execute("CREATE  TABLE  IF NOT EXISTS Following (" +
                " id TEXT," +
                " username TEXT," +
                " name TEXT," +
                " datetime TEXT" +
                ")");
    
    conn.execute("CREATE  TABLE  IF NOT EXISTS UserData (" +
                " pk TEXT," +
                " full_name TEXT," +
                " is_private TEXT," +
                " is_verified TEXT," +
                " media_count TEXT," +
                " follower_count TEXT," +
                " following_count TEXT," +
                " following_tag_count TEXT," +
                " biography TEXT," +
                " external_url TEXT," +
                " total_igtv_videos TEXT," +
                " total_clips_count TEXT," +
                " total_ar_effects TEXT," +
                " usertags_count TEXT," +
                " is_favorite TEXT," +
                " is_interest_account TEXT," +
                " has_chaining TEXT," +
                " mutual_followers_count TEXT," +
                " has_highlight_reels TEXT," +
                " can_be_reported_as_fraud TEXT," +
                " is_business TEXT," +
                " account_type TEXT," +
                " professional_conversion_suggested_account_type TEXT," +
                " is_call_to_action_enabled TEXT," +
                " include_direct_blacklist_status TEXT," +
                " is_potential_business TEXT," +
                " show_post_insights_entry_point TEXT," +
                " is_bestie TEXT," +
                " has_unseen_besties_media TEXT," +
                " show_account_transparency_details TEXT," +
                " show_leave_feedback TEXT," +
                " robi_feedback_source TEXT," +
                " auto_expand_chaining TEXT," +
                " highlight_reshare_disabled TEXT," +
                " is_memorialized TEXT" +
                ")");

    conn.close()

def INSERTData(_data):
    _data['biography'] = _data['biography'].replace("'", "{{{{{}}}}}")
    conn = sqlite3.connect('test.db')
    f = True
    for row in conn.execute("SELECT * FROM UserData WHERE pk = ?", (_data['pk'],)):
        f = False
    if f:
        conn.execute("INSERT INTO UserData"+
                        "(pk,full_name,is_private,is_verified,media_count,follower_count,following_count,following_tag_count,biography,external_url,total_igtv_videos,total_clips_count,total_ar_effects,usertags_count,is_favorite,is_interest_account,has_chaining,mutual_followers_count,has_highlight_reels,can_be_reported_as_fraud,is_business,account_type,professional_conversion_suggested_account_type,is_call_to_action_enabled,include_direct_blacklist_status,is_potential_business,show_post_insights_entry_point,is_bestie,has_unseen_besties_media,show_account_transparency_details,show_leave_feedback,robi_feedback_source,auto_expand_chaining,highlight_reshare_disabled,is_memorialized) " +
                        "VALUES('" + str(_data['pk']) + "'," +
                        "'" + str(_data['full_name']) + "'," +
                        "'" + str(_data['is_private']) + "'," +
                        "'" + str(_data['is_verified']) + "'," +
                        "'" + str(_data['media_count']) + "'," +
                        "'" + str(_data['follower_count']) + "'," +
                        "'" + str(_data['following_count']) + "'," +
                        "'" + str(_data['following_tag_count']) + "'," +
                        "'" + str(_data['biography']) + "'," +
                        "'" + str(_data['external_url']) + "'," +
                        "'" + str(_data['total_igtv_videos']) + "'," +
                        "'" + str(_data['total_clips_count']) + "'," +
                        "'" + str(_data['total_ar_effects']) + "'," +
                        "'" + str(_data['usertags_count']) + "'," +
                        "'" + str(_data['is_favorite']) + "'," +
                        "'" + str(_data['is_interest_account']) + "'," +
                        "'" + str(_data['has_chaining']) + "'," +
                        "'" + str(_data['mutual_followers_count']) + "'," +
                        "'" + str(_data['has_highlight_reels']) + "'," +
                        "'" + str(_data['can_be_reported_as_fraud']) + "'," +
                        "'" + str(_data['is_business']) + "'," +
                        "'" + str(_data['account_type']) + "'," +
                        "'" + str(_data['professional_conversion_suggested_account_type']) + "'," +
                        "'" + str(_data['is_call_to_action_enabled']) + "'," +
                        "'" + str(_data['include_direct_blacklist_status']) + "'," +
                        "'" + str(_data['is_potential_business']) + "'," +
                        "'" + str(_data['show_post_insights_entry_point']) + "'," +
                        "'" + str(_data['is_bestie']) + "'," +
                        "'" + str(_data['has_unseen_besties_media']) + "'," +
                        "'" + str(_data['show_account_transparency_details']) + "'," +
                        "'" + str(_data['show_leave_feedback']) + "'," +
                        "'" + str(_data['robi_feedback_source']) + "'," +
                        "'" + str(_data['auto_expand_chaining']) + "'," +
                        "'" + str(_data['highlight_reshare_disabled']) + "'," +
                        "'" + str(_data['is_memorialized']) +
                        "')")
        print('Record created successfully <INSERTData> pk: ' + str(_data['pk']))
        conn.commit()
    conn.close()

def INSERTFollowers(userId,userName,Name):
    Name = Name.replace("'", "{{{{{}}}}}")
    conn = sqlite3.connect('test.db')
    f = True
    for row in conn.execute("SELECT * FROM Follower WHERE id = ?", (userId,)):
        f = False
    if f:
        conn.execute("INSERT INTO Follower"+
                        "(id,username,name,datetime) " +
                        "VALUES('" + userId + "'," +
                        "'" + userName + "'," +
                        "'" + Name + "'," +
                        "'" + str(datetime.datetime.now()) +
                        "')")
        print('Record created successfully <INSERTFollowers>')
        conn.commit()
    conn.close()

def INSERTFollowing(userId,userName,Name):
    Name = Name.replace("'", "{{{{{}}}}}")
    conn = sqlite3.connect('test.db')
    f = True
    for row in conn.execute("SELECT * FROM Following WHERE id = ?", (userId,)):
        f = False
    if f:
        conn.execute("INSERT INTO Following"+
                        "(id,username,name,datetime) " +
                        "VALUES('" + userId + "'," +
                        "'" + userName + "'," +
                        "'" + Name + "'," +
                        "'" + str(datetime.datetime.now()) +
                        "')")
        print('Record created successfully <INSERTFollowing>')
        conn.commit()
    conn.close()

def ReadFollowers():
    # print('<- Followers ->')
    ls = []
    conn = sqlite3.connect('test.db')
    for row in conn.execute("SELECT * FROM Follower"):
        ls.append(row)
    return ls

def ReadFollowings():
    # print('<- Followings ->')
    ls = []
    conn = sqlite3.connect('test.db')
    for row in conn.execute("SELECT * FROM Following"):
        ls.append(row)
    return ls

def Check(userId):
    ls = []
    conn = sqlite3.connect('test.db')
    for row in conn.execute("SELECT * FROM Follower where id='" + str(userId) + "'"):
        ls.append(row)
    return ls

def CheckF(userId):
    ls = []
    conn = sqlite3.connect('test.db')
    for row in conn.execute("SELECT * FROM Following where id='" + str(userId) + "'"):
        ls.append(row)
    if len(ls) > 0:
        return False
    return True