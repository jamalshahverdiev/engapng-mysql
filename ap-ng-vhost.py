#!/bin/env python2.7

# Author Jamal Shahverdiev

import cmd
import time
import sys
import os

def ap():
    print('\nScript require domain name.')
    arg1 = raw_input('Please enter domain name: ')
    os.system('yum -y install epel-release')
    os.system('yum -y install httpd mod_ssl openssl')
    os.system('mkdir -p /usr/local/domen/')
    os.system('mkdir /var/log/httpd/')
    os.system('/bin/cp -f `pwd`/httpd.conf /etc/httpd/conf/')
    os.system('echo \"Include /usr/local/domen/*\" >> /etc/httpd/conf/httpd.conf')
    os.system('mkdir -p /var/www/'+arg1+'/public_html')
    os.system('chown -R apache:apache /var/www/'+arg1+'/public_html')
    os.system('chown -R apache:apache /usr/local/domen/')
    os.system('chmod 755 /var/www')
    os.system('touch /var/www/'+arg1+'/public_html/index.html')

    reps = {'www.domain.lan':arg1}
    with open('/var/www/'+arg1+'/public_html/index.html', 'w') as outfile:
        with open(os.getcwd()+'/tempindex.html', 'r') as infile:
            for line in infile:
                for src, target in reps.iteritems():
                    line = line.replace(src, target)
                outfile.write(line)

    vhf = {'domain':arg1}
    with open('/usr/local/domen/'+arg1, 'w') as outfile:
        with open(os.getcwd()+'/domain', 'r') as infile:
            for line in infile:
                for src, target in vhf.iteritems():
                    line = line.replace(src, target)
                outfile.write(line)

    os.system('touch /var/log/httpd/'+arg1+'_error.log')
    os.system('touch /var/log/httpd/'+arg1+'_access.log')
    os.system('chkconfig httpd on')
    os.system('/etc/init.d/httpd start')
    time.sleep(3)
    apidfile = '/var/run/httpd/httpd.pid'
    if os.path.isfile(apidfile):
        print('\nApache web server installed and virtual host configured.')
    else:
        print('There is problem when apache web server tired to start')
        sys.exit()
    print('\n\n################################################################')
    print('1. For install and configure PHP and MySQL please write 1 and click to ENTER button.')
    print('2. For exit from script, plase write 2 and click the ENTER button.')
    arg2 = raw_input('Please select your choise: ')

    if arg2 == str or len(arg2) != 1:
        print("\nYou can write only numbers 1 or 2.")
        sys.exit()
    elif len(arg2) == 1 and (arg2 == 1 or arg2 == 2):
        pass

    if int(arg2) == 1:
        os.system('yum -y install mysql-server.x86_64 php php-mysql')
        os.system('/etc/init.d/mysqld start')
        os.system('chkconfig mysqld on')
        os.system('service httpd restart')
        print('\n\n')
        mpidfile = '/var/run/mysqld/mysqld.pid'
        if os.path.isfile(mpidfile):
            print('Configure MySQL security.....')
            time.sleep(3)
            os.system('mysql_secure_installation')
        else:
            print('MySQL is not working')
            sys.exit()
        time.sleep(3)
        print('MySQL already configured..........')
        sqlroot = raw_input('Enter MySQL root user password: ')
        newdb = raw_input('Enter name for new database: ')
        newdbuser = raw_input('Enter new mysql user name: ')
        newdbpass = raw_input('Enter password for new '+newdbuser+': ')
        os.system('mysql -u root -p%s -e "CREATE DATABASE %s;"' %(sqlroot, newdb))
        os.system('mysql -u root -p%s -e "GRANT ALL PRIVILEGES ON %s.* TO %s@localhost IDENTIFIED BY \'%s\';"' %(sqlroot, newdb,newdbuser, newdbpass))
        os.system('mysql -u root -p%s -e "FLUSH PRIVILEGES;"' %(sqlroot))

        replacements = {'saytdb':newdb, 'saytuser':newdbuser, 'freebsd':newdbpass}
        with open('/var/www/'+arg1+'/public_html/index.php', 'w') as outfile:
            with open(os.getcwd()+'/tempindex.php', 'r') as infile:
                for line in infile:
                    for src, target in replacements.iteritems():
                        line = line.replace(src, target)
                    outfile.write(line)

        os.system('/etc/init.d/httpd restart')
        print('\nApache web server is installed and working\n\n')
    else:
        sys.exit()

