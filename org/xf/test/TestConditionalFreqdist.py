#coding:utf-8
import nltk
from nltk.corpus import brown
#链表推导式
#(genre, word) 表面1-1,实际m-n
genre_word = [(genre, word)
        for genre in brown.categories()
        for word in brown.words(categories = genre)
        ]

#输出验证
s = set([])
for test_word in genre_word:
    if test_word[0] == 'news':
        s.add(test_word[1])
        print test_word[1]
#创建条件频率分布
cfd = nltk.ConditionalFreqDist(genre_word)

"""---缺少剔除非单词终结符和根据词频筛选单词的过程
"""
#指定条件和样本作图
cfd.plot(conditions =['news','adventure'],samples = s)
