# -*- coding: utf-8 -*-
import json

import requests


class Kakou(object):
    def __init__(self, **kwargs):
        self.host = kwargs['host']
        self.port = kwargs['port']
        self.headers = {'content-type': 'application/json'}

        self.status = False

    def get_maxid(self):
        """获取最大ID值"""
        url = u'http://{0}:{1}/alarm_maxid'.format(self.host, self.port)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: %s, status: %s, %s' % (
                    url, r.status_code, r.text))
        except Exception as e:
            self.status = False
            raise

    def get_vehicle_by_id(self, _id):
        """根据ID范围获取车辆信息"""
        url = u'http://{0}:{1}/alarm/{2}'.format(
            self.host, self.port, _id)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: %s, status: %s, %s' % (
                    url, r.status_code, r.text))
        except Exception as e:
            self.status = False
            raise

    def get_kkdd_by_id(self, kkdd_id):
        """根据车牌号码获取布控信息"""
        url = u'http://{0}:{1}/kkdd/{2}'.format(
            self.host, self.port, kkdd_id)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: %s, status: %s, %s' % (
                    url, r.status_code, r.text))
        except Exception as e:
            self.status = False
            raise

