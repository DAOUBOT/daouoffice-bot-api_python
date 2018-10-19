from flask import Flask
from flask import request
from random import *
import requests
import json
import os


class DaouOfficeBot:

    def __init__(self, option):
                print(option)
                self.apiKey = option.get("apiKey")
                self.daouApiUrl = option.get("daouApiUrl")
                self.botServerPort = option.get("botServerPort")
                self.app = Flask(__name__)

    def start(self, cb):
        print('==== start ====')
        @self.app.route('/')
        def hello_world():
            return 'Hello World!'

        @self.app.route('/message', methods=['GET','POST'])
        def message():
            print('==== Receive Message ====')
            cb(self, request);
            return 'OK'
            

        self.app.run(host='0.0.0.0', port=self.botServerPort)
        
        
    def sendMessage(self, buddySeq, chatInfo, message):
        print('==== Send Message ====')
        print('buddySeq = ' + str(buddySeq))
        print('chatInfo = ' + str(chatInfo))
        print('message = ' + message)

        chattype = chatInfo.get('type')
        isSingle = False
        if chattype == 'SINGLE':
            isSingle = True

        param = {}
        param['apiKey'] = self.apiKey
        param['message'] = { "content": message }
        print(json.dumps(param))
        path = '/go/public/bot'
        path += "/single/" if isSingle else "/room/"
        path += str(buddySeq)
        URL = self.daouApiUrl + path
        print('URL = ' + URL)
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        requests.post(URL, headers=headers, data=json.dumps(param))
        return 'OK'






