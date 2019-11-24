def save_life(boy,girl,count):
    file_name_boy = 'D:\\boy_' + str(count) + '.txt'
    file_name_girl = 'D:\\girl_' + str(count) + '.txt'
    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()
f = open('D:\\record.txt',encoding='utf-8')
boy = []
girl = []
count = 1
for each_line in f:
    if each_line[:6] != '======':
        (role, line_spoken) = each_line.split(':', 1)
        if role == '小甲鱼':
            boy.append(line_spoken)
        else:
            girl.append(line_spoken)
    else:
        save_life(boy,girl,count)
        boy=[]
        girl=[]
        count += 1
save_life(boy,girl,count)
f.close()
