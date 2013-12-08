#!/bin/bash
#解压apache2源码压缩包
tar zxvf httpd-2.2.26.tar.gz
#进入解压后目录
cd httpd-2.2.26
#配置编译选项并生成makefile文件，其中--prefix是指明安装的目录,enable是开启apache的附加功能
sudo ./configure --prefix=/usr/local/apache2/ --enable-proxy --enable-ssl --enable-cgi --enable-rewrite --enable-so --enable-module=so
#使用makefile文件进行编译
sudo make
#安装apache2
sudo make install
#修改文件夹操作权限，为了后面能用命令修改配置文件
sudo chmod 777 -R /usr/local/apache2
#添加ServerName到配置文件
sudo echo "ServerName 0.0.0.0:80" >> /usr/local/apache2/conf/httpd.conf
#添加.php运行支持
sudo echo "AddType application/x-httpd-php .php" >> /usr/local/apache2/conf/httpd.conf
#添加ssl模块，即开启ssl的功能
sudo echo "Include conf/extra/httpd-ssl.conf" >> /usr/local/apache2/conf/httpd.conf
#创建名为ssl的文件夹，用于存放证书等
mkdir /usr/local/apache2/ssl
#用自签名方式生成证书和key
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /usr/local/apache2/ssl/apache.key -out /usr/local/apache2/ssl/apache.crt
#删除配置文件中默认的证书路径
sudo sed -i '120d' /usr/local/apache2/conf/extra/httpd-ssl.conf
#同上
sudo sed -i '129d' /usr/local/apache2/conf/extra/httpd-ssl.conf
#添加证书的新路径到配置文件
sudo echo "SSLCertificateFile \"/usr/local/apache2/ssl/apache.crt\"">>/usr/local/apache2/conf/extra/httpd-ssl.conf
#同上
sudo echo "SSLCertificateKeyFile \"/usr/local/apache2/ssl/apache.key\"">>/usr/local/apache2/conf/extra/httpd-ssl.conf
#启动apache2
sudo /usr/local/apache2/bin/apachectl start
