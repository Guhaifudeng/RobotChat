# -*- coding:utf8 -*-
import urllib2
import urllib

url_get_base = "http://api.ltp-cloud.com/analysis/"
args = {
    'api_key' : 'z1h0y653m69m3MbUmBltZxgAWAtOHv5X0jGJ8EOR',
    'text' : '我是中国人。',
    'pattern' : 'dp',
    'format' : 'plain'
}
data = urllib.urlencode(args)# 编码工作
req = urllib2.Request(url_get_base, data)# 发送请求同时传data表单
response = urllib2.urlopen(req) #接受反馈的信息
content = response.read()#读取反馈的内容
print content

#step1 wrong pydev可以运行 sumlimeText配置的编译环境无法运行-中文编码问题 cmd 运行可以，但乱码
