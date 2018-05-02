# -*- coding: utf-8 -*-
import json

import requests


class UnionKakou(object):
    def __init__(self, **kwargs):
        self.base_path = 'http://{0}:{1}{2}'.format(
            kwargs['host'], kwargs['port'], '/union-data')
        self.headers = {
            'content-type': 'application/json',
            'apikey': kwargs['apikey']
        }
        self.status = False


    def get_alarm_maxid(self):
        """获取过车报警最大ID值"""
        url = '{0}/alarm/maxid'.format(self.base_path)
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

    def get_alarm_by_id(self, _id):
        """根据ID范围获取过车报警信息"""
        url = '{0}/alarm/{1}'.format(self.base_path, _id)
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200 or r.status_code == 404:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise


    def get_traffic_crossing_info(self, param):
        """根据ID获取卡口地点信息"""
        url = '{0}/traffic_crossing_info?q={1}'.format(
            self.base_path, json.dumps(param))
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise


    def get_traffic_crossing_info_by_id(self, crossing_id):
        """根据ID获取卡口地点信息"""
        url = '{0}/traffic_crossing_info/{1}'.format(
            self.base_path, crossing_id)
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200 or r.status_code == 404:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise


    def get_control_unit(self, param):
        """根据ID获取控制单元信息"""
        url = '{0}/control_unit?q={1}'.format(
            self.base_path, json.dumps(param))
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise


    def get_control_unit_by_id(self, control_unit_id):
        """根据ID获取控制单元信息"""
        url = '{0}/control_unit/{1}'.format(
            self.base_path, control_unit_id)
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200 or r.status_code == 404:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise


    def get_traffic_sysdict(self, param):
        """获取配置信息"""
        url = '{0}/traffic_sysdict?q={1}'.format(
            self.base_path, json.dumps(param))
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200 or r.status_code == 404:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise


    def get_stat(self, param):
        """根据条件流量统计"""
        url = '{0}/stat'.format(self.base_path)
        try:
            r = requests.get(url, headers=self.headers, params=param)
            #print(r.url)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise