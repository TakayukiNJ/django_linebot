from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import urllib.request
import json


REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"

ACCESSTOKEN = 'tLtokJ+pzJsjBdaEG3ceJtiBtJwGwJLadaAztFQHvSiuC6LS5HBvLwOQEvIdHXYImBgfj4QTiXcgP7EnL+ouYCWZqGSv/aAF/jgt3JZ5ZK7w8kOlem8bkRC11yruCzr1wZN8uCF7Ybvsdz9+R31ELgdB04t89/1O/w1cDnyilFU='   #MessagingAPI設定|>チャネルアクセストークンからアクセストークンを取得
HEADER = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + ACCESSTOKEN
}

class LineMessage():
    def __init__(self, messages):
        self.messages = messages

    def reply(self, reply_token):
        body = {
            'replyToken': reply_token,
            'messages': self.messages
        }
        print(body)
        req = urllib.request.Request(REPLY_ENDPOINT_URL, json.dumps(body).encode(), HEADER)
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err.reason)