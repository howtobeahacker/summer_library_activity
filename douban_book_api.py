import re
import requests
import random
import time
import os
def proxy():
    proxy_list = []
    f = open(r"C:\Users\lenovo\Desktop\proxy_pool-master\useful.txt", 'r')
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
url="https://api.douban.com/v2/book/"
lon=len(proxy())
print(lon)
num=0
false=0
i=1008760
# for i in range(1000400,20000000):
while(i<20000000):
    try:
        r=requests.get(url+str(i),proxies=eval(proxy()[num]),timeout=2)
        if(r.status_code==200):
            i = i + 1
            try:
                f = open("book_douban_8.txt", "a")
                f.write(r.text)
                f.write("\n")
                f.close()
                print(i)

            except Exception:
                pass
        # elif(r.status_code!=200):
        #     i=i+1
        #     print(r.status_code+"pass")
        else:
            i = i + 1
            print("pass")
            if(num<lon):
                print("=================="+str(num)+"====================")
                num = num + 1
            if(num==lon):
                os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\getFreeProxy.py")
                print("---------------------------------getfreeproxy success--------------------------------")
                # analysize 分析代理有用的代理
                os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\analysize_proxy.py")
                print("---------------------------------analyszie proxy success--------------------------------")
                num=0
                lon = len(proxy())
                time.sleep(10)
            while (lon == 0):
                os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\getFreeProxy.py")
                print("---------------------------------getfreeproxy success--------------------------------")
                # analysize 分析代理有用的代理
                os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\analysize_proxy.py")
                print("---------------------------------analyszie proxy success--------------------------------")
                num = 0
                lon = len(proxy())
                time.sleep(10)
    except Exception:
        false += 1
        if (false == 100):
            false=0
            num = num + 1
        if (num == lon):
            os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\getFreeProxy.py")
            print("---------------------------------getfreeproxy success--------------------------------")
            # analysize 分析代理有用的代理
            os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\analysize_proxy.py")
            print("---------------------------------analyszie proxy success--------------------------------")
            num = 0
            lon = len(proxy())
            time.sleep(10)
        while (lon == 0):
            os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\getFreeProxy.py")
            print("---------------------------------getfreeproxy success--------------------------------")
            # analysize 分析代理有用的代理
            os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\analysize_proxy.py")
            print("---------------------------------analyszie proxy success--------------------------------")
            num = 0
            lon = len(proxy())
            time.sleep(10)
        print("Exception")
        continue


#1061403