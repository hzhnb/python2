"""
while条件：
    循环体
"""
"""
    for 目标 in 表达式
"""
favourite = 'FishC'
for i in favourite:
    print (i,end=' ')
member = ['韩志恒','赵晨阳','王天明','李康','刘依鹏']
for each in member:
    print(each,len(each))
"""
range([start,]stop[,step=1])
这个BIF有三个参数，其中用中括号括其起来的两个表示这两个参数是可选的。step=1表示第三个参数的值默认为1。
range这个BIF的作用是生成一个从start参数的值开始到stop参数的值结束的数字序列（含start,不含stop）
"""
print(range(5))
print(list(range(5)))
#传递两个参数，是从2开始到8结束，不包含9
print('------------------------------')
for j in range(2,9):
    print(j)
print('------------------------------')
#传递一个参数，默认是从0开始到4结束
for y in range(5):
    print(y)
print('---------------------------------')
for j in range(1,10,2):
    print(j)
print('---------------------------------')
#