#encoding:utf-8
import pynlpir as nlpir
nlpir.open()
s1 = "聊天机器人到底该怎么做呢？"
s2 = '聊天机器人到底该怎么做呢？'
segments = nlpir.segment(s1)# s1 s2均ok
for segment in segments:
    print segment[0].encode('gbk'),segment[1]


key_words = nlpir.get_key_words(s1,weighted = True)
for key_word in key_words:
    print key_word[0].encode('gbk'),key_word[1]
nlpir.close()
