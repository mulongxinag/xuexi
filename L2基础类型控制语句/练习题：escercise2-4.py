
# total=0                       #4
# for i in range(1,101):
#     total=total+i
# print(total)

# total=1                       #5
# for n in range(1,11):
#     total=total*n
# print(total)


# for n in range(1,5):          #1
#     print('****')


# a=1
# while a<=10:
#     b=1
#     while b<=a:
#         print('*',end='')
#         b+=1
#     print('\n')
#     a+=1


#
# for i in range(100,999+1):  #9
#     b3=i//100
#     b2=(i-b3*100)//10
#     b1=(i-b3*100-b2*10)//1
#     if b3**3+b2**3+b1**3== i:
#         print(i)
#

# for i in range(1,10):      #3
#     for n in range(1,10):
#         n=n+i
#         print('%s',%n, end='')
#   print()

# for x in range(1,10):      #9
#     for y in range(0,10):
#         for z in range(0,10):
#             num==x*100+y*10+z
#             if x**3+y**3+z**3==num
#             print(num)
#
# total=0                     #8
# for i in range(10000,100000):
#     b5=i//10000
#     b4=(i-b5*10000)//1000
#     b3=(i-b5*10000-b4*1000)//100
#     b2=(i-b5*10000-b4*1000-b3*1000)//10
#     b1=(i-b5*10000-
#     b4*1000-b3*100-b2*10)
#     if b5==b1 and b4 ==b2:
#         total+=1
#         print(i)
# print(total)

# for x in range(1,10):        #3
#     for y in range(1,x+1):
#         print(y,end='')
#     print()
#
# for x in range(1,11):        #2
#     for y in range(1,x+1):
#         print('*',end='')
#     print()
# #
# total=0                      #6
# for num in range(1,1000,2):
#     total=total+num
# print(total)


#7
#提示，例如数字15，分别去除以1.2、3、5、15，%
# num =14    #带判断的数
# total=0  #可以被整除的次数
#
# if num==1:
#     print('1既不是质数也不是合数')
# for i in range(1.15):
#     if num %i ==0:
#         total=total+1
# if total ==2:
#     print(num, '质数')
# #能被1、自身、和其它数整除
# elif total>2:
#     print(num,'合数')