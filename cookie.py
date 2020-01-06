import requests
import time
import json
import os , re


class Cookie_Server(object):
    def __init__(self, name='palmeiras', icon="Zaika"):
        self.name = name
        self.icon = icon
        self.session = requests.session()

    def save_cookie(self, file_name):
        f = open(file_name, 'w+')
        f.write(str(self.session.cookies.get_dict()))
        f.close()

    def load_cookie(self, file_name):
        f = open(file_name, 'r')
        self.session.cookies.update(eval(f.read()))
        f.close()

    def login(self):
        home = self.session.get('https://drrr.com',headers={'User-Agent': 'Bot'})
        token = re.search('<input type="hidden" name="token" data-value=".*?">', home.text).group(0)[-34:-2]
        home.close()
        login_body = {
            'name': self.name,
            'login': 'ENTER',
            'token': token,
            'direct-join': '',
            'language': 'en-US',
            'icon': self.icon
        }
        li = self.session.post('https://drrr.com', login_body, headers={'User-Agent': 'Bot'})
        li.close()