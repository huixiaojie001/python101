'''
最简单的函数式编程实现学生管理系统的基本功能

****************************
欢迎使用【学生管理系统】V1.0
    1.显示所有学生信息
    2.新建学生信息
    3.查询学生信息
    4.修改学生信息
    5.删除学生信息
    0.退出系统
****************************
'''
#所有的学生数据，用一个列表模拟学生数据库
data =[
    {
        'id':17209001,
        'name':'赵',
        'sex':'男',
        'address':'赵国'
    },
    {
        'id':17209002,
        'name':'韩',
        'sex':'女',
        'address':'韩国'
    },
    {
        'id': 17209003,
        'name': '楚',
        'sex': '男',
        'address': '楚国'
    },
    {
        'id': 17209004,
        'name': '燕',
        'sex': '女',
        'address': '燕国'
    },
    {
        'id': 17209005,
        'name': '魏',
        'sex': '男',
        'address': '魏国'
    },
    {
        'id': 17209006,
        'name': '齐',
        'sex': '女',
        'address': '齐国'
    },
    {
        'id': 17209007,
        'name': '秦',
        'sex': '男',
        'address': '秦国'
    }
]

#美化显示
def beauty_print(data_list):
    for index,student in enumerate(data_list):
        print(f'序号：{index+1}',end='\t')
        print(f'姓名：{student["name"]}',end='\t')
        print(f'性别：{student["sex"]}',end='\t')
        print(f'地址：{student["address"]}')


#1.显示所有学生信息
def show_all():
    beauty_print(data)


#输入名字
def input_name():
    while True:
        name=input('输入名字：').strip()# strip() 去掉字符串的空格
        if name:
            return name
        else:
            continue


#选择性别
def choose_sex():
    while True:
        print('1(男)|2(女)')
        n=input('选择性别：')
        if n==1:
            return '男'
        elif n==2:
            return '女'
        else:
            continue


#2.新建学生信息
def creat_student():
    name=input_name()
    sex=choose_sex()
    address=input('输入地址：')
    student={
        'name':name,
        'sex':sex,
        'address':address
    }
    print('添加成功')
    data.append(student)#添加到列表，表名.append()
    show_all()


#3.查询学生信息
def find_student():
    name=input('输入查询学生的姓名：')
    for student in data:
        if student['name']==name:
            print(student)
            return
    else:
           print('查无此人')


#4.修改学生信息
def modify_student():
    name=input('输入你要修改学生的姓名：')
    for student in data:
        if student['name']==name:
            print(student)
            student['name'] = input('输入新的名字：')
            student['sex'] = input('输入新的性别：')
            student['address'] = input('输入新的地址：')
            print('修改成功')
            show_all()
            return
    else:
        print('查无此人')


#5.删除学生信息
def remove_student():
    name = input('输入你要删除学生的姓名：')
    for student in data:
        if student['name'] == name:
            data.remove(student)
            print('删除成功')
            show_all()
            return
    else:
        print('查无此人')


print("""
****************************
欢迎使用【学生管理系统】V1.0
    1.显示所有学生信息
    2.新建学生信息
    3.查询学生信息
    4.修改学生信息
    5.删除学生信息
    0.退出系统
****************************
    """)

while True:
    op=input('请输入序号：')
    if op=='1':
        show_all()
    elif op=='2':
        creat_student()
    elif op=='3':
        find_student()
    elif op=='4':
        modify_student()
    elif op=='5':
        remove_student()
    elif op=='0':
        print('已退出')
        break
    else:
        print('没有找到任何信息，请确定你输入的序号是否正确！')
