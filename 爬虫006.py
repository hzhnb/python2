import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}
#parame = {"wd":"传智播客"}
#后面的那个问号可有可无
#url_temp = "https://www.baidu.com?"
#r = requests.get(url_temp,headers=headers,params=parame)
#print(r.status_code)
#print(r.request.url)
url = "https://www.baidu.com?wd={}".format("传智播客")
r = requests.get(url,headers=headers)
print(r.status_code)
print(r.request.url)