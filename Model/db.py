#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.models import *
from Conf.config import Config

# 操控数据库类
class Db:
    config = Config()
    # 获取数据库配置
    dbConf = config.db_conf()
    # 初始化数据库连接:
    query = 'mysql+mysqlconnector://' + dbConf['user'] + ':' + dbConf['password'] + '@' + dbConf['host'] + ':' + \
            dbConf['port'] + '/' + dbConf['db']
    # 链接数据库
    engine = create_engine(query)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建Session:
    session = DBSession()

    # 查询hlh_giftcard,hlh_giftcardexchg数据
    def select_gift_card(self, info):
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        giftCard = self.session.query(HlhGiftcard, HlhGiftcardexchg).outerjoin(HlhGiftcardexchg,
                                                                               HlhGiftcard.ID == HlhGiftcardexchg.GiftCardID).filter(
            HlhGiftcard.ID == int(info)).one()
        return giftCard

    # 查询hlh_mnssetting数据
    def select_mnssetting(self, info):
        mnsSetting = self.session.query(HlhMnssetting).filter(HlhMnssetting.MNSCode == int(info)).one()
        return mnsSetting

    # 插入数据hlh_mnssublog
    def insert_mnssublog(self, info, sendMsg):
        # 创建新HlhMnssublog对象:
        new_mnssublog = HlhMnssublog(MNSPubID=int(info['TopicID']), MNSSubID=int(info['MNSCode']),
                                     SubDate=time.strftime('%Y%m%d%H%I%S', time.localtime(time.time())),
                                     SubContent=sendMsg['SubContent'], SubStatus=sendMsg['SubStatus'],
                                     ErrContent=sendMsg['ErrContent'])
        # 添加到session:
        self.session.add(new_mnssublog)
        # 提交即保存到数据库:
        self.session.commit()

    # 查询方案名
    def select_schema(self, info):
        schmName = self.session.query(HlhSchema.SchmName).filter(HlhSchema.ID == info).one()
        return schmName[0]

    # 关闭Session
    def finish(self):
        self.session.close()
