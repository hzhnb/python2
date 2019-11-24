#字符串，可以进行以下操作：[:],
str = 'I love meinv'
print(str[:4])
print(str[4])
#字符串可以和元组一样进行拼接
print(str[6:] + ' 插入元素 ' + str[:6])
#capitlize()方法：把字符串的首字母改成大写
str2 = 'xiaoxie'
print(str2.capitalize())
#casefold:将所有字符转化为小写
str3 = 'DAXIExiaoxie'
print(str3.casefold())
#center(width):将字符串居中，并使用空格填充至长度width的新字符串
print(str3.center(100))
#count(sub,start,end):表示sub在字符串里面出现的次数，start和end表示范围，可选
print(str3.count('i'))
#endswith(sub,start,end):检查字符串是否以sub子字符串结束，如果是：返回True,如果不是：返回False,start和end可选
print(str3.endswith('i'))
#enpandtabs([tabsize=8]):把字符串中的（\t)符号转换为空格，如不指定参数，，默认的空格数tabsize=8
str4 = 'I\tlove\tcaobi'
print(str4)
print(str4.expandtabs(tabsize=20))
#find(sub,start,end):检测sub是否包含在子字符串中，如果有则返回索引，否则返回-1，start,end可选
print(str3.find('x',9,11))
print(str3.find('z'))
#index(sub,start,end):和find方法一样，不过如果sub不在string会返回一个异常
#isalnum()：如果字符串至少有一个字符并且所有字符都是字母或数字则返回True,否则返回False
print(str3.isalnum())
#isalpha():如果字符串中至少有一个字符并且所有的字符都是字母则返回True,否则返回False
str5 = '韩志恒'
print(str5.isalpha())
#isdecimal()：如果字符串只包含十进制数则返回True，否则返回False
#isdigit():如果字符串值包含数字则返回True,否则返回False
#举例如下：以下为：byte型，如果是用isdecimal()则会报错，如果使用isdigit则会返回True
str6 = b'15'
#print(str6.isdecimal())
print(str6.isdigit())
#issupper():如果字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回True,否则返回False
#islower():如果字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回True,否则返回False.如果是中文，则会返回False
#isnumeric():如果里面填写小数会输出False，写byte型会报错，剩余的都会输出True
str7 = b'7'
#print(str7.isnumeric())
#istitle():所有的单词都是以大写字母开头，其余字母都是小写，则返回True,否则返回False
#join(sub)：以使用此方法的字符串作为分隔符，插入到sub中
#split(sep=None,maxsplit=-1):不带参数默认是以空格为分隔符进行切片的，如果maxsplit参数有设置，则仅分割maxsplit个子字符串，
#maxsplit的值不能大于使用分割符切片的最大数量，否则只会切到最大数量，相当于索引下标
str8 = 'i love fishc'
print(str8.split())
print(str8.split('i',1))
#translate()
str9 = 'sssssssaaaaaasssss'
print(str9.translate(str9.maketrans('s','b')))
print('ssss')
print(str9.zfill(50))