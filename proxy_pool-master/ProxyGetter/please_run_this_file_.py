import os
import re
import requests
import random
import time

def cookies():
    f = open("D:\python_codes\douban_collection\cookies.txt", 'r')
    for i in f:
        COOKIES = eval(i)
    return COOKIES


# 设置cookies
def proxy():
    proxy_list = []
    f = open(r"C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\useful.txt", 'r')
    for eachline in f:
        proxy_list.append(eachline[:-1])
    f.close()
    return proxy_list


# 得到代理列表
def proxy_ip():
    proxy_list = proxy()
    proxy_num = len(proxy())
    num = random.randrange(1, proxy_num)
    return proxy_list[num]


# 得到随机代理
def open_url(url, proxies, cookies):
    HEADER = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              }
    r = requests.get(url, headers=HEADER, proxies=eval(proxies), cookies=cookies,timeout=3)
    return r


# 打开url，代理随机






def people_all_url(url):
    r = open_url(url,proxies=proxy_ip(),cookies=cookies())
    next_page = re.findall(
        '''<a href="https://book.douban.com/people/.*/collect[?]start=(.*)&amp;sort=time&amp;rating=all&amp;filter=all&amp;mode=grid''',
        r.text)
    big = 0
    for i in next_page:

        i = int(i)
        if (i > big):
            big = i
    url_list = []
    for i in range(0, big + 1, 15):
        url_list.append(url+"?sort=rating&start=" + str(
            i) + "&mode=grid&tags_sort=count")
    return url_list
    # print(next_page)
    # print(next_page)


# 得到这个人度过书的所有url
def people_ip():
    list = []
    f = open("D:\python_codes\douban_collection\id.txt", 'r')
    for eachline in f:
        eachline = eachline.replace("www", "book")
        list.append(eachline[:-1] + "collect")
    f.close()
    return list


# 得到用户的id
def read_books(url):
    r = open_url(url, proxy_ip(), cookies())
    num = re.findall(" .*读过的书[(](.*)[)] ", r.text)
    return int(num[0])
# 这个人看过多少书

def get_people_dict(url):
    list=[]
    r = open_url(url, proxy_ip(), cookies())
    book = re.findall('''<a href="https://book.douban.com/subject/.*/" title="(.*)"''', r.text)
    star = re.findall('''rating(.*)-t''', r.text)
    if(len(book)>=len(star)):
        for i in range(len(star)):
            list.append(str(book[i])+"="+str(star[i]))
    if (len(book) < len(star)):
        for i in range(len(book)):
            list.append(str(book[i]) + "=" + str(star[i]))


    return list

def get_book(url):
    r = open_url(url, proxy_ip(), cookies())
    book = re.findall('''<a href="https://book.douban.com/subject/.*/" title="(.*)"''', r.text)
    return  book

if __name__ == "__main__":

 for i in people_ip():
     f = open("D:\python_codes\douban_collection\\book_dict.txt", "a")
     f.write("\n")
     f.close()
     try:
        for i in people_all_url(i):
            print(i)
            try:
                for i in get_people_dict(i):
                    print(i)
                    f = open("D:\python_codes\douban_collection\\book_dict.txt", "a")
                    f.write(i + ",")
                    f.close()
                    time.sleep(1)

            except Exception:
                pass
     except Exception:
         pass
