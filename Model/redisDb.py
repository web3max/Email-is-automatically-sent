#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import redis
from Conf.config import Config # 引入配置文件

# 操控Redis类
class RedisDb:
    config = Config()
    redisConf = config.redis_conf()

    # 链接Redis
    connection = redis.Redis(host=redisConf['host'], port=redisConf['port'], db=0, password=redisConf['password'])

