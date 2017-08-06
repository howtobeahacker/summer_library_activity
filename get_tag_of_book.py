import requests
import re
url="https://book.douban.com/tag/?view=type&icn=index-sorttags-all"
r=requests.get(url,proxies={'https': '120.25.154.32:8080'})
# print(r.text)
name=re.findall('''\<a name="(.*?)" class="tag-title-wrapper"\>''',r.text)
# print(name)
tag=re.findall('''\<a href="\/tag\/(.*?)"\>''',r.text)
URL="https://book.douban.com/tag/"
for i in tag:
    print(URL+str(i))