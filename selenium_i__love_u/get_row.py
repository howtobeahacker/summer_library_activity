#将矩阵读入
f=open("square.txt","r")
num=0

for eachline in f:
    num=num+1
square=[ [ 0 for i in range(num) ] for j in range(num) ]
num=0
f=open("square.txt","r")
for eachline in f:
    square[num]=eachline.split(",")[:-1]
    num=num+1

# for eachline in square:
#     for eachlines in eachline:
#         eachlines=float(eachlines)
for i in range(len(square)):
    for j in range(len(square[i])):
        square[i][j]=float(square[i][j])

book_name=[]
f=open("book_name.txt","r")
for eachline in f:
    book_name.append(eachline[:-1])
book_name_input=input("请输入你喜欢的书名：")
row=book_name.index(book_name_input)
big_list=[]

square[row].sort()
big_list=square[row][-20:]
book_id=[]
for i in list(set(big_list)):
    num=0
    for j in square[row]:
        if(j==i):
            # print(num)
            book_id.append(num)
        num+=1

for i in book_id:
    print(book_name[i])