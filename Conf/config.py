#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 配置类
class Config:
    # Redis配置
    def redis_conf(self):
        redisConf = {
            "host": '',  # Redis连接IP
            "port": '',  # 连接端口
            "password": '',  # 登录密码
            "channel": [  # 需要发布和订阅的主题

            ]
        }
        return redisConf

    # MySQL配置
    def db_conf(self):
        dbConf = {
            "host": '',  # MySQL连接IP
            "user": '',  # 登陆名
            "password": '',  # 登录密码
            'db': '',  # 数据库名
            'port': ''  # 连接端口
        }
        return dbConf

    # Email配置
    def email_conf(self):
        emailConf = {
            'sender': '',  # 发件人
            'stmp': 'smtp.qq.com',  # smtp地址
            'username': '',  # 登陆名
            'password': '',  # 登录口令
            'smtp_secure': 'ssl',  # 安全ssl
            'port': '465',  # QQ邮箱端口
        }
        return emailConf
