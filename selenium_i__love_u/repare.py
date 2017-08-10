import square
f=open("dict.txt","r")
i=0

print("清空read_dict")
k=open("read_dict.txt","w")
k.truncate()
k.close()

print("把所有超过100本书的人读的书筛选出来,评分综合>0，并得到行数")
row_num=0
for eachline in f:
    if(eachline.count("=")>=100):
        sum=0
        first=eachline.split("//")[-1]
        for i in first.split("&&")[:-1]:
            num= i.split("=")[-1]
            sum=sum+float(num)
        if(sum!=0):
            k = open("read_dict.txt", "a")
            k.write(eachline)
            k.close()
            row_num=row_num+1
        else:
            print("sum=0")

print("得到不重复的书名,并的到列数")
f=open("read_dict.txt","r")
book_name=[]
LIST=[]
for eachline in f:
    eachline=eachline.split("\\")[-1]
    key_value = eachline.split("&&")[:-1]
    for i in key_value:
        LIST.append(i.split("=")[0])
        print("a")
for i in list(set(LIST)):
    book_name.append(i)
    print("b")
k=open("book_name.txt","w")
k.truncate()
k.close()
f = open("book_name.txt", "a")
for i in book_name:
    f.write(i+"\n")
    print("c")
f.close()

col_num=len(book_name)

#得到矩阵
book_star = [ [ 0 for i in range(col_num) ] for j in range(row_num) ]
print("将个人信息填写进矩阵")
k=open("read_dict.txt","r")
row_num=0
for eachline in k:
    eachline = eachline.split("\\")[-1]
    sum=0
    # noinspection PyInterpreter
    for i in eachline.split("&&")[:-1]:
        name=i.split("=")[0]
        col_num=book_name.index(name)
        book_star[row_num][col_num]=int(i.split("=")[-1])
        # sum=sum+float(i.split("=")[1])
    print("d")
    row_num=row_num+1

print("得到all_book")
r=square.all_book(book_star)

f=open("square.txt","w")
f.truncate()
f.close()
print("将all_book写入")
f = open("square.txt", "a")
for i in range(len(r)):
    for j in range(len(r)):
        f.write(str(r[i][j])+",")
    f.write("\n")
f.close()
