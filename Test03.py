import urllib.request

from bs4 import BeautifulSoup
import pymysql

h = {"user-agent":"Mozilla/5.0(windows NT 10.0;win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
req = urllib.request.Request("https://movie.douban.com/top250",headers=h)
r = urllib.request.urlopen(req)

#print(r.read().decode())

soup = BeautifulSoup(r.read().decode(),'html.parser')

#item = soup.find_all("div",attrs={"class":"item"})

items = soup.find_all("div",class_="item")
#print(items)

for item in items:
    pic_div = item.find("div",class_="pic")
    img=pic_div.a.img
    print(img['alt'])
    print(img['src'])
