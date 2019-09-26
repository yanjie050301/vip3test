#coding:utf-8
#列表知识
'''
s=[1,2,3,4,5,6,7,8,9]
print(s[-3])
print(s[3::2])
l=range(1,8)
print (list(l))

s=[2,3,4,10,5,6,7,10,8,9]
# s1=[5,3,2]
#s,reverse()  #逆序存放,改变原来元组的值不可赋值（能不能赋值要看该函数有没有返回值，有的话可以赋值，反之亦然）
# print(s)
# s.sort()     #从小到大排序存放，改变原来元组的值，不可赋值
# print(s)
# a=(sorted(s))  #从小到大排序,3、不改变原来元组的值，只返回一个排序结果，可赋值
# print(a)
# s.insert(4,99)  #在某一位置(s[n]前面)插入该值m，不可赋值
# print(a)
#s.append(100)     #在该元组末尾追加n，不可赋值
#print(s)
# s.extend(s1)    #将s和s1两个列表连接,s表后面跟着s1表的值，不可赋值
# print(s)
# a=s.pop(0)         #删除m[n]并返回该值，可赋值
# print(s,'\n',a)
# del s[1]             #删除s[n]，n为下标
# print(s)
# s.remove(10)         #将第一次出现的元素n删除
# print(s)
# a=s.count(10)           #返回元素n在列表中出现的次数,可赋值
# print(a)
# a=max(s)             #返回列表中元素最大值
# b=min(s)             #返回列表中元素最小值
# print(a,b)
# a=len(s)             #返回列表元素的个数
# print(a)
# a=s.index(10)         #得到元素n在列表中的下标,重复的元素只获取第一个元素的下标
# print(a)
# s.clear()               #清空列表
# print(s)

# 练习：列表[11,13,5,7,0,56,23,34,72]，
# 求该列表中的最大值，最小值及列表中一共有几个元素
# 获取56元素在列表的位置
# 追加元素7
# 删除元素0
# 排序列表（由大到小）
# 将列表[66,67,68]与原列表组合
# 答案：
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

#集合知识：
s={2,3,8,8,9}    #集合是无序的，且不重复
s.add(6)        #向集合s添加元素n
# s.remove(1)      #删除集合中的元素n，如果元素不存在，报Keyerror异常
s.discard(1)        #删除集合中的元素n，不报异常
s.clear()               #清空集合
print(s)


#字典知识：
s={'a':10,'b':20,'c':15}        #字典内的元素没有顺序，不能够通过下标引用只能通过键来引用或整体引用
print(s['b'])                   #只能通过键来引用，打印b的值
s['d']=11          #插入键值， #当key不存在时即可为字典插入，但是如果存在，即为修改
s['c']=12          #修改键值
a=s.keys()
b=s.values()
c=s.items()     #取出所有的键值对，作为一个元组内的元素
#s.clear()          #清空字典
del s['b']          #删除del s[‘key’]
print(a,'\n',b,'\n',c)

'''













s=[5,36,9,5,6,2,4]
a=int(input("输入数字："))
if a in s:
    print("列表s存在该数字")
else:
    print("列表s不存在该数字")



'''