import urllib.request
import urllib.parse

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
data = {}
data['type'] = 'AUTO'
data['i'] = 'I love you!'
data['doctype'] = 'json'
data['xmlversion'] =