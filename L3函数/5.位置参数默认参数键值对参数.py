#参数的几种类型

#位置参数。一个标识符做形参。位置参数普通和常用。
# def get_max(a,b,c):
#     max_num = a
#     if b > max_num:
#         max_num = b
#     if c > max_num:
#         max_num = c
#     return max_num
# get_max(1,5,3)
#
# #默认参数。带默认值的参数。
# for i in range(1,10):
#     print(i)


#
# def myrange():
#     i=0
#     while i<10:
#         print(i)
#         i+=1
# myrange()
#
#     i=start
#     while i<end:
#         print(i)
#         i+=step
# myrange(1,10,2)#(1,10,1)==(1,10)

#上例中的step=1 就是一个默认参数。函数调用时可以默认参数，那么这个参数的值就是默认值。如果实参传值的话，传的值会覆盖参数默认值。
#参数的顺序：默认参数 必须要在 位置参数之后。
#否则报错SyntaxError:non-default argument follows default argument

#默认值一般定义为你想要的默认信息，数字类型参数默认可以定位0，字符串参数默认值''，布尔默认值一般false。

#键值对参数（函数调用传实参时）
# def print_stu_info(name,sex='male',score=0):
#     print('姓名：{}，性别：{}，分数：{}'.format(name,sex,score))
#     print_stu_info('小明','male','90')
#     print_stu_info('小明',score='90',sex='male')
#当参数比较多，超过五个，十个的时候，用位置参数容易混淆出错。
#实参 键=值，这样就能准确给形参传值，所以位置顺序可以调换，但是要跟在位置参数后边。
def print_stu_info(name,sex='male',score=0):
    print('姓名：{}，性别：{}，分数：{}'.format(name,sex,score))
    print_stu_info('小明','male','90')
    print_stu_info('小明',score='90',sex='male')