# -*- coding:utf8 -*-
import urllib.request
import socket
socket.setdefaulttimeout(3)

inf = open("ip.txt")    # 这里打开刚才存ip的文件
lines = inf.readlines()
proxys = []
for i in range(0,len(lines)):
    proxy_host = "http://" + lines[i]
    proxy_temp = {"http":proxy_host}
    proxys.append(proxy_temp)

# 用这个网页去验证，遇到不可用ip会抛异常
url = "http://ip.chinaz.com/getip.aspx"
# 将可用ip写入valid_ip.txt
ouf = open("valid_ip.txt", "a+")

for proxy in proxys:
    try:
        res = urllib.request.urlopen(url,proxies=proxy).read()
        valid_ip = proxy['http'][7:]
        print ('valid_ip: ' + valid_ip)
        ouf.write(valid_ip)
    except Exception as e:
        print (proxy)
        print (e)
        continue
ouf.close()