def get_list():
    list = []
    f = open(r"C:\Users\lenovo\Desktop\proxy_pool-master\ProxyGetter\useful.txt", 'r')
    for eachline in f:
        list.append(eachline[:-1])
    f.close()
    return list
