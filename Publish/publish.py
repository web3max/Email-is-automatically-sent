#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Model.redisDb import *
import json
from Conf.config import Config # 引入配置文件

# 获取Redis配置
config = Config()
redisConf = config.redis_conf()

# 链接Redis
r = RedisDb().connection

# 创建主题
channel = redisConf['channel'][2]

# 主题消息内容
msg = {'status': 'Y', 'MNSCode': '0002', 'TopicID': '283', 'Giftcard': '114', 'errmsg': ''}

# 发布订阅到Redis
r.publish(channel, json.dumps(msg))
