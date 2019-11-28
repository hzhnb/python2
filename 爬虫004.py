import requests
#response.status_code:获取状态码
response = requests.get("http://www.baidu.com")
print(response.status_code)
#assert response.status_code==200
#response.headers:获取响应头信息
print(response.headers)
#获取请求url信息
print(response.request.url)
#获取响应url信息
print(response.url)
#获取请求头信息
print(response.request.headers)
