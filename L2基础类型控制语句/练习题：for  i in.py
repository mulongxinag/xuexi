
# while True:
#     n=input('请输入一些东西：')
#     a=0
#     b=0
#     c=0
#     d=0
#     for i in n:
#         if i.isalpha():
#             a+=1
#         elif i.isspace():
#             b+=1
#         elif i.isdigit():
#             c+=1
#         else:
#
#             d+=1
#     print('字母{}个，数字{}个，空格{}个，特殊字符{}'.format(a,b,c,d))
#


#1
alpha_num=0
digit_num=0
space_num=0
other_num=0
user_input=input('请随意输入一些东西：')

for i in user_input:
   if i.isalpha():
        alpha_num+=1
   elif i.isdigit():
        digit_num+=1
   elif i.isspace():
        space_num+=1
   else:
        other_num+=1
print('字母{}，数字{}，空格{}，其它{}'.format(alpha_num,digit_num,space_num,other_num))


