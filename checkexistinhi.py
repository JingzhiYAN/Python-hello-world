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


a = open('notexisted.txt','r')
while True:
    line = a.readline()
    if not line:
        break
    if line is None:
        f = open("doublecheck.txt","a")
        f.write('\n')
        print('\n')
        f.close()
        break
    urlstart="https://www.hicollie.com/search?q="
    url = urlstart+line
    
    response = urllib.request.urlopen(url)
    html = response.read()
    c = b"did not yield any results."

    if c in html:
        print('dis')
        time.sleep(0.5)
    else:
        f = open("doublecheck.txt","a")
        f.write(line)
        f.write('\n')
        f.close()
        time.sleep(0.5)
