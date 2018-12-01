# （了解）global
## (老写法 total是全局变量)从1 加100
# total=0
# for i in range(1,101):
#     total=total+i
# print(total)

## global 显示声明变量为全局变量
total = 0
def add1():
    global total
    total = total + 1

add1()
add1()
add1()
print(total)


## (了解)nonlocal
# def outer():
#     num = 10
#     def inner():
#         nonlocal num
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()
