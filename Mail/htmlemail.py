#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("E:\Python\Redis-publishes-subscriptions")  # 导入自己编写的模块，填入项目模块对应存放路径
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from Conf.config import Config


class Email():
    def __init__(self, toAddr):
        # 初始化收件人
        self.to_addr = toAddr

    # 格式化一个邮件地址。
    # 注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    # 发送邮件
    def sed_email(self, giftCard, exchg, mnsSetting):
        # 创建配置对象,获取email信息
        config = Config()
        emailConf = config.email_conf()

        # 拼接V卡信息、兑换信息、订阅频道信息,构建HTML邮件内容
        msg = MIMEText('''<!doctype html>
                            <html lang="zh">
                                <head>
                                    <meta charset="UTF-8" />
                                    <title></title>
                                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                                    <meta name="viewport" content="width=device-width, initial-scale=1">
                                    <style type="text/css">
                                        table {
                                            border: 1px solid #ddd;
                                            border-collapse: collapse;
                                            border-spacing: 0;
                                            empty-cells: show;
                                            margin-bottom: 8px;
                                            outline: 0;
                                            background-color: transparent;
                                            box-sizing: border-box;
                                            color: #333;
                                            font-size: 15px;
                                            width: 80%;
                                            margin-left: 10%;
                                        }
                                        th {
                                            vertical-align: middle;
                                            text-align: right;
                                            font-weight: 500;
                                            padding: 5px 0;
                                        }
                                        td {
                                            vertical-align: middle;
                                            font-weight: 500;
                                            padding: 5px 0;
                                        }
                                        caption {
                                            margin: 0;
                                            padding: 5px 6px;
                                            color: #fff;
                                            background-color: #337ab7;
                                            border-top-left-radius: 3px;
                                            border-top-right-radius: 3px;
                                            text-align: left;
                                            font-size: 16px;
                                        }
                                        @media only screen and (max-width: 768px) {
                                            table {
                                                width: 100%;
                                            }
                                            th {
                                                padding: 5px 0px;
                                                font-size: 10px;
                                                width: 32%;
                                            }
                                            td {
                                                font-size: 10px;
                                            }
                                            caption {
                                                padding: 2px 8px;
                                                font-size: 13px;
                                            }
                                        }
                                    </style>
                                </head>
                                <body>
                                    <table border="1">
                                        <caption>V卡详情</caption>
                                        <tr>
                                            <th width="15%">客户名：</th>
                                            <td width="35%">''' + str(giftCard.CustomerName) + '''</td>
                                            <th width="15%">V卡ID：</th>
                                            <td width="35%">''' + str(giftCard.ID) + '''</td>
                                        </tr>
                                        <tr>
                                            <th>卡号：</th>
                                            <td>''' + str(giftCard.CardNO) + '''</td>
                                            <th>创建人：</th>
                                            <td>''' + str(giftCard.CreateBy) + '''</td>
                                        </tr>
                                        <tr>
                                            <th>创建时间：</th>
                                            <td>''' + str(giftCard.CreateDate) + '''</td>
                                            <th>方案：</th>
                                            <td>''' + str(giftCard.schmName) + '''</td>
                                        </tr>
                                        <tr>
                                            <th>激活人：</th>
                                            <td>''' + str(giftCard.ActiveBy) + '''</td>
                                            <th>兑换码：</th>
                                            <td>''' + str(giftCard.ExchgCode) + '''</td>
                                        </tr>
                                        <tr>
                                            <th>激活时间：</th>
                                            <td>''' + str(giftCard.ActiveDate) + '''</td>
                                            <th>激活状态：</th>
                                            <td>''' + ('''已激活''' if str(giftCard.IsActive) == 'Y' else '''未激活''') + '''</td>
                                        </tr>
                                        <tr>
                                            <th>兑换状态：</th>
                                            <td colspan="3">''' + (
            '''已兑换''' if str(giftCard.IsExchg) == 'Y' else '''未兑换''') + '''</td>
                                        </tr>
                                    </table>
                                    <table border="1">
                                        <caption>兑换详情</caption>
                                        <tr>
                                            <th width="15%">兑换ID：</th>
                                            <td width="35%">''' + str(exchg.ID) + '''</td>
                                            <th width="15%">兑换商品编号：</th>
                                            <td width="35%"></td>
                                        </tr>
                                        <tr>
                                            <th>收货人姓名：</th>
                                            <td>''' + str(exchg.ShippingBy) + '''</td>
                                            <th>商品名称：</th>
                                            <td>''' + str(exchg.ProductName) + '''</td>
                                        </tr>
                                        <tr>
                                            <th>手机号：</th>
                                            <td>''' + str(exchg.MobileNO) + '''</td>
                                            <th>供应商：</th>
                                            <td></td>
                                        </tr>
                                        <tr>
                                            <th>收货地址：</th>
                                            <td>''' + exchg.Province + exchg.City + exchg.Area + exchg.ShippingAdress + '''</td>
                                            <th rowspan="4">商品图：</th>
                                            <td rowspan="4"><img width="180"/></td>
                                        </tr>
                                        <tr>
                                            <th>物流公司：</th>
                                            <td>''' + str(exchg.ExpressCompanyName) + '''</td>
                                        </tr>
                                        <tr>
                                            <th>快递单号：</th>
                                            <td>''' + str(exchg.ShipOrderNo) + '''</td>
                                        </tr>
                                        <tr>
                                            <th>发货人：</th>
                                            <td>''' + str(exchg.ShippingTo) + '''</td>
                                        </tr>
                                    </table>
                                </body>
                            </html>''', 'html', 'utf-8')
        # 添加邮件发件人
        msg['From'] = self._format_addr('%s <%s>' % (emailConf['sender'], emailConf['username']))
        # 添加邮件收件人
        msg['To'] = self._format_addr('尊敬的客户 <%s>' % self.to_addr)
        # 添加邮件主题
        msg['Subject'] = Header(mnsSetting.MNSName, 'utf-8').encode()
        try:
            server = smtplib.SMTP(emailConf['stmp'], emailConf['port'])
            server.ehlo()
            # 创建SSL安全连接
            server.starttls()
            server.set_debuglevel(1)
            server.login(emailConf['username'], emailConf['password'])
            server.sendmail(emailConf['username'], self.to_addr, msg.as_string())
            server.quit()
            sendMsg = {'SubStatus': 'Y', 'SubContent': '{"status":"Y",content:"邮件发送成功"}', 'ErrContent': ''}
            return sendMsg
        except smtplib.SMTPException as e:
            sendMsg = {'SubStatus': 'N', 'SubContent': '{"status":"N",content:"邮件发送失败"}', 'ErrContent': str(e)}
            return sendMsg
