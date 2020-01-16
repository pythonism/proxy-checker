#!/usr/bin/env python3
from checker import checker
from colorama import Fore
from os import system as term
term('clear')
phile=input('Type the filename of text file with proxies within: [] ')
filer=open(phile)
filer=list(filer)
checker=checker()
for item in filer:
    if checker.check(item):
        print(Fore.RED+'Bad proxy',item)
    else:
        phile=open('good.txt','a')
        phile.write(item)
        print(Fore.GREEN+'Good proxy',item)
