#coding:utf-8
import nltk
from nltk.book import *;
set_word = set([])
#提取当前单词最大概率连词，不能循环
def generate_model(cfdist, word, num = 10):
    for i in range(num):
        if not word in set_word:
            set_word.add(word)
        print word
        i = 0
        while word in set_word:
            word = cfdist[word][i]
            i = i+1
        #while not set_word.disjoint(word):
"""当最大概率连接词已经出现时，选择第二大，以此类推 ps:但好像没有什么意义
"""

#生成文本中词频最高的前10个词的最大连接词
def generate_model2(cfdist,set_word, num = 10):
    for i in range(num):
        print set_word[i],cfdist[set_word[i]].max()

#语料库
txt = nltk.corpus.genesis.words('english-kjv.txt')
maxprotokens_set = FreqDist(txt).keys()

#生成双连词
bigrams = nltk.bigrams(txt)

#生成条件频率分布
cfd = nltk.ConditionalFreqDist(bigrams)

#以the开头，生成随机串
string_note = u'以the开头，生成随机串'
#print type(string_note)
print string_note.encode('gbk')
#generate_model(cfd, 'the')

string_note = u'生成词频前十的最大连接词'
#print type(string_note)
print string_note.encode('gbk')

#print maxprotokens_set[:10]
generate_model2(cfd, maxprotokens_set[:10])

