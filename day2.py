#coding:utf-8
# wlihe循环练习
# 计算1+2+3+4……+100的和
# n=1
# m=0
# while n<101:
#     m=m+n
#     n=n+1
# print(m)
# 求100以内能被3整除的数，并将作为列表输出
# list = []
# n=1
# for n in range(1,101):
#     if n%3==0:
#         list.append(n)
# print(list)
# 设计一个计算器，输入两个数，自动实现加减乘除
# def sum(a,b):
#     c=a+b
#     return c
# def jian(a,b):
#     c=a-b
#     return c
# def cheng(a,b):
#     c=a*b
#     return c
# def chu(a,b):
#     if b==0:
#         print('除数不能为0')
#     c=a/b
#     return c
# a=int(input('请输入a的值：'))
# h=input("输入的计算符号：")
# b=int(input('请输入b的值：'))
# if h=='+':
#     d=sum(a,b)
# elif h=='-':
#     d=jian(a,b)
# elif h=='*':
#     d=cheng(a,b)
# elif h=='/':
#     d=chu(a,b)
# print('两数之间运算结束为：',a,h,b,'=',d)
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# def add_end(l=[]):
#     l.append('end')
#     return l
# print(add_end())
# print(add_end())
# 可变参数练习
# def list(*num):
#     n=1
#     print(*num)
#     for n in num:
#           if n%2==0:
#             print(n,'为偶数')
#         else:
#             print(n,'为奇数')
# num =[1,2,3,4,5,6,7,8,9]
# list(*num)
# 关键字参数
# def student(name,age,**sex):
#     print('name is',name,'age is',age,sex)
# student('yanjie',18,sex='女')
# 异常处理
# def calc(a,b):
#     try:
#         c=a/b
#         print(c)
#     except Exception as msg:
#         print(msg)
# a=int(input('输入a：'))
# b=int(input('输入b：'))
# calc(a,b)
# def calc(a,b):
#     try:
#         c=a/b
#         print(c)
#     except ZeroDivisionError:
#         print('除数不能为0')
#     else:          #不报异常的时候执行else
#        return c
#     # finally:           #不管报不报异常，都执行finally
#     #     return c
# def sum(a,b):
#     c=a+b
#     return c
# def jian(a,b):
#     c=a-b
#     return c
# def cheng(a,b):
#     c=a*b
#     return c
# def chu(a,b):
#     return calc(a,b)
# a=int(input('请输入a的值：'))
# h=input("输入的计算符号：")
# b=int(input('请输入b的值：'))
# if h=='+':
#     d=sum(a,b)
# elif h=='-':
#     d=jian(a,b)
# elif h=='*':
#     d=cheng(a,b)
# elif h=='/':
#     d=chu(a,b)
# print('两数之间运算结束为：',a,h,b,'=',d)
# 读取data文件中的数据，将所有的数字按照从小到大的顺序写入backup文件
# f = open ('F:\\test\\code\\data.txt','r')
# # print(f.readlines())    #读取所有行，作为一个列表输出,初始的是string类型
# # print(f.read())         #读取文件全部内容，或读取指定长度字节的数据
# m = f.readlines()
# list = []
# print(m)
# for n in m:
#     q=int(n.replace('\n',''))
#     list.append(q)
#     # print (type(q))
# print(list)
# list.sort()
# # list.reverse()
# print(list)
# f.close()
# h = open ('F:\\test\\code\\backup.txt','r+')
# print(n)
# s = 'asd'
# a='='.join(s)
# print(a)
# 类的练习
# class Preson():
#     def
#     def eat(self,food):
#         print(food,'吃东西')
#     def sleep(self):
#         print('睡觉')
# # 实例化
# a = Preson()
# # 调用类中的方法
# a.sleep()
# a.eat('高晓静')
# 构造实例化
# class Preson():
#     # 构造方法，在实例化的时候自动被执行
#     def __init__(self,name,sex):
#         print('执行init方法')
#         self.name = name
#         self.sex = sex
#     def eat(self,food):
#         print(food,'吃东西')
#     def sleep(self):
#         print(self.name,'睡觉')
# a = Preson('xiaojing','nv')
# a.sleep()
# a.eat('binggan')
# 练习：定义一个学生类：Student、内部含有一个方法：study，实现打印：xx学习xx课程
# class Student():
#     def study(self,person,kecheng):
#         print(person,'学习',kecheng)
# a=Student()
# a.study('xiaojing','it')
# 练习：定义一个类名：Student—学生、类内部含有一个属性：sno—学号，
# 一个方法：study—学习，实现打印：学号为xx的学生，学习xx课程
# class Student():
#     def __init__(self,sno):
#         self.sno = sno
#     def study(self,kecheng):
#         print('学号为：',self.sno,'的学生，学习',kecheng)
# a = Student('001')
# a.study('it')
# 继承
# class Animal():
#     def __init__(self,color):
#         self.color = color
#     def eat(self):
#         print('chi')
#     def drink(self):
#         print('he',self.color)
# # 第一步：继承谁，类中的括号就写谁
# # 第二步：子类就具有父类的所有属性和方法，但是父类不能具备子类的属性和方法
# class Gaofei(Animal):
#     def __init__(self,color,size):  #继承父类的属性写法
#         Animal.__init__(self,color)  #继承父类的属性写法，父类属性的初始化写法
#         self.size = size
# #第三步：如果父类中没有子类需要的方法，可以在子类中自行定义
#     def bark(self):
#         print('汪汪叫',self.size)
# class Tom(Animal):
#     def catch(self):
#         print('抓老鼠')
# s = Gaofei('color','size')
# s.drink()
# s.bark()
# 练习：
# 定义一个Teacher类，继承Person类，拥有自身的属性工号：gh，自身的方法：teach教课（课程）；
# 1、实现gh为xx的老师，教xx课
# 2、实现gh为xx老师，在xx上班，一月工资xx
# 3、名字是xx，工号为xx的老师，吃饭
class Person():
    def work(self,work,salary):
        print('在',work,'上班，','一月工资',salary)
    def name(self,name):
        print('名字是',name,'，',end='')

class Tescher(Person):
    def __init__(self,gh):
        self.gh = gh
    def teach(self,course):
        print( '教',course,'课')
    def ghh(self):
        print('gh为',self.gh, '的老师，', end='')
    def eat(self):
        print('吃饭')
a = Tescher('001')
a.ghh()
a.teach('数学')
a.ghh()
a.work('北京','3000')
b = Person()
b.name('闫洁')
a.ghh()
a.eat()




































