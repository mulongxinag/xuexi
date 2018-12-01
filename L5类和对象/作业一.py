class People():
    def __init__(self,name,race,state,height,weight):
        self.name=name
        self.race=race
        self.state=state
        self.height=height
        self.weight=weight

    def print_name(self):
        pass

    def print_race(self):
        pass

    def print_info(self):
        print('我叫{},我来自{},身高{}，体重{}'.format(self.name,self.origin,self.height,self.weight))

xiaoming=People('小明','黄种人','中国',180,70)
alice=People('Alice','白种人','美国',160,50)

xiaoming.print_info()
alice.print_info()




