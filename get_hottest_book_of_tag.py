import requests
import re
def get_url_of_hot_book(url):
    # print(requests.get(url,proxies={'https': '61.143.228.162:3128'}).status_code)
    html = requests.get(url,proxies={'https': '120.25.154.32:8080'}).text
    hot_book_name = re.findall('''\<a href="https:\/\/book.douban.com\/subject\/.*?\/" title="(.*?)" ''', html)
    hot_book_url = re.findall('''\<a href="https:\/\/book.douban.com\/subject\/(.*?)\/" title=".*?" ''', html)
    for i in range(len(hot_book_name)):
        print(hot_book_name[i]+"="+"https://book.douban.com/subject/"+hot_book_url[i]+"/")
        # print("https://book.douban.com/subject/"+hot_book_url[i]+"/")
f=open("C:\\Users\lenovo\Desktop\\tag_douban_book.txt","r")
for i in f:
    print("======================"+i.split("/")[-1].split("\n")[0]+"=======================")
    get_url_of_hot_book(i.split("\n")[0])
    # print(i.split("\n")[0])
# get_url_of_hot_book("https://book.douban.com/tag/港台")