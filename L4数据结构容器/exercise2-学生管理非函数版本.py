# 学生管理v1-非函数版本
student_list = ['小王', '小红', '小李']

while True:
    print("""
    欢迎使用学生管理系统
    1-查看学员姓名
    2-添加学员姓名
    3-修改学员姓名
    4-删除学员姓名
    0-退出程序
    """)

    num = int(input('请输入操作编号：'))

    if num == 1:
        # 打印列表
        # print(len(student_list))
        print('行号\t\t姓名')
        print('-------------------' )
        for i in range(0, len(student_list)):
            print(i+1, '\t\t', student_list[i])
    elif num == 2:
        # 添加
        new_name = input('请添加新姓名：')
        student_list.append(new_name)
        # student_list.append(input('请添加新姓名：'))
        print('添加成功')
    elif num == 3:
        # 修改
        print('行号\t\t姓名')
        print('-------------------')
        for i in range(0, len(student_list)):
            print(i+1, '\t\t', student_list[i])

        stu_num = int(input('修改第几个：'))
        student_list[stu_num-1] = input('修改后的名字:')
        print('修改成功')
    elif num == 4:
        # 删除
        print(""" 删除> 请输入子操作编号：
                  1）按学生编号删除
                  2）删除全部学生（谨慎） 
        """)
        sub_num = int(input('请选择子操作：'))
        if sub_num == 1:
            stu_num = int(input('要删除第几个学生？：'))
            student_list.pop(stu_num - 1)
            print('删除成功')
        elif sub_num == 2:
            confirm = input('确认删除全部？(Y/N)')
            if confirm == 'Y'or confirm == 'y':
                student_list.clear()
                print('删除全部成功')
    elif num == 0:
        print('谢谢使用')
        break

