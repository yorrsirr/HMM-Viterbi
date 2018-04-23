#-*-coding:utf-8-*-

import codecs

#所有词性
ww = []
#所有的词性
pos = []

ww_pos_text = open('ww_pos.txt', 'w')
yuliao_text = open('yuliao.txt', 'w')
pos_text = open('pos.txt', 'w')
ww_text = open('ww.txt', 'w')
fin = codecs.open("199801.txt", "r")
while(True):
    text = fin.readline()
    # print(text)
    if(text == ""):
        break
    tmp = text.split()
    if tmp:
        tmp.pop(0)
        print(tmp)
        for each in tmp:
            yuliao_text.write(each + " ")
        yuliao_text.write('\n')

        n = len(tmp)
        for i in range(0, n):
            word = tmp[i].split('/')
            ww_pos_text.write(word[0] + '/' + word[1] + '\n')
            if(word[1] not in pos):
                pos.append(word[1])
                pos_text.write(word[1])
                pos_text.write('\n')
            word[0].replace('[', '')
            if(word[0] not in ww):
                ww.append(word[0])
                ww_text.write(word[0])
                ww_text.write('\n')
ww_text.close()
pos_text.close()
yuliao_text.close()
ww_pos_text.close()



