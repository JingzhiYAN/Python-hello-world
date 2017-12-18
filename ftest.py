# code by sunkun 20170417
# -*- coding: UTF-8 -*-
import urllib
import urllib.request
import re
import csv
import codecs
import sys


a = open('categorylist.txt','r')
while True:
    line = a.readline()
    if not line:
        break
    urlstart="http://www.costway.com/catalogsearch/result/?q="
    url=urlstart+line
    
    proxy_support = urllib.request.ProxyHandler({'http':'104.219.136.138'})
    opener = urllib.request.build_opener(proxy_support)
    response = urllib.request.urlopen(url)
    html = response.read()
    c= b"Your search returns no results."

    if c in html:
        f=open("record.txt","a")
        f.write('true')
        f.write('\n')
        f.close()
    else:
        f=open("record.txt","a")
        f.write('false')
        f.write('\n')
        f.close()
