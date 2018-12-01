import sqlite3

def start_print():
    """初始界面"""
    print('-'*20, end='')
    print('欢迎使用学生管理系统', end='')
    print('-'*20)
    print('1-添加学生信息')
    print('2-修改学生信息')
    print('3-删除学生信息')
    print('4-查询学生信息')
    print('0-退出程序')


def create_db_table():
    """第一次执行创建数据库和表"""
    conn = sqlite3.connect('testsqlite.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE student
    (id INTEGER PRIMARY,
    name VARCHAR(20) NOT NULL,
    sex VARCHAR (10),
    age INTEGER );""")
    conn.commit()
    conn.close()


def add(cursor, connect):
    """添加新数据"""
    id1 = input('输入id')
    name1 = input('输入姓名')
    sex1 = input('输入性别')
    age1 = input('输入年龄')
    cursor.execute("""INSERT INTO student(id,name,sex,age) VALUES ('%s','%s','%s','%s');""" % (id1, name1, sex1, age1))
    connect.commit()
    cursor.close()
    print('学生信息添加成功')


def findall(cursor):
    """查询全部记录"""
    cursor.execute("SELECT * FROM student")
    data = cursor.fetchall()
    for x in range(len(data)):  # 循环下标访问
        print(f'id:{data[x][0]}\nname:{data[x][1]}\nsex:{data[x][2]}\nage:{data[x][3]}')
        print('-'*50)
    # print(data)
    cursor.close()


def findid(cursor):
    """以ID查询某条记录"""
    x = input("输入你要查询的id:")
    cursor.execute("SELECT * FROM student WHERE id = '%s'" % x)
    data = cursor.fetchone()
    print(f'id:{data[0]}\nname:{data[1]}\nsex:{data[2]}\nage:{data[3]}')  # 使用下标访问值
    cursor.close()


def update(cursor, connect):
    """修改数据"""
    up_id = input("输入你要修改的id：")
    new_name = input('输入新名字：')
    new_sex = input('输入性别：')
    new_age = input('输入新年龄:')
    cursor.execute("""UPDATE student SET name ='{}',sex='{}',age='{}'WHERE id = '{}'
""".format(new_name, new_sex, new_age, up_id))
    connect.commit()
    cursor.close()
    print('学生信息修改成功')


def delete(cursor, connect):
    """根据ID删除学生"""
    use_id = input('输入要删除的id：')
    cursor.execute("DELETE FROM student WHERE id = '{}'".format(use_id))
    print('删除成功')
    connect.commit()
    cursor.close()


def twice():
    """第2+次执行进入学生管理系统"""
    connect = sqlite3.connect('testsqlite.db')  # 连接数据库参数是数据库的名字。如果数据库在文件夹不存在会自动创建。
    start_print()
    while True:
        cursor = connect.cursor()
        print('请选择操作编号(1添加,2修改,3删除,4查询,0退出)')
        print('=' * 50)
        user_input = int(input())
        if user_input == 1:
            add(cursor, connect)
            print('='*50)
        elif user_input == 2:
            update(cursor, connect)
            print('=' * 50)
        elif user_input == 3:
            delete(cursor, connect)
            print('=' * 50)
        elif user_input == 4:
            print('1.查询某学生')
            print('2.查询全部学生')
            user_input1 = int(input('请输入操作编号：'))
            print('*' * 50)
            if user_input1 == 1:
                findid(cursor)
                print('=' * 50)
            elif user_input1 == 2:
                findall(cursor)
                print('=' * 50)
            else:
                print('请输入正确的操作编号')
                print('=' * 50)
                continue
        elif user_input == 0:
            connect.close()
            print('谢谢使用')
            print('=' * 50)
            break
        else:
            print('请输入正确的操作编号')
            print('=' * 50)
            continue
    return connect, cursor


if __name__ == '__main__':
    print('第1次执行请按1\n第2+次执行请按2')
    user_input3 = int(input('请输入1or2：'))
    if user_input3 == 1:
        create_db_table()
    elif user_input3 == 2:
        twice()
    else:
        print('输错了......')
