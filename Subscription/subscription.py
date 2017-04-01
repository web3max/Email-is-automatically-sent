#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("E:\Python\Redis-publishes-subscriptions")  # 导入自己编写的模块，填入项目模块对应存放路径
from Model.redisDb import *
import json
from Model.db import *
from Mail.htmlemail import *
from Conf.config import Config # 引入配置文件

config = Config()
redisConf = config.redis_conf()

# 链接Redis
r = RedisDb().connection

# 订阅频道应该要和发布的频道一样，否则将无法订阅到发布者发布的消息
# 这里订阅了配置文件中的所有频道
channel = redisConf['channel']

# 创建监听实例
msg_queue = r.pubsub()

# 监听channel频道
msg_queue.subscribe(channel)

# 订阅监听
for msg in msg_queue.listen():
    if msg['type'] == 'message':
        info = json.loads(msg['data'])
        # 创建查询对象
        select = Db()
        # 查询V卡信息,兑换信息
        giftCard = select.select_gift_card(info['Giftcard'])
        # 查询V卡方案名称
        giftCard.HlhGiftcard.schmName = select.select_schema(giftCard.HlhGiftcard.SchemaID)
        # 查询主题信息
        mnsSetting = select.select_mnssetting(info['MNSCode'])
        # 创建发送邮件对象,传入收件人邮箱地址
        # 群发则传入list
        email = Email('********@qq.com')
        # 传入V卡信息、兑换信息、频道信息;发送邮件
        sendMsg = email.sed_email(giftCard.HlhGiftcard, giftCard.HlhGiftcardexchg, mnsSetting)
        # 插入邮件发送记录
        select.insert_mnssublog(info, sendMsg)
        # 关闭数据库链接
        select.finish()
