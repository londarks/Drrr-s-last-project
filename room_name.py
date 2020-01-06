import json
import requests
import os, re

def Check_name():
    session = requests.session()
    f = open('athus.cookie', 'r')
    session.cookies.update(eval(f.read()))
    f.close()
    rooms = session.get("https://drrr.com/json.php?update=")
    if rooms.status_code == 200:
        rooms_data = json.loads(rooms.content)
        name = rooms_data['name']
    return name