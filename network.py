import requests
import time
import json
import os , re
import threading

global ts_last_greeting
ts_last_greeting = 0

class Commands(object):
    def __init__(self):
        self.session = requests.session()


    def load_cookie(self, file_name):
        f = open(file_name, 'r')
        self.session.cookies.update(eval(f.read()))
        f.close()

    def leave_room(self):
        leave_body = {
            'leave': 'leave'
        }
        lr = self.session.post('https://drrr.com/room/?ajax=1', leave_body)
        lr.close()

    def kick_room(self):
        kick_body = {
            'kick': 'kick'
        }
        kc = self.session.post('https://drrr.com/room/?ajax=1', kick_body)
        kc.close()

    def new_host(self, new_host_id):
        new_host_body = {
            'new_host': new_host_id
        }
        nh = self.session.post('https://drrr.com/room/?ajax=1', new_host_body)
        nh.close()

    def post(self, message, url='', to=''):
        post_body = {
            'message': message,
            'url': url,
            'to': to
        }
        p = self.session.post(url='https://drrr.com/room/?ajax=1', data=post_body)
        p.close()

    def share_music(self, url, name=''):
        share_music_body = {
            'music': 'music',
            'name': name,
            'url': url
        }
        p = self.session.post(url='https://drrr.com/room/?ajax=1', data=share_music_body)
        p.close()
        
    def room_enter(self, url_room):
        re = self.session.get(url_room,headers={'User-Agent': 'Bot'})
        re.close()
        room = self.session.get('https://drrr.com/json.php?fast=1')
        return room.text


    def room_update(self, room_text):
        update = re.search('"update":\d+.\d+', room_text).group(0)[9:]
        url_room_update = 'https://drrr.com/json.php?update=' + update
        while 1:
            time.sleep(0.5)
            ru = self.session.get(url_room_update,headers={'User-Agent': 'Bot'})
            update = re.search('"update":\d+.\d+', ru.text).group(0)[9:]
            url_room_update = 'https://drrr.com/json.php?update=' + update
           # search "talks" block in room update response
            if 'talks' in ru.text:
                talks_update = re.findall('{"id".*?"message":".*?"}', re.search('"talks":.*', ru.text).group(0))
                # talk in "talks" block
                for tu in talks_update:
                    try:
                        info_sender = re.findall('"from":{.*?}', tu)
                        info_sender = info_sender[0]
                        name_sender = re.findall('"name":".*?"', info_sender)[0][8:-1]
                        message = re.search('"message":".*?"', tu).group(0)[11:-1].encode(encoding='utf-8').decode(
                        encoding='unicode-escape')
                        #msg_gui ='{}:{}'.format(name_sender,message)
                        return message,name_sender
                    except (IndexError, UnicodeDecodeError, UnboundLocalError):
                        print('.....')
            ru.close() 