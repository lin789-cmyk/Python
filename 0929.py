import  requests
from bs4 import BeautifulSoup
import ddddocr
headers = {
     "Accept-Encoding":"gzip,deflate",
    "Accept-Language":"en-US,en;q=0.9,zh,q=0.7",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
proxies = {

        'https':'http://127.0.0.1:7890',
         #'http':'http://119.1.160.114:7890'

}
#请求登录界面
s = requests.Session()
login = s.get('http://www.nowapi.com/?app=account.login',headers=headers ,proxies=proxies)
#print(login.text)
#解析页面验证码
soup = BeautifulSoup(login.text,'html.parser')
image_url = soup.find_all(id='authCodeImg')[0]['src']
#把验证码存储为图片

rep_code = s.get(str(image_url),headers=headers,proxies=proxies)
image_code = rep_code.content
with open('lin.jpg','wb') as f:
    f.write(image_code)
#破解验证码
ocr = ddddocr.DdddOcr()
image = open('lin.jpg','rb').read()
result = ocr.classification(image)
print(result)
#通过验证码进行登录
data = {
    'usernm':'syl9617016',
    'passwd':'syl123321',
    'authcode':result,
    'toUrl':'',
    'app':'accountr.aja_login'

}

r = s.post('http://www.nowapi.com/index.php?ajax=1',headers=headers ,proxies=proxies,data=data)
print(r.text)