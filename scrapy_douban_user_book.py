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
    r = open_url(url, proxy_ip(), cookies())
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
        url_list.append(url+"?start=" + str(
            i) + "&sort=time&rating=all&filter=all&mode=grid")

    return url_list
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
    r = open_url(url, proxy_ip(), cookies())
    book = re.findall('''<a href="https://book.douban.com/subject/.*/" title="(.*)"''', r.text)
    star = re.findall('''rating(.*)-t''', r.text)
    return (dict(zip(book, star)))

def get_book(url):
    r = open_url(url, proxy_ip(), cookies())
    book = re.findall('''<a href="https://book.douban.com/subject/.*/" title="(.*)"''', r.text)
    return  book

if __name__ == "__main__":
 # url="https://www.douban.com/people/subdued731/"
 # print(requests.get(url,proxies={'http': '60.178.130.134:8081'},cookies={'bid': 'HZ9l3YBzjOI', 'gr_user_id': '2fb4b974-4621-4312-8974-7f3f91c14148', 'll': '"118163"', '__yadk_uid': '683pyN8HnV47rWC9w0AnQwcKdSCYhwPo', 'viewed': '"4822685_6709783_10769749_5333562_1964774_1240002"', '_ga': 'GA1.2.1621314262.1475848003', 'ps': 'y', 'dbcl2': '"161770925:WZnZViiBkMM"', '_vwo_uuid_v2': '71B8DD1909CD3E87067C64A3E4AA6C34|714d1b4c8545775f1f0a16bc8d709cf2', 'ct': 'y', 'ap': '1', '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1500179055%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dl2ruuHTuSRm9v4RLNXlqAHOWJw_SY1Bjuz0aX14Fpka%26ck%3D6498.2.115.149.143.196.145.196%26shh%3Dwww.baidu.com%26wd%3D%26eqid%3Dea145fc90002af5c00000005596abe7a%22%5D', '__utmt': '1', 'ck': '4meA', 'push_noty_num': '0', 'push_doumail_num': '0', '__utma': '30149280.1621314262.1475848003.1500174450.1500179055.46', '__utmb': '30149280.32.10.1500179055', '__utmc': '30149280', '__utmz': '30149280.1500167800.44.32.utmcsr=baidu|utmccn=(organic)|utmcmd=organic', '__utmv': '30149280.16177', '_pk_id.100001.8cb4': '3b0351bc421fa413.1486187084.37.1500180710.1500174871.', '_pk_ses.100001.8cb4': '*'}).text)
 #
 for i in people_ip():
     try:
        for i in people_all_url(i):
            print(i)
            try:
                for i in get_book(i):
                    print(i)
                    f = open("D:\python_codes\douban_collection\\book.txt", "a")
                    f.write(i + "\n")
                    f.close()
                    time.sleep(2)
            except Exception:
                pass
     except Exception:
         pass