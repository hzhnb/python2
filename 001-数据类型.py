#bool类型可以进行加减运算，True是1，False是0
a = True
b = False
print(a + b)
#科学计数法
c = 1.5e10
print(c)
#可以对数据类型进行转化int()抢转为int型，float()抢转为float型，str()抢转为字符类型
d = 150
e = '12'
f = str(d)
print(f)
#可以使用type()函数确定数据类型
print(type(False))
#可以通过isinstance确定是什么·类型
print(isinstance(230,int))