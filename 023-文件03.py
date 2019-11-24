#f.close()方法：如果文件操作在写入之后不适用这个方法，就一直在写入状状态，可能会早成数据丢失 
f = open("D:\\record.txt",encoding='utf-8')
boy = []
girl = []
count = 1
for each_line in f:
    if each_line[:6] != '======':
        (role,link_spoken) = each_line.split(':',1)
        if role == '小甲鱼':
            boy.append(link_spoken)
        else:
            girl.append(link_spoken)
    else:
        file_name_boy = 'boy_'+str(count)+'.txt'
        file_name_girl = 'girl'+str(count)+'.txt'
        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl,'w')
        boy_file.writelines(boy)
        girl_file.writelines(girl)
        boy_file.close()
        girl_file.close()
        boy = []
        girl = []
        count += 1
file_name_boy = 'boy_'+str(count)+'.txt'
file_name_girl = 'girl'+str(count)+'.txt'
boy_file = open(file_name_boy,'w')
girl_file = open(file_name_girl,'w')
boy_file.writelines(boy)
girl_file.writelines(girl)
boy_file.close()
girl_file.close()