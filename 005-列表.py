#列表拥有三种方式：1，创建一个空列表，2，创建一个混合列表，3，创建一个空列表
member = ['韩志恒','赵晨阳','王天明','李康','刘依鹏']
print(member)
number = [1,2,3,4]
print(number)
#列表中可以存放不同的数据类型
mix = [1,'韩志恒',3.14,[1,2,3]]
print(mix)
#创建一个空列表
empty = []
print(empty)
#append()方法:在已有的列表中添加一个元素，注意:只能添加一个元素
member1 = ['韩志恒','赵晨阳','王天明','李康','刘依鹏']
member1.append('沈帅帅')
print(member1)
print(len(member1))
#extend()方法：在已有的列表中可以添加多个元素，但是必须通过列表的形式进行添加
#注意：append()和extend()都是自动追加到列表的末尾
member1.extend(['武鹏伟','赵昂'])
print(member1)
#insert()中有两个参数：第一个参数树说明插入的元素的位置（下标是从0开始的),第二个参数是说明奥出入的内容的
member1.insert(1,'牡丹')
print(member1)