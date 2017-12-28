# code by Jingzhi Yan
# -*- coding: UTF-8 -*-
import urllib
import urllib.request
import re
import csv
import codecs
import sys
import time
import random


a = open('cate3.txt','r')
while True:
    line = a.readline()
    if not line:
        break
    if line is None:
        f=open("record3.txt","a")
        f.write('\n')
        print('\n')
        f.close()
        break
    urlstart="http://www.costway.com/catalogsearch/result/?q="
    url=urlstart+line
    
    response = urllib.request.urlopen(url)
    html = response.read()
    c= b"Your search returns no results."

    if c in html:
        f=open("record3.txt","a")
        f.write(line)
        f.write('\n')
        print('not exist')
        f.close()
        time.sleep(0.5)
    else:
        print('exist')
        print(line)