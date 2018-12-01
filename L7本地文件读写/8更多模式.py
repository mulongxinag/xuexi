# open（）更多模式

"""
open（）第二个参数mode模式：
'r',read  读取信息
'w',write  写信息
'rb',read byte  读取字节信息
'wb'write byte  写字节信息
"""

with open('8write.txt','w',encoding='utf8') as f:
    f.write('hi')
    f.write('!  你好！')
    f.write('没有什么')
    f.write('能够阻挡')

with open('8write.txt','w',encoding='utf8') as f:
    f.write('第二次写信息')

"""
w 写模式，每一次打开文件写信息，会将之前的信息覆盖掉。
"""

with open('8write.txt','a',encoding='utf8') as f:
    f.write('\n a模式会追加信息到文件末尾')

"""
a模式：append  打开文件并将追加写入信息。
（了解）r+ 打开文件用于读写。
（了解）ab 追加写二进制信息。
"""