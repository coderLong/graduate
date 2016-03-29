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
# pingce('G:/cresult-3','G:/cresult-3-p')

# 查找列表中连续的B，I
def find_tag(s,tag):  # s: sentence list , tags: tag list
    slot_vals = []
    map = {}
    i=0
    # print s
    # print "len s is ;",len(s)
    # print "tag list is:",tag
    while(i<len(s)):
        if tag[i].startswith(u'B'):
            slot_name = tag[i].split(u'_')[-1]
            slot_val = s[i]
            i = i + 1
            while(i < len(s)):
                if tag[i].startswith(u'I') and tag[i].split(u'_')[-1] == slot_name:
                    slot_val=slot_val+s[i]
                    i=i+1
                else:
                    break
            print slot_val
        else:
         i=i+1







# 将标注序列，答案序列还原为字符串（tag1:2;tag2:3;）

def pingce2(filename, new_file_name):
    f = open(filename)
    f1 = open(new_file_name, 'w')
    line_list = f.readlines()
    for index in range(len(line_list)):
        line_list[index] = line_list[index].decode('utf-8')
    index=0
    while(index<len(line_list)):
        print "index,",index
        if len(line_list[index].strip())>0:
            print"s index: ", line_list[index]
            print "s index+1 ", line_list[index+1]
            print line_list[index+2]
            f1.write(line_list[index].encode('utf-8'))
            f1.write(line_list[index+1].encode('utf-8'))
            f1.write(line_list[index+2].encode('utf-8'))
            sentence = line_list[index].strip().split(' ')
            tag = line_list[index+1].strip().split(' ')
            gold = line_list[index+2].strip().split(' ')
            if len(sentence)>0:
                find_tag(sentence,tag)
                find_tag(sentence,gold)
            index = index + 3
        else:
            index=index+1
    f.close()
    f1.close()

pingce2("D:/GitHub/graduate/cresult-3-p",'D:/GitHub/graduate/cresult-3-p1')





