#! /usr/bin/env python	

import dns.resolver
import subprocess
import datetime
import threading
import config as cfg
from time import sleep

def now():
    timestamp = str(datetime.datetime.now())
    return timestamp

def cleanIp(ip):
    ip = ip.split('#')[0]
    ip = ip.strip()
    
    return ip

def resolveNames():
    ips = []
    domains = []

    try:
        csfAllowDomains = open(cfg.files['allowDomains'], 'r')
        domains = [cleanIp(i) for i in csfAllowDomains.read().splitlines() if i.lstrip()[:1] != '#' and i.strip() != '']
    except IOError, e: 
        print e

    for domain in domains:
        aRecords = dns.resolver.query(domain,'A')
        for ip in aRecords:
            if ip not in ips:
                ips.append(ip.to_text())

    csfAllowDomains.close()

    return ips

def restartCsf():
    print 'Restarting CSF'
    try:
        subprocess.call(["csf", "-r"])
    except OSError as e:
        print e

def getCurrentIps():
    csfAllowFile = open(cfg.files['allowIps'], 'r+')
    csfAllow = csfAllowFile.read()
    ips = [cleanIp(i) for i in csfAllow.splitlines() if i.lstrip()[:1] != '#' and i.lstrip() != '']
    csfAllowFile.close()

    return ips

def appendIp(ip):
    print 'appended ' + ip
    csfAllowFile = open(cfg.files['allowIps'], 'a')
    csfAllowFile.write("\n" + ip + ' # CSF Allow Domains ' + now())
    csfAllowFile.close()

def isInCurrentIps(ip, currentIps):
    isIn = (ip in currentIps)
    return isIn

def updateSettings():
    wasCsfAllowChanged = False
    ips = resolveNames()
    currentIps = getCurrentIps()

    if len(ips) ==  0:
        return


    for ip in ips:
        if not isInCurrentIps(ip, currentIps):
            appendIp(ip)
            wasCsfAllowChanged = True
    
    if wasCsfAllowChanged:
        print 'csf Updated ' + now()
        restartCsf()

        
    threading.Timer(cfg.checkInterval, updateSettings).start()

if __name__ == '__main__':
    updateSettings()
