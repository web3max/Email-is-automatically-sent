#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("E:\Python\Redis-publishes-subscriptions")  # 导入自己编写的模块，填入项目模块对应存放路径
from Model.redisDb import *
import json
from Conf.config import Config # 引入配置文件

# 获取Redis配置
config = Config()
redisConf = config.redis_conf()

# 链接Redis
r = RedisDb().connection

# 需要发布的主题
channel = redisConf['channel'][0]

# 主题消息内容
msg = {'status': 'Y', 'MNSCode': '0002', 'TopicID': '283', 'Giftcard': '114', 'errmsg': ''}

# 发布订阅到Redis
r.publish(channel, json.dumps(msg))
