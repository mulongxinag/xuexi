# km=input('公里数(km)：')
# km=int(km)
# if 0<km<=2:
#     cost=print('8(元):')
#     print(cost)
# elif 2<km <=12:
#     cost=8+(km-2)*1.2
#     print(cost)
# elif km>12:
#     cost=8+1.2*(12-2)+(km-12)*1.5
#     print(cost)
#
#
# km=input('输入公里数：')
# km=int(km)
# pay=0
# if 0<=km<=2:
#     pay=8
# elif 2<km<=12:
#     pay=8+(km-2)*1.2
# elif km>12:
#     pay=8+10*1.2+(km-2)*1.5
#     print('输入不合法')
# #打印结果
# print('花费一共'+str(pay)+'元')

# a=int(input('输入第一个数:'))
# b =int(input('输入第二个数:'))
# c =int(input('输入第三个数：'))

def max_num(a,b,c):
    if a>=b>=c or a>=c>=b:
        print('第一个数大')
    elif b>=a>=c or b>=c>=a:
        print('第二个数大')
    elif a<=b<=c or c>=a>=b:
        print('第三个数大')
max_num(12,5,8)


a=int(input('输入第一个数:'))
b =int(input('输入第二个数:'))
c =int(input('输入第三个数：'))
max_num=a
if b>max_num:
    max_num=b
if c>max_num:
    max_num=c
print('最大值')
#理解：max_num就好像擂台一样，后面依次比较，谁更强谁就站上擂