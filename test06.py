import  requests


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

# your spider code


headers = {
     "Accept-Encoding":"gzip,deflate",
    "Accept-Language":"en-US,en;q=0.9,zh,q=0.7",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

data = {
    'username':'lin',
    'passwd':'123456'

}
def getHtml():
    retry_count = 5
    proxy = get_proxy().get("proxy")
    while retry_count > 0:
        try:
           r = requests.post('http://httpbin.org/post', headers=headers, proxies={"http": "http://{}".format(proxy)}, data=data)

           # 使用代理访问
           return r
        except Exception:
            retry_count -= 1
# 删除代理池中代理

    delete_proxy(proxy)
r=getHtml()
print(r.text)