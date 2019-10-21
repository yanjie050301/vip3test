# 导入import包
import requests,json
# 实例1：1.发get请求
# # 发送get请求
# urlste = 'https://blog.csdn.net/rainshine1190'
# # 发送请求
# r = requests.get(url = urlste)
# print(r.text)
# 实例2
# urlste = 'https://www.wanandroid.com/article/query'
# # 参数
# payload = {'k':'Android'}
# # 发送请求
# r = requests.get(url = urlste,params=payload)
# 获取结果
# print(r.text)  #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
# print(r.status_code) #响应状态码
# print(r.encoding)   # 编码格式
# print(r.content)   #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
# print(r.headers)  #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
# print(r.url)# 获取url
# print(r.cookies) # 获取response返回的cookie
# print(r.raw)  #返回原始响应体
# print(r.raise_for_status()) #失败请求(非200响应)抛出异常
# 实例3：发post请求（json）
# urlstr = 'http://httpbin.org/post'
# payload = {'qq群名':'selenium+jmeter+loadrunner','qq群号':'106014970'}
# # 方法一：
# # 通过json.dumps方法将python字符串转换成json类型
# # payload = json.dumps(payload)
# # r = requests.post(url = urlstr,data = payload)
# # 方法二：
# # 发送请求，接口请求为json数据，通过json=自动将python对象转变为json类型
# r = requests.post(url = urlstr,json = payload)
# print(r.text)
# print(r.json())
# 实例4：headers
# urlstr = 'https://www.wanandroid.com/user/login'
# payload = {'username':'chaoge','password':'123456'}
# r = requests.post(url = urlstr,data=payload)
# # 通过dict-key来访问对应的值
# a = r.json()['data']['admin']
# print(a)
# if a=='False':
#     print('你是管理员')
# else:
#     print('你不是管理员')
# print(type(r.text))
# 实例4：使用session登录
# urlstr = 'https://www.wanandroid.com/user/login'
# payload = {'username':'chaoge','password':'123456'}
# 初始化session对象
# s = requests.session()
# r = s.post(url = urlstr,data=payload)
# r2 = requests.get('https://www.wanandroid.com/1g/todo/list/0')
# print(r.text)
# print(r2.text)
# 实例5：携带cookie发送请求（4种方法）
# 方法一：通过r.cookies手动获取上一请求返回的cookie来设置下次请求的cookie
# urlstr = 'https://www.wanandroid.com/user/login'
# payload = {'username':'chaoge','password':'123456'}
# r = requests.post(url = urlstr,data=payload)
# # print(r.text)
# print(r.cookies)
# cookie = r.cookies
# r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies = cookie)
# print(r2.text,r2.status_code)
# 方法二：通过rquests.session自动设置cookie，来完成访问
# urlstr = 'https://www.wanandroid.com/user/login'
# payload = {'username':'chaoge','password':'123456'}
# s = requests.session()
# r = s.post(url=urlstr,data=payload)
# print(r.text)
# r2 = s.get('https://www.wanandroid.com/lg/todo/list/0')
# print(r2.text)
# 方法三：通过定制cookie，单独设置cookie来访问目标网址
# urlstr = 'https://www.wanandroid.com/user/login'
# payload = {'username':'chaoge','password':'123456'}
# r = requests.post(url = urlstr,data=payload)
# print(r.cookies)
# cookie ={'JSESSIONID' : r.cookies['JSESSIONID']}
# r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies = cookie)
# print(r2.text)
# 方法四：通过定制cookie，放入header来访问目标网址
urlstr = 'https://www.wanandroid.com/user/login'
payload = {'username':'chaoge','password':'123456'}
r = requests.post(url = urlstr,data=payload)
print(r.cookies)
header = {'cookie' : 'JSESSIONID='+r.cookies['JSESSIONID']}
r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',headers = header)
print(r2.text)
result = r2.text.find('已完成清单')
print(result)
if result != -1:
    print('查询成功')
else:
    print('查询失败')
















