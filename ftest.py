# code by sunkun 20170417
# -*- coding: UTF-8 -*-
import urllib
import re
import csv
import codecs
file = open("categorylist.txt") # 需要查询的关键词按行放在文件里
resultFile = open('F:\categorylist_type.csv','wb')  # 输出的文件。 
# resultFile2 = open('C:\Users\sunkun\Desktop\pinpai2.csv','a+') 
resultFile.write(codecs.BOM_UTF8) # 防止中文乱码
fieldname = ['keywords', 'type'] # 返回文件，第一列放关键词，第二列放查询到的返回类型。
writer = csv.DictWriter(resultFile, fieldnames=fieldname)
# writer.writeheader() # 是否写上表头

while 1:
    line = file.readline()
    if not line:
        break
    # print line
    keyWords = (urllib).quote(line)     # url不支持中文，进行转码操作
    # keyWords = line.encode('utf-8')
    # line = '新闻软件'
    # url = 'http://quickshare.swc.sogou/quickshared?content=Clapton&class=null&part=0&platform=iOS&location=116.326022%7C39.992892&id=1481119148606063034&naming=raphael&framework=raphael'
    urlStart = 'http://www.costway.com/catalogsearch/result/?q='
    url = urlStart + keyWords
    try:
        request = urllib.Request(url)
        response = urllib.urlopen(request)
        content = response.read().decode('gbk')
        pattern = re.compile('<returntype>(.*?)</returntype>', re.S)
        resultType = re.findall(pattern, content)

        print 
