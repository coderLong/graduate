# -*- coding:utf-8 -*—
# drop out the agent sentence
def dropout(fileName, newFilename):
    f1 = open(fileName)
    f2 = open(newFilename, 'w')
    linesList = f1.readlines()
    for index in range(len(linesList)):
        if 'user' in linesList[index]:
            f2.write(linesList[index])
            if '{' in linesList[index + 1]:
                f2.write(linesList[index + 1])
        if 'agent:' in linesList[index]:
            if '{' in linesList[index + 1]:
                f2.write("agent:" + linesList[index + 1])
        if '*' in linesList[index]:
            f2.write(linesList[index])

    f1.close()
    f2.close()


def get_intention(line):
    index = line.find('{')
    sub_string = line[index + 1:len(line) - 2]
    # print sub_string
    tag_list = sub_string.split(";")
    intention_list = []
    for tag in tag_list:
        if len(tag) > 0:
            print tag
            k = tag.find('(')
            k1 = tag.find(')')
            if k != -1:
                act = tag[0:k]
                if k1 - k == 1:
                    intention_list.append(act)
                else:
                    tag_string = tag[k + 1:k1]
                    sub_tag_list = tag_string.split(',')
                    for sub_tag in sub_tag_list:
                        if len(sub_tag) > 0:
                            if '=' in sub_tag:
                                intention_list.append(act + '_' + sub_tag[0:sub_tag.find('=')])
                            else:
                                intention_list.append(act + '_' + sub_tag)
                                # print(tag_string)
    return intention_list


dropout('G:/fulldialogue3-11','G:/fulldialogue3-11(1)')

def get_agent_act(file_name, new_file_name):
    f1 = open(file_name)
    f2 = open(new_file_name, 'w')
    for line in f1.readlines():
        if 'agent:' in line:
            index = line.find('{')
            sub_string = line[index + 1:len(line) - 2]
            # print sub_string
            tag_list = sub_string.split(";")
            intention_list = []
            for tag in tag_list:
                if len(tag) > 0:
                    print tag
                    k = tag.find('(')
                    k1 = tag.find(')')
                    if k != -1:
                        act = tag[0:k]
                        if k1 - k == 1:
                            intention_list.append(act)
                        else:
                            tag_string = tag[k + 1:k1]
                            sub_tag_list = tag_string.split(',')
                            for sub_tag in sub_tag_list:
                                if len(sub_tag) > 0:
                                    if '=' in sub_tag:
                                        intention_list.append(act + '_' + sub_tag[0:sub_tag.find('=')])
                                    else:
                                        intention_list.append(act + '_' + sub_tag)
                        print(tag_string)
                        print intention_list
            f2.write("agent_act:")
            for item in intention_list:
                f2.write(item + ' ')
            f2.write('\n')
        else:
            f2.write(line)
    f1.close()
    f2.close()


get_agent_act('G:/fulldialogue3-11(1)', 'G:/fulldialogue3-11(2)')

