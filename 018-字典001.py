#字典的标志性东西就是大括号，字典由多个键和其对应的值构成
dict1 = {'李宁':'一切皆有可能','耐克':'Just do it','阿迪达斯':'Impossible is nothing','韩志恒':'改变世界'}
print('韩志恒名言：',dict1['韩志恒'])
dict2 = {1:'one',2:'two',3:'there'}
print(dict2[1])
#创建一个空字典
dict3 = {}
print(dict3)
#dict()中只有一个参数，以下用元组去模拟只有一个参数
dict4 = dict((('F',70),('i',105),('s',115),('h',104),('C',67)))
print(dict4['F'])
dict5 = dict()
#用关键字来创建字典，里面的key是没有括号的
dict6 = dict(小甲鱼='让编程改变世界',乔布斯='或者就为改变世界')
print(dict6)
#直接给字典中的键赋值，如果key是不存在的，直接创建然后赋值，如果存在，就修改其对应value的值
dict6['乔布斯'] = '只有那些疯狂到认为自己能够改编世界的人才能够改编世界'
print(dict6)
dict6['韩志恒'] = '我要让世界因为我的存在而有所不同'
print(dict6)