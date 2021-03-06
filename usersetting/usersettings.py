import eel
import time
import os
from datetime import date
import datetime
import eel
import sys
import platform
import json
#with open('data.json', 'w', encoding='utf-8') as f:
    #json.dump(data, f, ensure_ascii=False, indent=4)
eel.init("usersetting/settingweb")

@eel.expose
def usersettingwrite(username, usercity, user_gender, userdob, useremail, useremailpass):
    try:
        with open('data.json', 'w', encoding='utf-8') as f:
        #json.dump(data, f, ensure_ascii=False, indent=4)
            print("Name: " + username)
            print("Usercity: " + usercity)
            print("usergender: " + user_gender)
            print("userdob: " + userdob)
            print("useremail: " + useremail)
            print("useremailpass: " + useremailpass)
            data = {
                "main_user_data": {
                    "username": username,
                    "usercity": usercity,
                    "usergender":user_gender,
                    "userdob": userdob,
                    "useremail":useremail,
                    "useremailpass":useremailpass,
                    "userspecies": "homo sapien",
                    "userbloodtype": "Null",
                    "userskincolor":"null",
                    "userethnicity":"null",
                    "userreligion":"null",
                    "userweight":"null",
                    "userheight":"null",
                    "usersport":"null",
                    "userhobby":"null",
                    "userinterest":"null",
                    "userpersonaldiscordbottoken":"null"
                }
            }
            json.dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)
    except Exception as e:
        print(e)
if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:

    eel.start("homesetting.html",cmdline_args=['--start-fullscreen'], port=1111, mode='default')
else:
    raise EnvironmentError('Error: System is not Windows 10 or above')
