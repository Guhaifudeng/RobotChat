#encoding:utf-8
import nltk
from nltk import CFG
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det Nom | PropN
Nom -> Adj Nom | N
VP -> V Adj | V NP | V S | V NP PP
PP -> P NP
PropN -> 'Buster' | 'Chatterer' | 'Joe'
Det -> 'the' | 'a'
N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
Adj -> 'angry' | 'frightened' | 'little' | 'tall'
V -> 'chased' | 'saw' | 'said' | 'thought' | 'was' | 'put'
P -> 'on'
""")
sent = "the angry bear chased the frightened little squirrel"
sent = nltk.word_tokenize(sent)
parser = nltk.ChartParser(grammar)
trees = parser.parse(sent)
for tree in trees:
    print tree
    tree.draw()
#nltk版本问题，导致很多函数不能用，建议NLP with python，使用教程http://www.nltk.org/book/
