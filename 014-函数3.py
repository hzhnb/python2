#在函数中，如果有返回值，那么就返回对应的值，如果没有返回值，那么就返回：None
#函数可以返回多个类型的值
def back():
    return [1,2.2,'jjj']
print(back())
#函数变量的作用域：如下面的price,rate,final+price都是局部变量，old_price就是全局变量
#全局变量在整个代码中都有意义，局部变量值在函数中起作用
def discounts(price,rate):
    final_price = price * rate
    return final_price
old_price = float(input('请输入原件：'))
rate = float(input('请输入折扣:'))
new_price = discounts(old_price,rate)
print('打折后价格是：',new_price)
print()