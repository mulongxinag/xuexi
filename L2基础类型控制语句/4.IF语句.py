# 主题：控制语句之if

# age = 20
# if age > 18:
#     print('年龄大于18是成人')
# else:
#     print('未成年')


score = 90
score = int(score)
if score < 60:
    print('不及格')
elif 60 < score < 70:
    print('及格')
elif 70 <= score and score < 90:
    print('良')
elif score>=90:
    print('优秀')
elif score<0 or score>100:
    print('分数不合法')

"""
如果...,那么...
if<条件>：  条件为true或（非空字符串，非空列表，非0）后执行代码块中的语句，false或（空字符串，空列表，0）的时候不执行。
if <条件1>:
    条件1为true执行语句
else:
   不满足上面条件的时候执行的语句
更多的选择分支
if<条件1>:
elif<条件2>:
elif<条件3>:
从上到下判断各个条件，如果走入一个分支，其他分支不会再走
设计项目注意条件怎么去设计
注意控制语句的嵌套层数不要超过四层。

pass：不执行实际功能，只是为了占位置
"""
"""
 表达式：一句代码。
语句块：后面的代码是从属于前面的一个语句，愈发特点：一条语句，然后有一个冒号，然后语句块以缩进（4个空格或一个tab）开始，语句块具有明显的层级关系。其他语言靠{}和：来区分语句块。

缩进：Python要求语句块强制缩进。必须为4个空格。tab和shift+tab调整代码缩进，、。
缩进错误会报错‘IndentatonError:unexpected indent’
"""

# (语法糖）if语句单行写法。（要求了解能看懂，不必可以使用）
# def get_max1(num1,num2):
#     # if num1>num2:
#     #     return num1
#     # else:
#     #     return num2
#     return num1 if num1>num2 else num2
# print(get_max1(1,2))
# print(get_max1(2,1))
# 类似三元表达式c=a>b?1:0
# if else语句