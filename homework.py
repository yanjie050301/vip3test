#coding:utf-8
#第一题：输入一个数，判断该数的范围：90-100：等级为A……60以下：等级为E
'''
a=int(input('请输入一个数字：'))
if 100>a>=90:
    print('等级为A')
elif 90>a>=80:
    print('等级为B')
elif 80>a>=70:
    print('等级为C')
elif 70>a>=60:
    print('等级为D')
elif a>=100 or a<=1:
    print("小伙子，请输入1-100的数~~")
else:
    print('等级为E')
'''
#第二题：定义一个列表，从键盘输入一个随机数，判断该数是否在列表中
a=int(input("请输入一个数字"))
b=[1,2,5,6,3,25,3,5]
if a in b:
    print("该数字在列表b中")
else:
    print("该数字不在列表b中")


























# a="abcdef"
# b=list(a)
# b.reverse()
# a="".join(b)
# print(a)

# n=1
# m=0
# while n<4:
#     while m<3:
#         c=b[m]
#         b[m]=b[5-m]
#         b[5-m]=c
#         ++m
#     n=n+1
# print(b)
# a="".join(b)
# print("a=",a)