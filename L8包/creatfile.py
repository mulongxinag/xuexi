import os
print(os.getcwd())#获取当前路径
os.chdir('test')#切换到test文件夹下
#路径可以是绝对路径或者相对路径  绝对路径"D:\\tutorial\\L8包\\test"
#D:/tutorial/L8包
filelist = os.listdir()
print(filelist)
a = 0
b = ['a', 'b', 'c']
for file in filelist:
    os.rename(file, '{}.txt'.format(b[a]))
    a += 1

