# -*- coding: UTF-8 -*-
"""
pickle可以存储什么类型的数据呢？
    1,所有python支持的原生类型：布尔值，整数，浮点数，复数，字符串，字节，None。
    2,由任何原生类型组成的列表，元组，字典和集合。
    3,函数，类，类的实例
"""
my_list = [123,3.14,'小甲鱼',['another list']]
pickle_file = open('D:\\my_list.pkl','wb')
import pickle
pickle.dump(my_list,pickle_file)
pickle_file.close()
pickle_file = open('D:\\my_list.pkl','rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)
#pickle模块
#存放：picking,读取：unpicking