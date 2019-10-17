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
# class Home():
#     def homes(self,house_type,area,furnture_type):
#         furnture_type = {'bed': '4.0', 'closet': "2.0", 'table': '1.5'}
#         print('房子的户型为：',house_type,end='')
# class  Furnture(Home):
#     def furnture1(self):
#         furnture_area = { 'bed' : '4.0', 'closet' : "2.0", 'table' : '1.5'}
#         a=furnture_area.values
#
#
#             self.area = self.area - float(furnture_area)
#             print(self.area)
#             return self.area
# furnture2 = ['bed', 'closet', 'table']
# for furnture_area12 in furnture2:
#     a = Home('四居','80','furnture_area12')
#     if furnture_area12 == 'bed':
#         a.Furnture1('4.0')
#     elif furnture_area12 == 'closet':
#         a.Furnture1('2.0')
#     elif furnture_area12 == 'table':
#         a.Furnture1('1.5')
# print()
# furnture_area = {'bed': '4.0', 'closet': "2.0", 'table': '1.5'}
# a = furnture_area['bed']
# print(a)
# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量