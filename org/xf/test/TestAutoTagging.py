#encoding:utf-8
import jieba
import jieba.posseg as pseg
import nltk
from nltk.corpus import brown
#待标记语句
string_note = u'我郁闷我为啥没考上交大的研究生'
words_tag = pseg.cut(string_note)
for wt in words_tag:
    print wt.word.encode('gbk'),wt.flag
    # python2.7 无乱码  pydev 乱码，改gbk-utf-8

#先切词，后标记
print "first cut the sentense,then tag it"
string_note = "我郁闷我为啥没考上交大的研究生"
words_list = list(jieba.cut(string_note,cut_all = False))
default_tagger = nltk.DefaultTagger('NN')
tags = default_tagger.tag(words_list)
for wt in tags:
    print wt[0].encode('gbk'),wt[1]

#组合标注器
print "combination tagger"

#暂时不知道如何引入中文语料库
#这里使用 brown
brown_tagged_sents = brown.tagged_sents()#categories = 'news',)
train_sents = brown_tagged_sents
#print train_sents
default_tagger = nltk.DefaultTagger('NN')
unigram_default_tagger = nltk.UnigramTagger(train_sents, backoff = default_tagger)
bigram_unigram_defualt_tagger = nltk.BigramTagger(train_sents,backoff = unigram_default_tagger)
tags = bigram_unigram_defualt_tagger.tag(words_list)
print "chinese is unable to be tagged"
for wt in tags:
    print wt[0].encode('gbk'),wt[1]
#训练集得到的模型不适用于中文

print "english is able to be tagged"
enword_list = nltk.word_tokenize('I do not like green eggs and ham, I do not like them Sam I am!')
tags = bigram_unigram_defualt_tagger.tag(enword_list)
print tags
#保存训练好的标注器
#from cPickle import dump
#加载训练好的标注器
#from cPickle import load
