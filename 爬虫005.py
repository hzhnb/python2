import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}
response = requests.get("http://www.baidu.com",headers=headers)
print(response.content.decode())
