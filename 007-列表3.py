list1 = [123]
list2 = [456]
print(list1>list2)
#列表在比较大小的时候，只比较第一个元素，那个列表的第一个元素大，则哪个列表就大.
list1 = [123,456]
list2 = [234,123]
list5 = ['kkk']
list6 = ['ZZZ']
list7 = [456,'lll']
#如果两个列表的类型完全不同的话，那么这两个列表是不能比较大小的，否则直接回报错。
#如果两个列表的第一个元素的数据类型一致，那么就可以比较大小，无论是什么类型.
list8 = True;
list9 = False;
print(list8 > list9)
print(list1 > list7)
#如果是两个列表是字符型的，则从第一个元素第一个字母进行ASCII比较,
print(list6 < list5)
print(list1>list2)
#两个列表相加，就相当于追加在一个列表后面几个元素，相当于extend()方法
list3 = list1 + list2;
list4 = list2 + list1;
print(list3)
print(list4)
#如果想实现列表的追加，最好还是使用append(),extend()等方法，这样是最好的，
#因为相加的两个列表的类型必须一致，否则就会报错。如：list1+'账号'，数字加文字就会报错，
#想要实现就必须使用append()，insert()等方法
#在列表中可以直接使用“*”运算符，这样子：乘及就会是列表扩大为原来的几倍
print(list1 * 2)
#"in"和"not in"可以判断一个元素是否在此列表中
print(123 in list1)
print(123 not in list1)
#在列表中定义了一个列表，然后用"in"判断小列表中一个元素是否在这个大列表中结果是False。
list10 = [123,['罗密欧','朱丽叶'],456];
print('罗密欧' in list10)
#想要做这样的判断，必须指出小小列表在大列表中的位置。如下所示：
print('罗密欧' in list10[1])
#想要访问列表中列表的元素必须使用像c语言中的二维列表一样,如下所示：
print(list10[1][1])
#count()方法：查询一个元素在一个列表中出现了几次
print(list1.count(123))
#index('要查找的元素'，a,b),a,b可以省略，如果省略，则表示从第0个元素查找，否则就是从第a个元素开始查找
#如果a,b都没有省略，则表示从查找的位置从a出发，到b(不好b)结束,像下面这样程序会直接报错not in list11
list11  = [123,234,345,567];
#print(list11.index(345,0,2))
#reserve()方法，就是将列表进行翻转,它没有返回值
list11.reverse()
print(list11)
#sort()：对类型一致的列表进行大小比较，如果是字符类型的，就比较ASCII码
list12 = [4,6,81,2,3,1,65]
list12.sort()
print(list12)
list13 = ['ppp','ZZZ'];
list13.sort();
print(list13)
#sort(reverse=True):表示把列表从大到小进行排序
list12.sort(reverse=True)
print(list12)
