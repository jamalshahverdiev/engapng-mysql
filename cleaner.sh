rm -rf /var/www/
rm -rf /usr/local/domen/
rm -rf /var/log/httpd/
rm -rf /etc/httpd
rm -rf /var/lib/mysql/
rm -rf /etc/nginx/
rm -rf /var/log/nginx/
rm -rf /etc/php-fpm.d/
yum remove -y httpd 
yum remove -y php php-mysql
yum -y remove mysql mysql-server mysql-libs
yum -y remove mysqlclient16-5.1.61-4.ius.centos6.x86_64
yum -y remove nginx php-fpm
