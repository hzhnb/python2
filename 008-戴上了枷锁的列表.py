#元组：戴上枷锁的列表，元组的元素是不可以随意改变的
#创建一个元组
tople1 = (1,2,3,4,5,6,7,8);
print(tople1[1])
#以下操作和列表一致
print(tople1[5:])
#元组和普通int型的主要区别是看有没有“，”，而到底有没有小括号，其实不影响实际数据类型
#以下数据类型是元组
temp = 1,
print(type(temp))
#以下是空元组的创建
temp1 = ()
print(type(temp1))
#一下数据类型就是int型
temp2 = (1)
print(type(temp2))
print(8*(8,))
print(8*8)
#元组中对元素进行修改:操作如下，吧想要得到的元组拼接在一起
temp3 = ('韩志恒','赵晨阳','王天明');
temp3 = temp3[0:2] + ('刘依鹏',) + temp3[2:]
print(temp3)
#in,not in,<,>,and,not,or都能使用在元组里面