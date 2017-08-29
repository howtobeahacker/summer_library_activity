#coding="utf-8"
from selenium import webdriver
import re
import time
def signin():
    driver = webdriver.Firefox()
    driver.get("https://www.douban.com/")
    driver.find_element_by_id("form_email").send_keys("17327764197")
    driver.find_element_by_id("form_password").send_keys("sz869993410")
    w=input("输入验证码：")
    driver.find_element_by_class_name("bn-submit").click()
    driver.get("https://book.douban.com")
    return driver
def get_info(name):
    driver.find_element_by_id("inp-query").clear()
    driver.find_element_by_id("inp-query").send_keys(name)
    driver.find_element_by_class_name("inp-btn").click()
    url =re.findall('''<a href="(.*?)" title=''', re.findall('''div class="info"([\s\S]*)''', driver.page_source)[0][:200])[0]
    driver.get(url)
    try:
        tag = re.findall('''href="/tag/(.*?)"''', driver.page_source)[:2]
    except Exception:
        try:
            tag = re.findall('''href="/tag/(.*?)"''', driver.page_source)[:1]
        except Exception:
            tag="none"
    try:
        title=(re.findall('''<span property="v:itemreviewed">(.*?)</span>''',driver.page_source)[0])
    except Exception:
        title="none"

    try:
        author=(re.findall('''>([\s\S]*)</a>''',re.findall('''<span class="pl">作者:</span>([\s\S]*)<br>''',driver.page_source)[0][:200])[0])
        author=author.replace("\n","")
        author=author.replace(" ","")
    except Exception:
        try:
            author = (re.findall('''>([\s\S]*)</a>''',
                                 re.findall('''<span class="pl"> 作者</span>([\s\S]*)<br>''', driver.page_source)[0][:200])[0])
            author = author.replace("\n", "")
            author = author.replace(" ", "")
        except Exception:
            author="none"
    try:
        publisher=(re.findall("出版社:</span>(.*?)<br>",driver.page_source)[0])
    except Exception:
        publisher="none"

    try:
        pubdate = (re.findall("出版年:</span>(.*?)<br>", driver.page_source)[0])
    except Exception:
        pubdate="none"

    try:
        pages = (re.findall("页数:</span>(.*?)<br>", driver.page_source)[0])
    except Exception:
        pages ="none"

    try:
        price = (re.findall("定价:</span>(.*?)<br>", driver.page_source)[0])
    except Exception:
        price ="none"

    try:
        binding = (re.findall("装帧:</span>(.*?)<br>", driver.page_source)[0])
    except Exception:
        binding="none"

    try:
        series = (re.findall('''>(.*?)</a>''', re.findall("丛书:</span>(.*?)<br>", driver.page_source)[0])[0])
    except Exception:
        series="none"

    try:
        isbn = (re.findall("ISBN:</span>(.*?)<br>", driver.page_source)[0])
    except Exception:
        isbn    ="none"

    try:
        rating = (re.findall('''<strong class="ll rating_num " property="v:average">(.*?)</strong>''', driver.page_source)[0])
    except Exception:
        rating    ="none"

    try:
        images = (re.findall('''<img src="(.*?)" title="点击看大图" ''', driver.page_source)[0])
    except Exception:
        images="none"

    try:

        a = re.findall('''<div class="intro">([\s\S]*)</div>''',
                       re.findall('''<span class="">内容简介</span>([\s\S]*)<style>''', driver.page_source)[0])
        for i in a:
            if '''<a href="javascript:void(0)" class="j a_show_full">''' in a[0]:
                i = re.findall('''<div class="intro">([\s\S]*)''', a[0])[0]
                b = i.replace("<p>", "")
                c = b.replace("</p>", "")
                d = c.replace("</div>", "")
                summary = d.replace("\n", "")
            else:
                b = i.replace("<p>", "")
                c = b.replace("</p>", "")
                d = c.replace("</div>", "")
                summary = d.replace("\n","")
    except Exception:
        summary="none"

    try:
        a = (re.findall('''<div class="intro">([\s\S]*)''',
                        re.findall('''<span class="">作者简介</span>([\s\S]*)</p></div>''', driver.page_source)[0]))
        for i in a:
            if '''<a href="javascript:void(0)" class="j a_show_full">''' in a[0]:
                i = re.findall('''<div class="intro">([\s\S]*)''', a[0])[0]
                b = i.replace("<p>", "")
                c = b.replace("</p>", "")
                d = c.replace("</div>", "")
                author_intro=d.replace("\n","")
            else:
                b = i.replace("<p>", "")
                c = b.replace("</p>", "")
                d = c.replace("</div>", "")
                author_intro = d.replace("\n","")
    except Exception:
        author_intro="none"

    book_info={"title":title,"author":author," publisher":publisher,"pubdate":pubdate,"pages":pages,"tags":tag,"price":price,"binding":binding,"series":series,"isbn":isbn,"rating":rating,"img":images,"summary":summary,"author_intro":author_intro}
    book_info=str(book_info).encode("gbk",errors="ignore").decode("gbk",errors="ignore")
    # print(book_info)
    return book_info
    # f = open("book_info4.txt", "a")
    # f.write(book_info+"\n")
    # f.close()
if __name__=="__main__":

    L = []
    f=open("j.txt","r")
    for i in f:
        L.append(i[:-1])
    f.close()
    driver = webdriver.Firefox()
    # driver.get("https://www.douban.com/")
    # driver.find_element_by_id("form_email").send_keys("17327764197")
    # driver.find_element_by_id("form_password").send_keys("sz869993410")
    # w = input("输入验证码：")
    # driver.find_element_by_0class_name("bn-submit").click()
    driver.get("https://book.douban.com")


    # a=get_info("移居台湾的九大师")
    # print(a)
    # f=open("k.txt","a")
    # f.write(a+"\n")
    # f.close()


    #
    f=open("k.txt","a")
    num=0
    times=0
    for i in L:
        try:
            times+=1
            if(times==100):
                time.sleep(10)
                driver.refresh()
                times=0
            a=get_info(i)
            f.write(a+"\n",)
            print(i)
            num=0
        except Exception:
            num+=1
            print("false")
            k=open("false.txt","a")
            k.write(i+"\n")
            k.close()
            if(num==10):
                time.sleep(20)
                num=0
                # driver.refresh()
                driver.close()
                driver = webdriver.Firefox()
                # driver.get("https://www.douban.com/")
                # driver.find_element_by_id("form_email").send_keys("17327764197")
                # driver.find_element_by_id("form_password").send_keys("sz869993410")
                # w = input("输入验证码：")
                # # driver.find_element_by_class_name("bn-submit").click()
                driver.get("https://book.douban.com")
    f.close()