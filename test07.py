import  requests


headers = {
     "Accept-Encoding":"gzip,deflate",
    "Accept-Language":"en-US,en;q=0.9,zh,q=0.7",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
proxies = {

        'https':'http://163.123.192.31:7890',
         #'http':'http://119.1.160.114:7890'

}
data = {
    'usernm':'syl9617016',
    'passwd':'syl123321',
    'authcode':'',
    'toUrl':'',
    'app':'accountr.aja_login'

}
r = requests.post('http://www.nowapi.com/index.php?ajax=1',headers=headers ,proxies=proxies,data=data)
print(r.text)