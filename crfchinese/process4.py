# -*-coding:utf-8-*-
# 把每一句user的话里面都加入 agent 历史信息

def add_agent_act(file_name,new_file_name):
    f1 = open(file_name)
    f2 = open(new_file_name,'w')
    line_list = f1.readlines()
    for index in range(len(line_list)):
        line_list[index].decode('utf-8')
    index_list = []
    for index in range(len(line_list)):
        if '***' in line_list[index]:
            index_list.append(index)
    for index in range(len(index_list)-1):
        dialogue_list = line_list[index_list[index]:index_list[index+1]]
        user_index = 0
        agent_index = 0
        if "user" not in dialogue_list[1]:
            print "dialogue doesnot start with user!!!"
            print index_list[index]
        f2.write("************\n")
        for sub_index in range(len(dialogue_list)):
            if "agent_act" in dialogue_list[sub_index]:
                agent_index = sub_index
            if "user:" in dialogue_list[sub_index]:
                user_index = sub_index
                f2.write(dialogue_list[user_index])
                f2.write(dialogue_list[user_index+1])
                f2.write(dialogue_list[user_index+2])
                f2.write(dialogue_list[user_index+3])

                if agent_index > 0:
                    f2.write(dialogue_list[agent_index])
                else:
                    f2.write("agent_act:null\n")
                # f2.write('\n')

    f1.close()
    f2.close()
def duplicate(file_name, new_file_name):
    f1 = open(file_name)
    f2 = open(new_file_name,'w')
    for line in f1.readlines():
        if "agent_act:" in line and "select" in line:
            line=line.strip()
            index = line.find(":")
            act_list = line[index+1:len(line)].split(' ')

            act_list = list(set(act_list))
            f2.write("agent_act:")
            for it in act_list:
                f2.write(it+' ')
            f2.write('\n')
            if"agent_act:req_timel select_loc select_ loc" in line:
                print line
                print act_list

        else:
            f2.write(line)
    f2.close()
    f1.close()

add_agent_act('G:/fulldialogue3-11(3)','G:/fulldialogue3-11(4)')
duplicate('G:/fulldialogue3-11(4)','G:/fulldialogue3-11(5)')