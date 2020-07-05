'''
#基础 + - * / 算法
print(1+2)
print (1+2+3)
print (3-1)
print(3-1-1)
print (3*7)
print (3*7*3)
print (21//7)
print(2+4*2/4)
print((2+4)*2/4)
print ()

#变量（不能用数字开头）=值
box_width=3
BOX_WIDTH=33
box_heigth=4
s=box_width*box_heigth
S=BOX_WIDTH*box_heigth
print (s)
print (S)
print ()

#python 流程控制 if-else 语句
age=18
if age>16:
    print("可以进入")
else:
    print ("年纪太小，不能进入")
print()

#python 流程控制 if-elif-ekse 语句
score=80
if score>=90:
    print("A")
elif score>=80:
    print ("B")
elif score>=70:
    print ("C")
elif score>=60:
    print("D")
else:
    print("E")
print ()

#python 的for 遍历：从一个序列中逐一取出
for i in range(5):
    print(i)
for i in range(1,15,2):#从1开始，增量是2，范围<15
    print(i)
print ()

#python 的 while 循环
n=1
while(n<10):
    print (n)
    n=n+1
else:
    print("循环结束了")
print ()

#python 的for 循环嵌套
#经典案例：输出乘法口诀表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}",end=" ")
    print()
print ()

#经典案例：通过while 输出乘法口诀表
n=1;
while n<=9:
    m=1;
    while m<n:
        print(f"{m}*{n}={m*n}",end=" ")
        m=m+1
    n=n+1
    print ()
print ()

#经典案例：while+for 输出乘法口诀表
n=1
m=1
while n<=9:
    for m in range(1,n+1):
        print(f"{m}*{n}={m*n}",end =" ")
    n=n+1
    print()
print()

#循环控制： break，结束整个循环
while True:
    s=input("输入0退出,请输入：")
    if s=="0":
        print("已退出")
        break
    print("你输入的是：",s)
print()

#循环控制： continue，跳过后面的代码，立即直接进入下一轮循环
for i in [1,2,3,4,5,6,7,8,9]:
    if i==3:
        continue
    print(i)
print()

#实战 猜数字
# 在1-100直接随机产生一个整数，
# 让用户反复猜，
# 只提示”猜大了“或”猜小了“，
# 猜对结束游戏
import random#import导入一个random随机数模块
m=random.randint(1,100)
while True:
    n=int(input("输入1~100之间的整数："))
    if n<m:
        print("猜小了")
    elif n>m:
        print("猜大了")
    else:
        print ("猜对了")
        break
print()

#实战 猜数字改进
# 在1-100直接随机产生一个整数，
# 让用户只允许猜五次，如果没有猜对就结束游戏，
# 只提示”猜大了“或”猜小了“，
# 猜对结束游戏
# ctrl+/  注释快捷键
import random#import导入一个random随机数模块
m=random.randint(1,100)
count=0#猜了的次数
total=5#猜的总数
while count<total:
    n=int(input("输入1~100之间的整数(只有五次机会)："))
    count=count+1
    if n<m:
        print("猜小了")
    elif n>m:
        print("猜大了")
    else:
        print (f"你一共猜了{count}次，猜对了")
        break
else:
    print(f"很抱歉，你没有在{count}次机会中猜对，游戏结束，答案是{m}")
print()

#一对单引号或双引号 单引号双引号本质上没有区别
print('python')
print("python")
print()

#一对单三引号（''''''）或一对双三引号（""""""） 要输出多行文本可以使用这种
print("""py
C++
PHP
thon""")
print()

#转义字符 \n  \t
print('这里\n有一个换行')
print('这里\t有一个制表符')
print()

#字符串的索引
#正向从0开始计数
s='床前明月光'
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print()
#逆向从-1开始计数
s='床前明月光'
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print()

#字符串切片
#’字符串‘.[开始：结束：步长]
s='床前明月光！'
print(s[1:4])#从一到四取
print(s[1:5:3])#从一开始取往后两位
print(s[0:])#从开始到结尾
print(s[2:])#从二到结尾
print(s[:4])#从开始到三
print(s[:])#从开始到结尾
print()

#格式化输出：format()
user_1="韩梅梅"
user_2="李雷"
print('{}对{}说："你好！"'.format(user_1,user_2))
#新的格式化输出：f-string
print(f'{user_2}对{user_1}说："你好！"')
print()

#+号连接多个字符串
print("are "+"you "+"ok")
print()

#列表[]
my_list=[1,2,'a',1.3]
print(my_list)
#列表的索引
my_list=[1,2,'a',1.3]
print(my_list[2])
print(my_list[-1])
#列表的切片
my_list=[1,2,'a',1.3]
print(my_list[1:4])
#列表添加元素：append()直接插入在最后
my_list=[1,2,'a',1.3]
my_list.append("python")
print(my_list)
#列表添加元素： insert()可以选择插入位置
my_list=[1,2,'a',1.3]
my_list.insert(2,"python")
print(my_list)
#列表添加元素：extend()方法必须加一个序列
my_list=[1,2,'a',1.3]
my_list.extend("python")
print(my_list)
#列表删除元素：pop()中间不写就默认删除最后一个位置
my_list=[1,4,'a',1.3]
my_list.pop(2)
print(my_list)
#列表删除元素：remove()删除具体某个值
my_list=[1,4,'a',1.3]
my_list.remove(1.3)
print(my_list)
#列表的修改
my_list=[1,2,'a',1.3]
my_list[3]=33
print(my_list)
print()

#元组（不可变的列表）和列表一致，只是不能修改
my_list=(1,2,'a',1.3)
print(my_list)
print()

#字典{}
#键值对  键-->值
user={
    'name':'Tom',
    'age':'18',
    'gender':'male'
}
user['fav']='打篮球'#新增一个
user['age']=28#修改
print(user)#输出全部
print(user['age'])#输出具体某个值
print()
'''
#为什么使用函数
#2个目的：
# 1.降低编程难度
# 2.增加代码复用

# 1+2+3+...+100
#用函数,函数关键词def
def qiu_he(n,m):
    sum=0
    while n<=m:
        sum+=n
        n+=1
    return sum

print(qiu_he(1,100))
print(qiu_he(1,10))
print(qiu_he(5,32))