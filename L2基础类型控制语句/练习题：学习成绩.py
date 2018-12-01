# 接收用户输入的学生成绩
score=input('成绩：')
score=int (score)
if score< 60:
    passed='不及格'
    print(passed)
else:
    passed='及格'
    print(passed)
    if 60<=score<70:
        rank='D'

    elif 70<=score<80:
        rank='C'

    elif 80<=score<90:
        rank='B'

    elif 90<=score<=100:
        rank='A'
    print(rank)


    # score=input('成绩：')
    # score=int(score)
    #print(score,type(score))

    #判断成绩

    # if score<0 or score>100:
    #      print('用户输入不合法')
    # if  0<=score<60:
    #     print('不及格')
    # else:
#  #       print('及格')
    #     if 60<=score<70:
    #         print('D')
    #
    #     elif 70<=score<80:
    #         print('C')
    #     elif 80<=score<90:
    #         print('B')
    #     elif 90<=score<=100:
    #         print('A')
    #
