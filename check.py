#!/usr/bin/env python2
import urllib2
from socket import setdefaulttimeout
from colorama import Fore
filename = raw_input("Type the file name[]: ")
setdefaulttimeout(100)
file = open(filename)
proxies = list(file)
def bad(prox):
    try:
        handler = urllib2.ProxyHandler({'http': prox})
        open = urllib2.build_opener(handler)
        open.addheader = [('User-Agent', 'Mozilla/5.0')]
        urllib2.install_opener(open)
        reqo = urllib2.Request("http://catsblog.tk")
        sock = urllib2.urlopen(reqo)
    except urllib2.HTTPError, e:
        print Fore.RED + "ERROR_CODE: ", e.code
        return e.code
    except Exception, detail:
        print Fore.RED + "ERROR: ", detail
        return 1
    return 0

for item in proxies[:-1]:
    if bad(item):
        print Fore.RED + "Bad ", item
    else:
        print Fore.GREEN + item, " is working..."
        f = open('good.txt', 'a')
        f.write(item)
        
