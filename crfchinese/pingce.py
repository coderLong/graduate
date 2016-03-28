# -*-coding:utf-8-*-
# 将结果写到一个新文件里  第一行是句子，第二行是答案，第三行是标注
def pingce(filename,new_file_name):
    f1 = open(filename)
    f2 = open(new_file_name,'w')
    sen_list = []
    s1 = ''
    s2=''
    s3=''
    for line in f1.readlines():
        line = line.decode('utf-8')
        line = line.strip()
        line_list = line.split()
        if len(line_list) > 0:
            sen_list.append(line_list)
        else:
            for sub_list in sen_list:
                s1=s1+sub_list[0]+' '
                s2=s2+sub_list[-2]+' '
                s3 = s3+sub_list[-1]+' '
            f2.write((s1+'\n').encode('utf-8'))
            f2.write((s2+'\n').encode('utf-8'))
            f2.write((s3+'\n').encode('utf-8'))
            f2.write('\n'.encode('utf-8'))
            sen_list=[]
            s1=s2=s3=''
    f1.close()
    f2.close()
pingce('G:/cresult-3','G:/cresult-3-p')

# 查找列表中连续的B，I
def find_tag(s,tags):
    flag = []
    for i in range(len(s)):
        flag.append(0)
    for i in range(len(s)):
        if tags[i].startswith('B'):
            flag[i]=2   # B:2; I1,I1:1; I1,I2:3
        if



# 将标注序列，答案序列还原为字符串（tag1:2;tag2:3;）

def pingce2(filename, new_file_name):
    f = open(filename)
    f1 = open(new_file_name,'w')
    line_list = f.readlines()
    for index in range(len(line_list)):
        line_list[index] = line_list[range(index)].decode('utf-8')
    for index in range(len(line_list)-2):
        if len(line_list[index])>0:
            f1.write(line_list[index].encode('utf-8'))
            f1.write(line_list[index+1].encode('utf-8'))
            f1.write(line_list[index+2].encode('utf-8'))
            sentence = line_list[index].split()
            tag = line_list[index+1].split()
            gold = line_list[index+2].split()

            for i in range(len(sentence)):
                if tag[i].startswith('B'):
                    slot_name = tag[i].split('_')[-1]
                    slot_val = tag[i]
                    for k in range(len(sentence)-i):





