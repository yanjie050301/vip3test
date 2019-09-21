#coding:utf-8

'''
s=[1,2,3,4,5,6,7,8,9]
print(s[-3])
print(s[3::2])
l=range(1,8)
print (list(l))
'''
# s=[10,2,3,4,5,6,7,8,9]
# s1=[5,3,2]
#s,reverse()  #逆序存放,不可赋值（能不能赋值要看该函数有没有返回值，有的话可以赋值，反之亦然）
# print(s)
#s.sort()     #排序存放，不可赋值
# print(s)
# a=(sorted(s))  #排序,3、不改变原来元组的值，只返回一个排序结果，可赋值
# print(a)
# s.insert(4,99)  #在某一位置(s[n]前面)插入该值m，不可赋值
# print(a)
#s.append(100)     #在该元组末尾追加n，不可赋值
#print(s)
# s.extend(s1)    #将s和s1两个列表连接,s表后面跟着s1表的值，不可赋值
# print(s)


'''
y=[11,13,5,7,0,56,23,34,72]
a=max(y)
b=min(y)
c=len(y)
print("第一题：",a,b,c)
d=y.index(56)
print("第二题：",d)
y.append(7)
print("第三题：",y)
y.pop(4)
print(y)
y.sort()
y.reverse()
print(y)
x=[66,67,68]
y.extend(x)
print(y)

s=[5,36,9,5,6,2,4]
a=int(input("输入数字："))
if a in s:
    print("列表s存在该数字")
else:
    print("列表s不存在该数字")

'''
a=int(input())
if 100>a>=90:
    print('A')
elif 90>a>=80:
    print('B')
elif 80>a>=70:
    print('C')
elif 70>a>=60:
    print('D')
else:
    print('E')
