#!/bin/bash

tar zxvf httpd-2.2.26.tar.gz
cd httpd-2.2.26
sudo ./configure --prefix=/usr/local/apache2/ --enable-proxy --enable-ssl --enable-cgi --enable-rewrite --enable-so --enable-module=so
sudo make
sudo make install
sudo chmod 777 -R /usr/local/apache2
sudo echo "ServerName 0.0.0.0:80" >> /usr/local/apache2/conf/httpd.conf
sudo echo "AddType application/x-httpd-php .php" >> /usr/local/apache2/conf/httpd.conf
sudo echo "Include conf/extra/httpd-ssl.conf" >> /usr/local/apache2/conf/httpd.conf
mkdir /usr/local/apache2/ssl
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /usr/local/apache2/ssl/apache.key -out /usr/local/apache2/ssl/apache.crt
sudo sed -i '120d' /usr/local/apache2/conf/extra/httpd-ssl.conf
sudo sed -i '129d' /usr/local/apache2/conf/extra/httpd-ssl.conf
sudo echo "SSLCertificateFile \"/usr/local/apache2/ssl/apache.crt\"">>/usr/local/apache2/conf/extra/httpd-ssl.conf
sudo echo "SSLCertificateKeyFile \"/usr/local/apache2/ssl/apache.key\"">>/usr/local/apache2/conf/extra/httpd-ssl.conf
sudo /usr/local/apache2/bin/apachectl start
