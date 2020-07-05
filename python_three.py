#类和对象：面向对象编程

#人：张三、李四、王五
#人是类
#张三、李四、王五是具体的对象

class Person:
    def __init__(self,name,sex,birthday):# __init__关键词，固定写法
        self.name=name#指代
        self.sex=sex
        self.birthday=birthday

    def say(self,word):
        print(f'{self.name}说："{word}"')#word通过外面传进来

zhang_san=Person('张三','男','20000202')
li_si=Person('李四','女','20000202')
zhang_san.say('你好')
li_si.say('你也好')