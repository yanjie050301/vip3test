#coding:utf-8
# 1、打印小猫爱吃鱼，小猫要喝水
# class Name():
#     def __init__(self,name):
#         self.name = name
#     def fish(self):
#         print(self.name,'爱吃鱼')
#     def drink(self):
#         print(self.name,'爱喝水')
# a = input('请输入动物名称：')
# animal = Name(a)
# animal.drink()
# animal.fish()
# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小明的体重是45.0公斤
# class Person():
#     def __init__(self,name,weight):
#         self.name = name
#         self.weight = float(weight)
#     def run(self):
#         self.weight = self.weight-0.5
#         print(self.name,'跑步了一次，体重为',self.weight,'公斤')
#         return self.weight
#     def eat(self):
#         self.weight = self.weight + 1.0
#         print(self.name, '吃东西了一次，体重为', self.weight, '公斤')
#         return self.weight
#
# mingcheng = input('输入名称：')
# xiaoming = Person(mingcheng,'75.0')
# n = 1
# m = 1
# while n<3:
#     b = xiaoming.run()
#     n = n+1
# while m<3:
#     a = xiaoming.eat()
#     m = m+1
# print(mingcheng,'跑步了',n-1,'次','体重为',b)
# print(mingcheng,'吃东西了',m-1,'次','体重为',a)
# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
# 定义家具类
class  Furnture():
    # 初始化; name,area:类的属性(家具名称 占地面积)
    def __init__(self,furnture_name,furnture_area):
        self.furnture_area = float(furnture_area)
        self.furnture_name = furnture_name
    def __str__(self):
        # str方法:规范化(输出信息)
        msg1 = "家具名称为:"+self.furnture_name+"    家具面积为："+str(self.furnture_area)
        return msg1
# 定义房子类
class Home():
    def __init__(self, house_type, zarea,):
        self.house_type = house_type
        self.zarea = zarea
        # sarea: 类的属性(剩余面积)
        self.sarea = zarea
        # self.furnture_name: 类的属性(家具名称列表)
        self.furnture_name= []
    def __str__(self):
        msg2 = '房子户型为：' + self.house_type +'   总面积为：' + str(self.zarea)+ '    家具列表：'+ str(self.furnture_name)
        return msg2
    # 定义添加家具方法
    # item:家具类的一个对象
    def add_furnture(self,item):
        # append方法:将家具添加到家具列表中
        self.furnture_name.append(item.furnture_name)
        # 计算剩余面积
        self.sarea = self.sarea - item.furnture_area
        return  '    剩余面积为：' + str(self.sarea)
# 创建房子对象
fangzi = Home('两居室',80)
print(fangzi)
# 创建家具对象
bed = Furnture('床',4.0)
print(bed)
# 将家具添加到房子中(调用方法)
a = fangzi.add_furnture(bed)
print(fangzi,end='')
print(a)

zhuozi = Furnture('桌子',2.0)
print(zhuozi)
a = fangzi.add_furnture(zhuozi)
print(fangzi,end='')
print(a)

yigui = Furnture('衣柜','3.5')
print(yigui)
a = fangzi.add_furnture(yigui)
print(fangzi,end='')
print(a)

# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量