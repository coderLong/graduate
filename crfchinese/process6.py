# -*-coding:utf-8-*-
def make_crf(file_name, new_file_name):
    f1 = open(file_name)
    f2 = open(new_file_name,'w')
    line_list = f1.readlines()
    for index in range(len(line_list)):
        line_list[index]=line_list[index].decode('utf-8')
    for index in range(len(line_list)):
        if "user:" in line_list[index]:
            act_str = line_list[index+4]
            if act_str[act_str.find(":")+1] == '1':
                user_sentence = line_list[index+1].strip()
                print user_sentence
                print(len(user_sentence))
                tag_line = line_list[index+2].strip()
                tag_list = tag_line[tag_line.find(":")+1:].split()
                print tag_list
                print len(tag_list)
                agent_line = line_list[index+5].strip()
                agent_list = agent_line[agent_line.find(":")+1:].split()
                agent_act_num = len(agent_list)
                null_act_num = 4-agent_act_num
                user_act_line = line_list[index+4].strip()
                user_act_list = user_act_line[user_act_line.find(":")+1:].split()
                for i in range(len(user_sentence)):
                    f2.write(user_sentence[i].encode('utf-8'))
                    for k in range(agent_act_num):
                        f2.write((' '+agent_list[k]).encode('utf-8'))
                    for k1 in range(null_act_num):
                        f2.write((' '+'null').encode('utf-8'))
                    f2.write((' '+tag_list[i]+'\n').encode('utf-8'))
                f2.write('ACT'.encode('utf-8'))
                for k in range(agent_act_num):
                        f2.write((' '+agent_list[k]).encode('utf-8'))
                for k1 in range(null_act_num):
                        f2.write((' '+'N').encode('utf-8'))
                f2.write((' '+user_act_list[-1]).encode('utf-8'))
                f2.write('\n\n'.encode('utf-8'))
    f1.close()
    f2.close()


def count_agent_act(file_name):
    f = open(file_name)
    count=[0,0,0,0,0,0]
    intent_list = []
    user_int_list = []
    m=0
    for line in f.readlines():
        m= m+1
        if "agent_act" in line:
            line = line.strip()
            act_list = line[line.find(":")+1:].split()
            k = len(act_list)
            count[k]+=1
            for act in act_list:
                if act not in intent_list:
                    intent_list.append(act)
                if act ==  "_loc":
                    print line
                if act == "conf_":
                    print line
                if act == "select_":
                    print line
                    print m
        if "user_intent" in line:
            line = line.strip()
            user_act_list = line[line.find(":")+1:].split()

            for act in user_act_list:
                if act not in user_int_list:
                    user_int_list.append(act)
                if act == "inf_":
                    print line
    f.close()
    print(count)
    for it in intent_list:
        print it
    print len(intent_list)
    print"user act:"
    for it in user_int_list:
        print it
    print len(user_int_list)
# count_agent_act('G:/fulldialogue3-11(6)')

# make_crf('G:/crf.test','G:/china.crf.test')

def count_sen_num(file):
    f = open(file)
    num = 0
    for line in f.readlines():
        line = line.strip()
        line_list = line.split()
        if len(line_list) == 0:
            num+=1
    print num

count_sen_num("G:/china.crf.train")