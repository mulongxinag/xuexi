#a 表示前第二个数
#b 表示前第一个数
#c 表示前两个数的和
print('1、','1、',end='')
a=1
b=1

for i in range(3,10):
    c=a+b
    print(c,'、',end='')
    a=b
    b=c