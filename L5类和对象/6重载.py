# （了解）重载
# 面试题：重写跟重载的区别？
# 重写参考  L5/5类的继承2.py 一节

# 引题1：写几个关于比大小的函数。
# 1> 给定两个数，返回最大的那个数
# 2> 给定三个数，返回最大的那个数
# 3> 传入数字组成的列表[1, 0, -1, 3.5], 返回最大的那项数字
def get_max1(num1, num2):
    # if num2 > num1:
    #     return num2
    # else:
    #     return num1
    max = num1
    if num2 > max:
        max = num2
    return max

print(get_max1(1, 3))

def get_max2(num1, num2, num3):
    # if num2 > num1 and num2>num3:
    #     max=num2
    # if num3 > num2 and num3>num1:
    #     max=num3
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    return max_num

print(get_max2(6,3,5))



def get_max3(num_list):
    max = num_list[0]
    # for i in range(0,len(num_list)):
    #     if max < num_list[i]:
    #         max=num_list[i]
    for index, num in enumerate(num_list):
        print(index, num)
        if num > max:
            max = num
    return max


num_list=[1,2,3,-1]
print(get_max3(num_list))

# 2 把上面的三个函数封装到一个类中。
# 3 然后觉得get_max1 get_max2看着难受，所以都变成get_max，发觉报错，python由于自身特性没有重载机制。
class GetMaxNum(object):
    @staticmethod
    def get_max(num1, num2):
        max = num1
        if num2 > max:
            max = num2
        return max

    @staticmethod
    def get_max(num1, num2, num3):
        max_num = num1
        if num2 > max_num:
            max_num = num2
        if num3 > max_num:
            max_num = num3
        return max_num

    @staticmethod
    def get_max(*num_list):
        max = num_list[0]
        for index, num in enumerate(num_list):
            print(index, num)
            if num > max:
                max = num
        return max

# GetMaxNum.get_max(1,3)
# GetMaxNum.get_max(1,2, 3)
# GetMaxNum.get_max([1,2,3])    # 传参类型可变
# GetMaxNum.get_max(1)
# GetMaxNum.get_max(True)
GetMaxNum.get_max(*[1,2,3])     # 参数个数可变

"""
重写：子类重写父类中的同名方法。针对类继承情况。
重载：类中有多个同名方法。参数个数不同，或参数类型不同，这种情况较方法重载。针对方法参数的不同状况。

python当中没有重载机制，java语言中才有。同名函数重复定义，以最后的为准。因为python是动态类型语言，传实参什么类型都接收；形参和实参可以穿可变个数的参数。
"""

