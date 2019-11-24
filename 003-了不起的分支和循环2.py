#在python中elif相当于其他其他语言中的else if
#在其他语言中else是匹配离它最近的一个if的，但是在python中，else是看和那个else的缩进一样来确定是匹配那个if
#程序一：在这个程序中，else是和第一个if对齐的，所以他对应的是第一个if
hi = 1;
if hi>2:
    if hi>7:
        print('好棒，好棒')
else :
    print("切~")
#程序二：在这个程序中，else是和第二个if对齐的，所以是和第二个if匹配
ha = 9
if ha>2:
    if ha>7:
        print('好棒，好棒')
    else:
        print('切~')
#三目运算符：如果a<b正确，执行if前面的内容，如果错误，执行else后面的内容
a = 6
b = 7
small = a if a < b else  b
print(small)
#assert这个关键字被我妈称之为“断言”，当这个关键词后面的条件为假是，程序自动崩溃并抛出AssertionError的异常
#一般来说，我妈可以用他来置入检查点，当需要确保程序中的某个条件一定为真时才让程序正常工作，assert关键字非常有用
#assert 3>4
var = 20
ver = 25
print('var的值为：',var)
print('var的值为：%d,ver的值为：%d'%(var,ver))
temp = input("temp的值为：")
print(temp)
