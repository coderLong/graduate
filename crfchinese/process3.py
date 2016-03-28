# -*-coding:utf-8-*-
# 处理usersentence
def get_user_inf(file_name, new_file_name):
    f1 = open(file_name)
    f2 = open(new_file_name, 'w')
    line_list = f1.readlines()
    for index in range(len(line_list)):
        line_list[index] = line_list[index].decode('utf-8', errors='strict')
    # print line_list[1]
    for index in range(len(line_list)):
        line = line_list[index]
        if 'user' in line:
            print line
            sub_line = line[line.find(':')+1:]
            sub_line = sub_line.strip()  #去掉user:后的suer sentence
            f2.write("user:\n".encode('utf-8'))
            f2.write((sub_line+'\n').encode('utf-8'))
            tag_line = []  # 最后的标注序列列表
            for i in range(len(sub_line)):
                tag_line.append('O')
            next_line = line_list[index + 1]  # 语料中的user sentence 的标注行
            print(next_line)
            if '{' in next_line:
                index = next_line.find('{')
                sub_string = next_line[index + 1:len(next_line) - 2]  # 标注行去掉{}
                print "next line substring: ", sub_string
                tag_list = sub_string.split(";")   # 标注单元以;分割为列表
                intention_list = []  # 意图列表
                for tag in tag_list:
                    if len(tag) > 0:
                        print tag
                        k = tag.find('(')
                        k1 = tag.find(')')
                        if k != -1:
                            act = tag[0:k]  # find act
                            if k1 - k == 1:
                                intention_list.append(act)  # only has act , act is intention
                            else:
                                tag_string = tag[k + 1:k1]  # ()中的标注信息
                                sub_tag_list = tag_string.split(',')
                                for sub_tag in sub_tag_list:
                                    if len(sub_tag) > 0:
                                        if '=' in sub_tag:
                                            eq_index = sub_tag.find('=')
                                            slot_name = sub_tag[0:eq_index]  # get slot name
                                            intention_list.append(act + '_' +slot_name)
                                            slot_value = sub_tag[eq_index+1:len(sub_tag)]  # get slot value
                                            sub_line_k = sub_line.find(slot_value)
                                            # find the index of slot value in user sentence
                                            if sub_line_k != -1:
                                                for i in range(len(slot_value)):
                                                    if i == 0:
                                                        tag_line[sub_line_k] = 'B_'+slot_name
                                                    else:
                                                        tag_line[sub_line_k+i] = 'I_'+slot_name

                                        else:
                                            slot_name = sub_tag
                                            intention_list.append(act + '_' + slot_name)
            f2.write('user_tag:'.encode('utf-8'))
            for it in tag_line:
                f2.write((it+' ').encode('utf-8'))
            f2.write('\nuser_intention:'.encode('utf-8'))
            for it in intention_list:
                f2.write((it+' ').encode('utf-8'))
            f2.write('\n'.encode('utf-8'))
            # intention_list = get_intention(next_line)  # 得到意
            print('标注序列: ')
            print(tag_line)
        if "agent_act" in line or "**" in line:
            f2.write(line.encode('utf-8'))



    f1.close()
    f2.close()
get_user_inf('G:/fulldialogue3-11(2)','G:/fulldialogue3-11(3)')
