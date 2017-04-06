# Email-is-automatically-sent
结合Python、MySQL、Redis发布订阅功能，实现Email自动发送

### 1. 安装pip
windows 安装时pip默认安装；自定义安装请勾选安装pip选项

### 2. 查看pip版本
* pip -V

### 3. 使用pip安装以下库
* pip install sqlacodegen
* pip install mysql-connector==2.1.4
* pip install sqlalchemy
* pip install redis
* pip install requests
* pip install setuptools

### 4. 查看已安装的库
* pip list

### 5. 查看Python版本
* python -V

### 6. 查看Python安装路径
**1. Python交互模式下查看Python安装路径**
```
    >>> import sys
    >>> path = sys.executable
    >>> print(path)
```

**2. Linux命令行模式下查看Python安装路径**
* which python


#### Centos7搭建Python3.6开发环境
> **Tip:**
> - 文件编辑尽量使用vi操作,可以避免linux和windows字符编码不一致带来的问题

**1. 一键安装脚本,包含许多必需库,不需要中途再次重新编译**

```
wget https://raw.githubusercontent.com/LunacyZeus/Python3.6-for-Centos7.0/master/install.sh && sh install.sh
```
**以下就是上面的脚本执行代码，你也可以按步骤执行安装**
```
#Centos 7.0 安装Python3.6脚本
#作者: LunacyZeus
#Git主页: https://github.com/LunacyZeus

echo "Python3.6 for Centos 7.0 一键安装脚本\nGitHub主页地址: https://github.com/LunacyZeus\n这个脚本是我在经过多次测试后做出来的,安装了Python要用的所有的必需库(如有缺少,请指出,谢谢!),不会出现在使用中需要某些库而重新编译安装Python的蛋疼事情: 本脚本在腾讯云亲测可用. 遇到问题请在Github提交BUG"

read -p "请按任意键以继续" var


echo "Let's Go..."

echo "安装开发环境工具..."
yum groupinstall -y "Development tools"

echo "安装编译Python必需工具..."
yum install -y nano nginx sqlite-devel screen ncurses-devel ncurses-libs zlib-devel mysql-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-develtk-devel gdbm-devel db4-devel libpcap-devel xz-devel openssl-devel

echo "获取并解压Python3.6源码..."
wget http://on0aob5yd.bkt.clouddn.com/Python-3.6.0.tar.xz && tar xvJf Python-3.6.0.tar.xz && cd Python-3.6.0

echo "构建Python3.6..."
./configure
echo "编译安装Python3.6..."
make&& make install

echo "好了,你的Python3.6 for Centos7.0之旅正式开始啦~"
```
> **Tip: CentOS查找目录或文件**
> - 查找目录：find / -name '查找关键字' -type d
> - 查找文件：find / -name python -print
> - find / -name "pip3*"
> - whereis python
> - whereis python3
> - which python3

**2. 命令创建Python软连接**

```
mv  python python.backup
ln -s /usr/local/bin/python3.6 /usr/bin/python
ln -s /usr/local/bin/python3.6 /usr/bin/python3

# 查看python3.6是否安装成功
python -V
```

**3. 更改yum脚本的python依赖**

```
cd /usr/bin
ls yum*
yum yum-config-manager yum-debug-restore yum-groups-manager
yum-builddep yum-debug-dump yumdownloader
```

更改以上文件头,把 #!/usr/bin/python 改为 #!/usr/bin/python2

**4. 修改gnome-tweak-tool配置文件**

```
# vi /usr/bin/gnome-tweak-tool
```

把文件头 #!/usr/bin/python 改为 #!/usr/bin/python2

**5. 修改urlgrabber配置文件**

```
# vi /usr/libexec/urlgrabber-ext-down
```

把文件头 #!/usr/bin/python 改为 #!/usr/bin/python2

**6. 新建pip的软连接**
```
mv /usr/bin/pip /usr/bin/pip.bak
cp /usr/local/bin/pip3 /usr/bin/pip

# 查看pip是否安装成功
pip -V
```

**7. 使用pip安装以下库**

```
pip install sqlacodegen
pip install mysql-connector==2.1.4
pip install sqlalchemy
pip install redis
pip install requests
pip install setuptools
pip install pymysql

# 查看已安装的库
pip list
```
**8. 开机自动启动脚本pythonemail**

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
> **Tip:**
> - 脚本可以先执行一下看看报不报错
> ```
> cd /etc/rc.d/init.d
> chmod +x pythonemail
> ./pythonemail start
> ```


**9. 赋予脚本权限**
```
cd /etc/rc.d/init.d
chmod +x pythonemail
chkconfig --add pythonemail
chkconfig --list pythonemail
```
这样脚本开机就会自动运行

> **也可以后台静默执行,每一次重新开机启动需要重新执行命令**
> ```
> cd /etc/rc.d/init.d
> chmod +x pythonemail
> nohup ./pythonemail start &
> 回车
> exit
> ```
> 不能直接关闭shell窗口,不然不会在后台静默执行,一定要exit退出登录后,再关闭shell窗口

> **Tip:**
> - CentOS重启命令：reboot
> - 如果邮件发送不出去也有可能是服务器端口的问题，需要在服务器安全组中打开对应的端口









