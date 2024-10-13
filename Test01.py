import urllib.request

r = urllib.request.urlopen("https://www.sohu.com/")
"""print(r.status)
print(r.msg)"""
print(r.read().decode())
