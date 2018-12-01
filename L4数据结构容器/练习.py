# 学生管理系统--非函数版本
student_list = ['小王','小兰','小白']

while True:
    print("""
    欢迎使用学生列表
    1-查询学生信息
    2-添加学生信息
    3-修改学生信息
    4-删除学生信息
    0-退出程序
    """)

    num = int(input('请输入操作编号：'))

    # 查询
    if num == 1 :
        print('行号\t\t\t姓名')
        print('-'*50)
        for i in range(0,len(student_list)):
            print(i+1,'\t\t\t',student_list[i])

    # 添加
    elif num == 2:
        new_name = input('请输入新添加的姓名：')
        student_list.append(new_name)
        print('添加成功')

    # 修改
    elif num == 3:
        print('行号\t\t\t姓名')
        print('-'*50)
        for i in range(0,len(student_list)):
            print(i+1,'\t\t\t',student_list[1])
