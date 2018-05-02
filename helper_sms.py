# -*- coding: utf-8 -*-
import json

import requests


class SMS(object):
    def __init__(self, **kwargs):
        self.host = kwargs['host']
        self.port = kwargs['port']
        self.headers = {
            'content-type': 'application/json',
            'apikey': kwargs['apikey']
        }
        self.path = '/sms'
        self.status = False

    def sms_send(self, content, mobiles, user):
        """发送短信"""
        url = 'http://{0}:{1}{2}/sms'.format(self.host, self.port, self.path)
        data = {'content': content, 'mobiles': mobiles, 'user_name': user}
        try:
            r = requests.post(url, headers=self.headers, data=json.dumps(data))
            if r.status_code == 201:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

