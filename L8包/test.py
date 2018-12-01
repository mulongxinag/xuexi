import os

os.chdir('C:\\Users\\Administrator\\Pictures')
filelist = os.listdir('C:\\Users\\Administrator\\Pictures')
print(filelist)
a = 1
for file in filelist:
    os.rename(file,'图片{}.{}'.format(a, file.split('.')[1]))
    a += 1


# import os
#
# os.chdir('')
# filelist = os.listdir('')











