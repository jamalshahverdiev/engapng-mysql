#!/bin/sh

if [ ! -f /usr/local/bin/bash ]
    then
        pkg install -y bash bash-completion vim
        echo "fdesc  /dev/fd  fdescfs  rw  0   0" >> /etc/fstab
        mount -t fdescfs fdesc /dev/fd
        cp -R `pwd`/freebsd-bash/.* /root/
        chsh -s /usr/local/bin/bash root
        cp /usr/local/bin/bash /bin/bash
        echo "bash bash-completion and vim already installed"
    elif [ -f /usr/local/bin/bash ]
    then
        cp -R `pwd`/freebsd-bash/.* /root/
        chsh -s /usr/local/bin/bash root
        cp /usr/local/bin/bash /bin/bash
        echo "USER Shell is changed"
fi
