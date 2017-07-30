import os
import requests
from bs4 import BeautifulSoup
import sys

# os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\getFreeProxy.py")
# print("---------------------------------getfreeproxy success--------------------------------")
# # analysize 分析代理有用的代理
# os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\analysize_proxy.py")
# print("---------------------------------analyszie proxy success--------------------------------")



url="http://www.douban.com"

proxy_list=[]
f = open(r"C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\useful.txt", 'r')
for eachline in f:
    proxy_list.append(eachline[:-1])
f.close()

proxy_num=0
proxy_lon = len(proxy_list)
id=[]
id_url=[]
lon_id_url=len(id_url)
new_url=[]
old_url=[]
success_time=0
while(True):
    try:
        if(requests.get(url,proxies=eval(proxy_list[proxy_num]),timeout=0.5)==200):
            success_time+=1
            print(success_time)
        else:
            proxy_list.remove(proxy_list[proxy_num])
            print("remove" + proxy_list[proxy_num])
            proxy_num = 0
    except Exception:
        os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\getFreeProxy.py")
        print("---------------------------------getfreeproxy success--------------------------------")
        # analysize 分析代理有用的代理
        os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\analysize_proxy.py")
        print("---------------------------------analyszie proxy success--------------------------------")
        f = open(r"C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\useful.txt", 'r')
        for eachline in f:
            proxy_list.append(eachline[:-1])
        f.close()
    # except Exception:
    #     try:
    #         proxy_list.remove(proxy_list[proxy_num])
    #         print("remove"+proxy_list[proxy_num])
    #         proxy_num=0
    #     except Exception:
    #         os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\getFreeProxy.py")
    #         print("---------------------------------getfreeproxy success--------------------------------")
    #         # analysize 分析代理有用的代理
    #         os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\analysize_proxy.py")
    #         print("---------------------------------analyszie proxy success--------------------------------")
    #         f = open(r"C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\useful.txt", 'r')
    #         for eachline in f:
    #             proxy_list.append(eachline[:-1])
    #         f.close()