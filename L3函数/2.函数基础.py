#函数基础

#函数 function：将重复公共的代码抽象出来，多次调用。封装代码。函数把业务逻辑打包起来，我们使用时直接调用，不必关心内部是如何实现的，降低项目的实现难度。实现某一种功能。好处：减少重复代码节省代码量。模块逻辑清晰。
def calculate_area(r):#定义
    print('圆面积',3.14 * r * r)

calculate_area(151)#调用
calculate_area(3)
calculate_area(10)

# 语法
##函数定义：关键字def(define)  后跟函数名 后跟（参数） ：下面是  语句块
##参数：函数运行前需要告诉函数一些运行时需要的信息原料、数值，函数根据传入的参数，参与内部的逻辑运算。
##函数调用：函数名（参数）   同学错误一：
