"""
****************************
欢迎使用【学生管理系统】V1.1
    1.显示所有学生信息
    2.新建学生信息
    3.查询学生信息
    4.修改学生信息
    5.删除学生信息
    0.退出系统
****************************
"""

from datetime import datetime

#模拟的学生数据
data =[
    {
        'name':'赵',
        'sex':'男',
        'address':'赵国',
        'birthday':'20011001'
    },
    {
        'name':'韩',
        'sex':'女',
        'address':'韩国',
        'birthday':'20021002'
    },
    {
        'name': '楚',
        'sex': '男',
        'address': '楚国',
        'birthday':'20031003'
    },
    {
        'name': '燕',
        'sex': '女',
        'address': '燕国',
        'birthday':'20041004'
    },
    {
        'name': '魏',
        'sex': '男',
        'address': '魏国',
        'birthday':'20051005'
    },
    {
        'name': '齐',
        'sex': '女',
        'address': '齐国',
        'birthday':'20061006'
    },
    {
        'name': '秦',
        'sex': '男',
        'address': '秦国',
        'birthday':'20071007'
    },
    {
        'name': '秦',
        'sex': '男',
        'address': '秦国',
        'birthday':'20081007'
    }
]

#学生类
class Student:
    #学生初始化
    def __init__(self,name,sex,address,birthday):
        self.name=name
        self.sex=sex
        self.address=address
        self.birthday=birthday

    #获取学生年龄
    def get_age(self):
        if self.birthday:
            age=datetime.now().year-int(self.birthday[:4])
            return age
        else:
            return '不知道'


#学生管理系统类
class System_student:
    #初始化
    def __init__(self,name):
        self.name=name
        self.data=[]


    #美化输出打印
    def beauty_printt(self,data_list):
        for index,student in enumerate(data_list):
            print(f'序号：{index+1}',end='\t')
            print(f'名字：{student.name:3}',end='\t')
            print(f'性别：{student.sex:3}', end='\t')
            print(f'地址：{student.address:3}', end='\t')
            print(f'年龄：{student.get_age()}')

     #加载数据
    def load_data(self):
        for item in data:
            student=Student(item['name'],item['sex'],item['address'],item['birthday'])
            self.data.append(student)

    #启动学生管理系统
    def start(self):
        #在系统启动时，第一步加载数据
        self.load_data()
        self.show_menu()
        while True:
            op=input('选择操作：')
            if op=='1':
                self.show_all_student()
            elif op=='2':
                self.create_student()
            elif op=='3':
                self.find_student()
            elif op=='4':
                self.modify_student()
            elif op=='5':
                self.remove_student()
            elif op == '0':
                print('已退出')
                break
            else:
                print('没有找到任何信息，请确定你输入的序号是否正确！')


    #选择性别
    def choose_sex(self):
        sex=input('选择性别（1，男|2，女）:').strip()
        if sex=='1':
            return '男'
        elif sex=='2':
            return '女'
        else:
            return '未知'

    #根据名字查找学生
    def find_student_by_name(self):
        name = self.input_name()
        find_list=[]
        for student in self.data:
            if name.lower() in student.name.lower():#字符串的一个方法lower，把大写转换成小写
                find_list.append(student)
        if find_list:
            return find_list
        else:
            print(f'没有找到学生{name}')

    #输入姓名
    def input_name(self):
        while True:
            name=input('输入姓名：').strip()
            if name:
                return name
            else:
                continue


    #显示菜单
    def show_menu(self):
        #f-string
        print(f"""
        ****************************
        欢迎使用【{self.name}】V1.1
            1.显示所有学生信息
            2.新建学生信息
            3.查询学生信息
            4.修改学生信息
            5.删除学生信息
            0.退出系统
        ****************************
        """)

    #1.显示所有学生系统
    def show_all_student(self):
        self.beauty_printt(self.data)

    #2.新建学生信息
    def create_student(self):
        name=self.input_name()
        sex=self.choose_sex()
        address=input('输入地址:')
        birthday=input('输入生日:')
        student=Student(name,sex,address,birthday)
        self.data.append(student)

    #3.查询学生信息
    def find_student(self):
        find_list=self.find_student_by_name()
        self.beauty_printt(find_list)

    #4.修改学生信息
    def modify_student(self):
        find_list=self.find_student_by_name()
        if find_list:
            self.beauty_printt(find_list)
            index=int(input('选择修改的序号：'))
            student=find_list[index]
            print('当前修改的是：')
            self.beauty_printt([student])
            name=input('输入新名字：').strip()
            sex=self.choose_sex()
            address=input('输入新地址：')
            birthday=input('输入新生日：')
            if name:
                student.name=name
            student.sex=sex
            student.address=address
            student.birthday=birthday

    #5.删除学生信息
    def remove_student(self):
        find_list=self.find_student_by_name()
        if find_list:
            self.beauty_printt(find_list)
            index=int(input('选择删除序号：'))
            print('当前要删除的是：')
            student=find_list[index]
            self.beauty_printt([student])
            self.data.remove(student)
            print('删除成功！')


if __name__=='__main__':
    student_sys=System_student('BiliBili学生管理系统')
    student_sys.start()