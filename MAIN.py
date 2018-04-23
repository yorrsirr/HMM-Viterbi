#-*-coding:utf-8-*-

import importlib,sys
importlib.reload(sys)
import codecs

#所有词性
ww = []
#所有的词性
pos = []
#每个词出现的评率
fre = {}
#先验概率矩阵
pi = {}
#状态转移概率矩阵
A = {}
#观测概率矩阵
B = {}
B1 = {}
#dp概率
dp = {}
#路径记录
pre = []

ww_text = open('ww.txt', 'r')
pos_text = open('pos.txt', 'r')

for each in ww_text:
    ww.append(each.replace('\n', ''))
for each in pos_text:
    pos.append(each.replace('\n', ''))

ww_text.close()
pos_text.close()

#初始化概率矩阵
n = len(pos)
for i in pos:
    pi[i] = 0
    fre[i] = 0
    A[i] = {}
    B[i] = {}
    B1[i] = {}
    for j in pos:
        A[i][j] = 0
    for j in ww:
        B[i][j] = 0
        B1[i][j] = 0

#计算概率矩阵
line = 0
fin = codecs.open('yuliao.txt', 'r')
while(True):
    text = fin.readline()
    if(text == '\n'):
        continue
    if(text == ""):
        break
    tmp = text.split()
    len_temp = len(tmp)
    line += 1
    for i in range(0, len_temp):
        word = tmp[i].split('/')
        pre = tmp[i-1].split('/')
        fre[word[1]] += 1
        if(i == 1):
            pi[word[1]] += 1
        elif(i > 0):
            A[pre[1]][word[1]] += 1
        B[word[1]][word[0]] += 1
        B1[word[1]][word[0]] += 1
fin.close()


for i in pos:
    # pi[i]=pi[i]*1.0/line
    for j in pos:
        A[i][j] += 1
        # print(A[i][j])
    for j in ww:
        B[i][j] += 1
        # print(B[i][j])

for i in pos:
    pi[i] = pi[i]*1.0/line
    for j in pos:
        A[i][j] = A[i][j]*1.0/(fre[i])
    for j in ww:
        B[i][j] = B[i][j]*1.0/(fre[i])
        # print(B[i][j])
print("训练结束！")

# print(fre)
input_text = "才 发觉 已 迷失 了 来 路"
text = input_text.split(" ")

res = {}
max_res = {}
for i in text:
    res[i] = []

# print(B1)
num = len(text)
for i in range(0, num):
    for j in pos:
        if(B1[j][text[i]] != 0):
            res[text[i]].append(j)
# print(res)

#维特比算法
max_end = ""
for i in range(0, num-1):
    max = 0
    # print(res[text[i]])
    for each in res[text[i]]:
        for each1 in res[text[i+1]]:
            if(A[each][each1] > max):
                max = A[each][each1]
                max_res[i] = each
                if(i == num-2):
                    max_end = each1
# print(res[text[num-1]])
max_res[num-1] = max_end
# print(max_res)

for i in range(0, num):
    print(text[i] + '/' + max_res[i] + ' ', end = "")