#encoding:utf-8
import nltk
class UnigramChunker(nltk.ChunkParserI):#块树
    def __init__(self, train_sents):
        #将训练数据转换成适合训练标注器的形式，
        #使用tree2conlltags 映射每个块树到一个(词，标记，块)三元组的链表
        train_data = [[(t, c) for w, t, c in nltk.chunk.tree2conlltags(sent)]
                        for sent in train_sents]
        #转换好的训练数据训练一个unigram 标注器
        #eg.(u'NN', u'B-NP'), (u'IN', u'O'), (u'DT', u'B-NP'), (u'NN', u'I-NP')
        self.tagger = nltk.UnigramTagger(train_data)
    def  parse(self, sentence):
        #eg.('I', 'PRP'), ('miss', 'VBP'), ('you', 'PRP')
        pos_tags = [pos for (word, pos) in sentence]
        #(u'NNP', u'I-NP')
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        #eg.(u'Unilab', u'NNP', u'I-NP')
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                    in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)
#转换函数chunk.conllstr2tree()用这些多行字符串建立一个树表示
