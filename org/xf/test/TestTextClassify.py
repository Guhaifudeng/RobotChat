#encoding:utf-8
"""构建一个整个语料库中前2000个最频繁词的链表"""

from nltk.corpus import movie_reviews
import random
import nltk
documents = [(list(movie_reviews.words(fileid)), category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)
            ]
#为什么要用list，而不是set,统计词频?没有，他后期处理了
random.shuffle(documents)

"""然后，定义一个特征提取器，简单地检查这些词是否在一个给定的文档中"""
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
#选取词频前2000名做特征提取 格式 contains(?):true or false

#训练分类器 Xi = 2000 {contains(?):true or false} :Yi = category
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

#测试分类器
print nltk.classify.accuracy(classifier, test_set)
#哪些特征是分类器发现最有信息量
#print classifier.most_informative_features(100)
#尝试重新训练分类器

#train_set_top100 = classifier.most_informative_features(100)
#classifier = nltk.NaiveBayesClassifier.train()
