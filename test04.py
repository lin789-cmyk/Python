import urllib.request
h = {
    "Accept-Encoding":"gzip,deflate",
    "Accept-Language":"en-US,en;q=0.9,zh,q=0.7",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
}
req = urllib.request.Request("http://httpbin.org/get",headers=h)
proxies = {"http":"119.1.160.114:7890"}
proxy_handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(proxy_handler)
r = opener.open(req)
print(r.read().decode())