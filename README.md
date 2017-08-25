![Contrast](http://upload-images.jianshu.io/upload_images/6171922-b9f0e2cc255018ee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

结合 Python、MySQL、Redis 发布订阅功能，实现 Email 自动发送 HTML 模版邮件.
## 1. Centos7 上搭建 Python3.6 开发环境
这个可以产考我的另一篇文章[CentOS7.3 编译安装 Python3.6.2](http://www.jianshu.com/p/7a76bcc401a1)

**使用 pip 安装以下库**

```
pip install sqlacodegen
pip install mysql-connector==2.1.4
pip install sqlalchemy
pip install redis
pip install requests
pip install setuptools
pip install pymysql
```
**查看已安装的库**
```
pip list
```

## 2. 查看Python安装路径
**Python交互模式下查看Python安装路径**
```
    >>> import sys
    >>> path = sys.executable
    >>> print(path)
```

**命令行模式下查看Python安装路径**
* which python

## 3. 使用SQLAlchemy创建数据模型
**pymysql**
```
sqlacodegen mysql+pymysql://root:653155073@192.168.0.107:3306/pythonemail > models.py
```
也可以导出某一张表的数据模型

```
sqlacodegen mysql+pymysql://root:653155073@192.168.0.107:3306/pyemail --tables test_user > models.py
```


**sqlalchemy**

```
sqlacodegen mysql+mysqlconnector://root:653155073@192.168.0.107:3306/pythonemail > models.py
```
也可以导出某一张表的数据模型
```
sqlacodegen mysql+mysqlconnector://root:653155073@192.168.0.107:3306/pyemail --tables test_user>models.py
```
## 4. 开机自动启动脚本pythonemail

```
#!/bin/sh
#chkconfig: 23456 80 90
#description:auto_run
lock="subscription.py"
start(){
        echo "service start...."
        su root -c "/usr/local/bin/python /usr/local/apache2/htdocs/python_email/Subscription/subscription.py &"
}
stop(){
    echo "service stop...." pkill -f $lock
}
status(){
        if [ -e $lock ];then
            echo "$0 service start"
        else
            echo "$0 service stop"
        fi
}
restart(){
        stop
        start
}
case "$1" in
"start")
        start
        ;;
"stop")
        stop
        ;;
"status")
        status
        ;;
"restart")
        restart
        ;;
*)
        echo "$0 start|stop|status|restart"
        ;;
esac
```
把脚本 pythonemail 放入 /etc/rc.d/init.d 文件夹下

**脚本可以先执行一下看看报不报错**
```
cd /etc/rc.d/init.d
chmod +x pythonemail
./pythonemail start
```

**赋予脚本权限**
```
cd /etc/rc.d/init.d
chmod +x pythonemail
chkconfig --add pythonemail
chkconfig --list pythonemail
```
这样脚本开机就会自动运行

**也可以后台静默执行,每一次重新开机启动需要重新执行命令**
```
cd /etc/rc.d/init.d
chmod +x pythonemail
nohup ./pythonemail start &
 回车
exit
```
> 不能直接关闭shell窗口,不然不会在后台静默执行,一定要exit退出登录后,再关闭shell窗口

> **Tip:**
> - CentOS重启命令：reboot
> - 如果邮件发送不出去也有可能是服务器端口的问题，需要在服务器安全组中打开对应的端口.

这里我并不会讲具体的实现,只讲前期准备,具体的代码实现参考 Github 上的源码
[**结合 Python、MySQL、Redis 发布订阅功能，实现 Email 自动发送**](https://github.com/longhuicode/Email-is-automatically-sent),源码中有详细的注释说明,理解起来不难,欢迎大家提意见.