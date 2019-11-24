
print("{0} love {1}.{2}".format("I","FishC","com"))
print("{a} love {b}.{c}".format(a="I",b="FishC",c="com"))
#这种情况下，数字和字母一起使用，必须把数字放在前面
print("{0} love {b}.{c}".format("I",b="FishC",c="com"))
#print("{a} love {b}.{0}".format(a="I",b="FishC","com"))
#这里使用了双括号，大括号直接被转义了，会直接输出{0}
print("{{0}}".format("不打印"))
#0后面的冒号:表示格式化的考试，“.1f”表示四舍五入保留一位小数
print("{0:.1f}{1}".format(27.658,"GB"))
print('%c' % 97)
print('%c %c %c'%(97,98,99))
print('%d + %d = %d' % (4,5,4+5))
print('%5.2f'% 255.2335)