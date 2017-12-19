import urllib.request
import re
import time

#Get IP
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Hosts': 'www.xicidaili.com',
    'Referer': 'http://www.xicidaili.com/nn',
    'Connection': 'keep-alive'
}
#Get page range, 1 to 100 pages.
for i in range(1,100):
    url = 'http://www.xicidaili.com/nn/' + str(i)
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req).read().decode('utf-8')
#Get IP and portal
    ip_list = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6})", res, re.S)
#Save the ips and portals to file
    f = open("ip.txt","a+")
    for li in ip_list:
        ip = li[0] + ':' + li[1] + '\n'
        print(ip)
        f.write(ip)


        time.sleep(2)
f.close()