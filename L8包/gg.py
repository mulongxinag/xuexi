import os

print(os.getcwd())
os.chdir('C:\\EXE')
filelist = os.listdir()
a = 1
for file in filelist:
    print(file)
    os.rename(file,'文件{}.jpg'.format(a))
a += 1