#while 循环
#if true：
#   print('hello')
#while true:
#    print('hello')

#while<条件>:
#   如果条件为true，那么重要运行while语句块中的内容。
#如果while循环的条件一直为true，死循环。


#
# #while后的条件变化着
# num=0
# while num<10:
#     print(num)
#     num=num+1
#     #num+=1 # 简写语法

while True:
    number=10
    num=int(input('请输入一个数字：'))

    if num<number:
        print('猜小了')
    elif num>number:
        print('猜大了')
    else:
        print('猜对了')