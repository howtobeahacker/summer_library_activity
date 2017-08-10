#这个代码是测试能否调用firfox浏览器进行网页抓取（这些网页的download按键，用phantomjd和chrome都无法点击，只有firfox可以，但是firfox的打开速度极其缓慢)
from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time
import re
# driver.add_cookie(cookie_dict={'bid': 'HZ9l3YBzjOI'})
# driver.get('https://book.douban.com/people/62561247/collect')  # 加载网页
driver=webdriver.PhantomJS()

# binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
# driver = webdriver.Firefox(firefox_binary=binary)
driver.get("https://www.douban.com")
driver.find_element_by_id("form_email").send_keys("17327764197")
driver.find_element_by_id("form_password").send_keys("sz869993410")
# data=driver.page_source
# img=re.findall('''<img id="captcha_image" src="(.*?)"''',data)
# print(img)
# yanzhengma=input("输入验证码：")
# driver.find_element_by_id("captcha_field").send_keys(yanzhengma)
driver.find_element_by_class_name("bn-submit").click()

# for i in list(num):
#     driver.find_element_by_id("form_email").send_keys(i)
#     time.sleep(1)
def open_douban(url):
    success=0
    url = str(url)
    driver.find_element_by_id("inp-query").send_keys(url)
    driver.find_element_by_class_name("inp-btn").click()
    # driver.find_element_by_("搜索").click()
    # driver.get("https://www.douban.com/people/62561247/")
    # driver.get('https://book.douban.com/people/62561247/collect')
    time.sleep(1)
    driver.refresh()
    data=driver.page_source
    # print(re.findall('''<a href="(.*?)" onclick="moreurl''',data))
    driver.get(re.findall('''<a href="(.*?)" onclick="moreurl''',data)[0])
    driver.get("https://book.douban.com/people/"+url+"/collect")
    data=driver.page_source
    num = re.findall(" .*读过的书[(](.*)[)] ", data)
    # print(num[0])
    if(int(num[0])>100 and int(num[0])<600):
        next_page = re.findall(
            '''<a href="https://book.douban.com/people/.*/collect[?]start=(.*)&amp;sort=time&amp;rating=all&amp;filter=all&amp;mode=grid''',
            driver.page_source)
        big = 0
        for i in next_page:

            i = int(i)
            if (i > big):
                big = i
        url_list = []
        for i in range(0, big + 1, 15):
            url_list.append("https://book.douban.com/people/" + url + "/collect" + "?sort=rating&start=" + str(i) + "&mode=grid&tags_sort=count")
            # url_list.append("https://book.douban.com/people/"+url+"/collect"+"?start="+str(i)+"&sort=time&rating=all&filter=all&mode=grid")
        f = open("dict.txt", "a")
        f.write(url + "\\\\")
        f.close()
        for i in url_list:
            driver.get(i)
            data=driver.page_source
            book = re.findall('''<a href="https://book.douban.com/subject/.*/" title="(.*?)"''', data)
            star = re.findall('''rating(.*)-t''', data)

            if(len(book)==len(star)):
                for i in range(len(book)):
                    f=open("dict.txt","a")
                    f.write(book[i]+"="+star[i]+"&&")
                    f.close()
        f = open("dict.txt", "a")
        f.write("\n")
        f.close()
        success+=1
        print(str(success)+"="+url)
        driver.get("https://www.douban.com")
    else:
        driver.get("https://www.douban.com")
# open_douban(62561247)
#
#
id_list=[]
f=open("idd.txt","r")
for i in f:
    id_list.append(i[:-1])
for i in id_list:
    try:
        open_douban(i)
    except Exception:
        driver.get("https://www.douban.com")
        pass
    # print(type(i))



# driver.find_element_by_id('switcher_plogin').click()#点击下载按钮
# driver.find_element_by_class_name("modal-dialog-button-ok").click()#点击同意按钮
# time.sleep(2)
# data = driver.page_source  # 获取网页文本
# driver.save_screenshot('1.png')  # 截图保存
# print(data)
# driver.close()

# /warehouse/getbinary?subjectId=f43e4ee2f8f3e278b4250b90e6223188&subjectClass=entity&cache=1502071667956&fn=465f35e72eb7e.kmz&recordEvent=true&name=ks