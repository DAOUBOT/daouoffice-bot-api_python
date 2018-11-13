Python DaouOffice Bot Api
==========================

[![DaouOffice Bot API](https://img.shields.io/badge/DaouOffice%20Bot%20API-v.0.1.9-00aced.svg)](https://github.com/DAOUBOT/daouoffice-bot-api/blob/master/docs/api.md) [![Build Status](https://travis-ci.org/DAOUBOT/daouoffice-bot-api.svg?branch=master)](https://travis-ci.org/DAOUBOT/daouoffice-bot-api) [![Node Version](https://img.shields.io/node/v/passport.svg)](https://nodejs.org/en/) [![DaouOffice Version](https://img.shields.io/badge/DaouOffice(Custom)-%3E%3D%202.5.4.0-orange.svg)](http://bot.terracetech.co.kr)

Python module to interact with official DaouOffice Bot API. A bot apikey is required and can be obtained by http://bot.terracetech.co.kr:8000

Install
-------

```bash
pip install daou-chat-bot
```

Usage
-----

```py

from daou_chat_bot import daou_chat_bot
import requests
import json

options = {
    "daouApiUrl" : "http://172.22.1.103:8000",
    "botServerPort" : 3000,
    "apiKey" : "O6hFGmkAnjg0Eu4vYOHwzg=="
};

chatBot = daou_chat_bot.daou_chat_bot(options)


def rescvieMsg(self, request):
    print("rescvieMsg")
    content = request.json
    print(json.dumps(content))
    message = content.get('message').get('content')
    chatBot.sendMessage(content.get('buddySeq'), content.get('chatInfo'), message)
    return 'OK'

chatBot.start(rescvieMsg)

```

Documentation
-------------

-	[API Reference](https://github.com/DAOUBOT/daouoffice-bot-api/blob/master/docs/api.md)

Test
----

**Note:** The following command creates an html report under the local mochawesome-report folder.

License
-------

**The MIT License (MIT)**
