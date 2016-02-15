This is autoinstaller for automatically install and configure apache or nginx with MySQL and PHP. On install time Apache or nGinx script will ask about virtual host domain name. On install time for MySQL database script will ask questions about MySQL root pass, new database name, new username and password for the new user.

Main script is ap-ng-vhost.py

Requirements:

1. CentOS 6.7 or higher(or any yum based Linux).

2. Python2.7 must be installed to your Linux server.

3. Download all files to the Linux server and execute ap-ng-vhost.py script.


For test virtual domain name just add your server IP and virtual name to c:\windows\system32\drivers\etc\hosts file for Windows or /etc/hosts file for Linux as follows:
172.16.100.10 unix.com