def ng():
    print('\nScript require domain name.')
    arg1 = raw_input('Please enter domain name: ')

    os.system('yum -y install epel-release')
    os.system('yum -y install nginx')
    os.system('mkdir -p /var/www/'+arg1+'/public_html')
    os.system('chown -R nginx:nginx /var/www/'+arg1+'/public_html')
    os.system('chmod 755 /var/www')
    os.system('touch /var/www/'+arg1+'/public_html/index.html')

    nghtreps = {'ngsec.lan':arg1}
    with open('/var/www/'+arg1+'/public_html/index.html', 'w') as outfile:
        with open(os.getcwd()+'/ngindex.html', 'r') as infile:
            for line in infile:
                for src, target in nghtreps.iteritems():
                    line = line.replace(src, target)
                outfile.write(line)

    os.system('touch /etc/nginx/conf.d/'+arg1+'.conf')

    ngvhcnfreps = {'ngsec.lan':arg1}
    with open('/etc/nginx/conf.d/'+arg1+'.conf', 'w') as outfile:
        with open(os.getcwd()+'/ngsec.conf', 'r') as infile:
            for line in infile:
                for src, target in ngvhcnfreps.iteritems():
                    line = line.replace(src, target)
                outfile.write(line)

    os.system('chkconfig nginx on')
    os.system('/etc/init.d/nginx restart')
    time.sleep(3)
    os.system('/bin/cp -f `pwd`/nginx.conf /etc/nginx/')

    ngpfile = '/var/run/nginx.pid'
    if os.path.isfile(ngpfile):
        print('\nNginx web server installed and virtual host created.\n\n')
    else:
        print('There is problem when nginx web server tired to start.')
        sys.exit()

    print('################################################################')
    print('1. For install and configure PHP-FPM and MySQL please write 1 and click to ENTER button.')
    print('2. For exit from script, plase write 2 and click the ENTER button.')
    arg2 = raw_input('Please select your choise: ')

    if arg2 == str or len(arg2) != 1:
        print("\nYou can write only numbers 1 or 2.")
        sys.exit()
    elif len(arg2) == 1 and (arg2 == 1 or arg2 == 2):
        pass

    if int(arg2) == 1:
        os.system('yum -y install mysql-server.x86_64 php-fpm php-mysql')
        os.system('/etc/init.d/mysqld start')
        os.system('chkconfig mysqld on')
        os.system('service nginx restart')
        print('\n\n')
        mpidfile = '/var/run/mysqld/mysqld.pid'
        if os.path.isfile(mpidfile):
            print('Configure MySQL security.....')
            time.sleep(3)
            os.system('mysql_secure_installation')
        else:
            print('MySQL is not working')
            sys.exit()	
        time.sleep(3)
        print('MySQL already configured..........')
        sqlroot = raw_input('Enter MySQL root user password: ')
        newdb = raw_input('Enter name for new database: ')
        newdbuser = raw_input('Enter new mysql user name: ')
        newdbpass = raw_input('Enter password for new '+newdbuser+': ')
        os.system('mysql -u root -p%s -e "CREATE DATABASE %s;"' %(sqlroot, newdb))
        os.system('mysql -u root -p%s -e "GRANT ALL PRIVILEGES ON %s.* TO %s@localhost IDENTIFIED BY \'%s\';"' %(sqlroot, newdb,newdbuser, newdbpass))
        os.system('mysql -u root -p%s -e "FLUSH PRIVILEGES;"' %(sqlroot))
        os.system('/bin/cp -f `pwd`/php.ini /etc/')
        os.system('/bin/cp -f `pwd`/nginx.conf /etc/nginx/')

        dbreps = {'saytdb':newdb, 'saytuser':newdbuser, 'freebsd':newdbpass}
        with open('/var/www/'+arg1+'/public_html/index.php', 'w') as outfile:
            with open(os.getcwd()+'/tempindex.php', 'r') as infile:
                for line in infile:
                    for src, target in dbreps.iteritems():
                        line = line.replace(src, target)
                    outfile.write(line)

        rplace = {'ngphp.lan':arg1}
        with open('/etc/nginx/conf.d/'+arg1+'.conf', 'w') as outfile:
            with open(os.getcwd()+'/ngphp.conf', 'r') as infile:
                for line in infile:
                    for src, target in rplace.iteritems():
                        line = line.replace(src, target)
                    outfile.write(line)

        os.system('rm -rf /var/www/'+arg1+'/public_html/index.html')
        os.system('/bin/cp -f `pwd`/www.conf /etc/php-fpm.d/')
        os.system('/etc/init.d/php-fpm start')
        os.system('/etc/init.d/nginx restart')
        print('\nNginx web server is installed and working\n\n')
    else:
		print('Thank you for use this script...')
		sys.exit()

while True:
    print('Select menu: ')
    print('1. For install LAMP and configure virtual host write 1 and click to Enter button.')
    print('2. For install Nginx, PHP-FPM, MySQL and configure virtual host write 2 and click to Enter button.')
    print('3. For exit from script write 3 and click to Enter button.')
    ent = raw_input('Please write number: ')

    if len(ent) > 1 and (ent != 1 or ent !=2 or ent != 3):
        print("\nYou can write only numbers 1, 2 and 3.")
        sys.exit()
    elif int(ent) == 1 or int(ent) == 2:
        pass

    if int(ent) == 1:
        ap()
    elif int(ent) == 2:
        ng()
    else:
        break
