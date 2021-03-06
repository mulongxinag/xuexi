# 多态
class Animal(object):
    # def __init__(self, name):
    #     self.name = name

    def run(self):
        print('动物在跑')

class Cat(Animal):
    def run(self):
        print('猫在跑')

class Dog(Animal):
    def run(self):
        print('狗在跑')

class Pig(Animal):
    pass
class Bird(Animal):
    pass
class Monkey(Animal):
    pass

# 1 > 不同的类实例化，实例再调用自己的方法
# cat1 = Cat()
# dog1 = Dog()
# cat1.run()
# dog1.run()

# 2> 把上面的语句封装成函数
def animal_run(class_instance):     # 参数接收的是一个类实例
    class_instance.run()        # 传入cat执行cat.run() ,传入dog执行dog.run()

cat1 = Cat()
dog1 = Dog()
animal_run(cat1)
animal_run(dog1)


"""
多态：一段已写好业务逻辑代码，传入的实例不同，最终运行出的代码也跟着变化。一种程序可以有多种运行时状态，所以叫多态。
多态是类的三大特性之一。
好处：代码灵活。
"""
