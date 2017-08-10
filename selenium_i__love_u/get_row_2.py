import square
f=open("dict.txt","r")
i=0

#清空read_dict
k=open("read_dict.txt","w")
k.truncate()
k.close()

#把所有超过100本书的人读的书筛选出来，并得到行数
row_num=0
for eachline in f:
    if(eachline.count("=")>=100):
        k = open("read_dict.txt", "a")
        k.write(eachline)
        k.close()
        row_num=row_num+1

#得到不重复的书名,并的到列数
# f=open("read_dict.txt","r")
# book_name=[]
# LIST=[]
# for eachline in f:
#     eachline=eachline.split("\\")[-1]
#     key_value = eachline.split("&&")[:-1]
#     for i in key_value:
#         LIST.append(i.split("=")[0])
# for i in list(set(LIST)):
#     book_name.append(i)
# k=open("book_name.txt","w")
# k.truncate()
# k.close()
# for i in book_name:
#     f=open("book_name.txt","a")
#     f.write(i+"\n")
#     f.close()
book_name=[]
f=open("book_name.txt","r")
for eachline in f:
    book_name.append(eachline[:-1])
col_num=len(book_name)

#得到矩阵
book_star = [ [ 0 for i in range(col_num) ] for j in range(row_num) ]

#将个人信息填写进矩阵
k=open("read_dict.txt","r")
row_num=0
for eachline in k:
    eachline = eachline.split("\\")[-1]
    for i in eachline.split("&&")[:-1]:
        name=i.split("=")[0]
        col_num=book_name.index(name)
        book_star[row_num][col_num]=int(i.split("=")[-1])
    row_num=row_num+1
print(book_star)
r=square.all_book(book_star)
big=0
book_name_input=input("请输入你喜欢的书名：")
row=book_name.index(book_name_input)
print(row)
print(r[row][row])
for i in r[row]:
    if(i>big):
        big=i
for i in range(len(r[0])):
    for j in range(len(r[0])):
        if(r[i][j]==1.0):
            print(str(i)+";"+str(j))
print(big)
print(book_name[r[row].index(big)])
print(r[38][0])
print(r[38][38])
# print(big)
