# from ip_proxies import get_proxy
import requests
# import requests_headers_proxies

list=[]
f=open("proxy.txt",'r')
for eachline in f:
    # print(eachline)
    if (eachline!="\n"):
        list.append(eachline[:-1])


f.close()

useful=[]

#
# proxy_http=get_proxy.proxy("http")
# proxy_https=get_proxy.proxy("https")
#
url="http://ip.chinaz.com/getip.aspx"
url2="http://desk.zol.com.cn/meinv/"
url3="https://www.pornhub.com/"
url4="https://www.douban.com"
proxys=[]

# for i in list:
#     http_dic = {"http":i.split("/n")[0]}
#     proxys.append(http_dic)
#
# for i in proxy_https:
#     https_dic = {"https": i.split("/n")[0]}
#     proxys.append(https_dic)

for i in list:
    http={"http":i}
    https={"https":i}
    proxys.append(http)
    proxys.append(https)

for proxy in proxys:
    # print(proxy)



    try:
        if(requests.get(url4,proxies=proxy,timeout=0.5).status_code==200):
            # print(proxy)
            useful.append(proxy)
            print(proxy)

    except Exception as e :
        pass
k=open("useful.txt","w")
k.truncate()

f=open("useful.txt",'w')
for eachline in useful:
    f.write(str(eachline)+"\n")
f.close()