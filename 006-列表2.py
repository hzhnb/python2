#列表和其他语言中的数组是一样的，也可以通过索引来获取对应的值
member1 = ['韩志恒','赵晨阳','王天明','李康','刘依鹏']
print(member1[0])
#remove()方法，从列表中删除一个元素
member1.remove('刘依鹏')
print(member1)
#del语句：del 列表名【索引】:删除索引所指向的元素。del 列表名：删除整个索引
del member1[2]
print(member1)
#pop方法：列表名.pop（）：如果不加参数，则为删除列表中最后一个元素并且返回它的值。
print(member1.pop())
#列表名.pop(索引):把具体的列表中的索引值的元素删除掉
print(member1.pop(0))
#列表分片：member[a:b]:赋值列表中从a开始到b(不含b)的元素
member = ['韩志恒','赵晨阳','王天明','刘依鹏','李康','沈帅帅']
print(member[1:3])
#member[:b]:赋值列表中从0开始到b（不含b）的元素
print(member[:3])
#member[2:]:赋值列表中从a到最后一个元素（包含最后一个元素）
print(member[1:])
#member[:]完全赋值一个列表,这种方法是用来赋值完整的列表的
print(member[:])
"""
member2 = member[:]和member3=member之间的不同：
member3只是重新找了一个标签等于和member一样的内存地址,会随着member的改变而改变
而member2则是在内存中重新开辟了一个内存空间来存放数组，不会随着member的改变而改变
"""
member2 = member[:]
member3 = member;
member.sort()
print(member2)
print(member3)