# -*- coding: utf-8 -*-
import os
import time
import datetime
import json

import arrow
import requests

from helper_kakou import Kakou
from helper_sms import SMS
from ini_conf import MyIni
from my_logger import *


debug_logging(u'logs/error.log')
logger = logging.getLogger('root')


class BKCPAlarm(object):
    def __init__(self):
        self.my_ini = MyIni()

        self.sms = SMS(**self.my_ini.get_sms())
        self.kakou = Kakou(**self.my_ini.get_kakou())

        self.id_flag = 1

        self.fx = {
            1: u'由东向西',
            2: u'由西向东',
            3: u'由南向北',
            4: u'由北向南',
            9: u'进城',
            10: u'出城'
        }
        # 布控车牌字典形如 {'粤LXX266': {'kkdd': '东江大桥卡口',
        # 'jgsj': <Arrow [2016-03-04T09:39:45.738000+08:00]>}}
        #self.bkcp_dict = {}
        
    def __del__(self):
        del self.my_ini

    def send_sms(self, content, mobiles):
        """发送短信"""
        try:
            self.sms.sms_send(content, mobiles)
	    logger.info(content)
	    logger.info(mobiles)
        except Exception as e:
            logger.error(e)
        
    def loop_get_data(self):
        self.id_flag = self.kakou.get_maxid()['maxid']
        while 1:
            try:
                maxid = self.kakou.get_maxid()['maxid']
                if maxid > self.id_flag:
                    info = self.kakou.get_vehicle_by_id(maxid)
                    kkdd = self.kakou.get_kkdd_by_id(info['crossing_id'])
                    content = u"[{0}卡口报警]{1},{2},{3},{4}".format(
                        kkdd['city_name'], info['pass_time'], kkdd['kkdd_name'],
                        self.fx.get('direction_index', u'进城'), info['plate_no'])
                    self.send_sms(content, info['mobiles'])
		self.id_flag = maxid
                time.sleep(1)
            except Exception as e:
                logger.error(e)
                time.sleep(5)

