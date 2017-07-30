
import os
while(True):
    #getproxy得到代理池
    os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\getFreeProxy.py")
    print("---------------------------------getfreeproxy success--------------------------------")
    #analysize 分析代理有用的代理
    os.system(r"python C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\analysize_proxy.py")
    print("---------------------------------analyszie proxy success--------------------------------")

    #看看单个代理是否有用
    # os.system(r"python D:\python_codes\douban\requests_headers_proxies.py")

