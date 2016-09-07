#!/usr/bin/env bash

OSBSD=`uname -s`
FVER=`uname -r | cut -f1 -d'.'`

if [ "$OSBSD" == "FreeBSD" ] && [ "$FVER" = "10" ]
then
    kill -9 `ps waux| grep bind | grep -v grep | awk '{ print $2 }'`
    pkg delete -y bind910
    rm -rf named_*
    rm -rf zone_*
    rm -rf /usr/local/etc/namedb/
    rm -rf /usr/local/sbin/named/
    rm -rf /var/log/bind/
else [ -f /etc/issue ] && [ -f /etc/redhat-release ]
    kill -9 `ps waux|grep named | grep -v grep | awk '{ print $2 }'`
    yum -y remove bind.x86_64
    rm -rf /var/named
    rm -rf /etc/named*
    rm -rf /var/log/bind/
    rm -rf /usr/sbin/named
fi
