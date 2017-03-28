#encoding:utf-8
from nltk.corpus import conll2000
from unigramChunker  import UnigramChunker
import nltk

def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)# 分句
    print "documentcut:",sentences
    sentences = [nltk.word_tokenize(sent) for sent in sentences] #分词
    print "eachsentcut:",sentences
    sentences = [nltk.pos_tag(sent) for sent in sentences]#词性标注
    print "wordtag:",sentences
    return sentences

test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print "test_sents[0]:",test_sents[0]#NP块
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
unigram_chunker = UnigramChunker(train_sents)
print unigram_chunker.evaluate(test_sents)

result = unigram_chunker.parse(ie_preprocess("I miss you! I love you!")[0])
print result
result.draw()
