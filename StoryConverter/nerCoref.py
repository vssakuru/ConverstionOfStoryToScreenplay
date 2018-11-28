from stanfordcorenlp import StanfordCoreNLP
from nltk import sent_tokenize, Tree
from nltk import pos_tag
from nltk import word_tokenize


def nameentityrecognision(ner):
    for tuple in ner:
        if tuple[1] == 'PERSON' or tuple[1] == 'TITLE':
            NAME.append(tuple[0])
        elif tuple[1] == 'TIME' or tuple[1] == 'DATE' or tuple[1] == 'SET' or tuple[1] == 'DURATION':
            TIME.append(tuple[0])

def locationrecognision(para):
    for words in para:
        if type(words) == Tree:
            for i in range(0, len(words)):
                if words.label() == 'GPE':
                    LOCA.append(words[0][0])


fstory = open("./Data/Train/sleepingBeauty.txt")
story = fstory.read()

sentences = sent_tokenize(story)
#nlp = StanfordCoreNLP(r'/home/sai/stanford-corenlp-full-2018-10-05', quiet=True, timeout=100000)
nlp = StanfordCoreNLP(r'/Users/unaizafaiz/Documents/UIC/Spring2017/NLP/StandfordNLP/stanford-corenlp-full-2017-06-09', quiet=True, timeout=100000)


index = 10
para = " "
NAME = []
TIME = []
LOCA = []
PRNN = []

# NER for each paragraph
for sent in sentences:
    if index > 0:
        para += sent
        index -= 1
    else:
        ner = nlp.ner(para)
        nameentityrecognision(ner)
        locationrecognision(para)
        para = " "
        index = 10
ner = nlp.ner(para)
nameentityrecognision(ner)
locationrecognision(para)

print(NAME)
print(TIME)
print(LOCA)
