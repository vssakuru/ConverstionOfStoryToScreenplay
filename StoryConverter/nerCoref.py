from stanfordcorenlp import StanfordCoreNLP
from nltk import sent_tokenize
from nltk import pos_tag
from nltk import word_tokenize


def nameentityrecognision(ner):
    for tuple in ner:
        if tuple[1] == 'PERSON' or tuple[1] == 'TITLE':
            NAME.append(tuple[0])
        elif tuple[1] == 'TIME' or tuple[1] == 'DATE' or tuple[1] == 'SET' or tuple[1] == 'DURATION':
            TIME.append(tuple[0])


fstory = open("/home/sai/Desktop/git/SNLP-Proj/ConverstionOfStoryToScreenplay/StoryConverter/Data/Train/cinderella.txt")
story = fstory.read()

sentences = sent_tokenize(story)
nlp = StanfordCoreNLP(r'/home/sai/stanford-corenlp-full-2018-10-05', quiet=True, timeout=100000)

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
        print(nlp.coref(para))
        nameentityrecognision(ner)
        para = " "
        index = 10
ner = nlp.ner(para)
nameentityrecognision(ner)
print(NAME)
print(TIME)


# Coref for each paragraph
# for sent in sentences:
#     if index > 0:
#         para += sent
#         index -= 1
#     else:
#         coref = nlp.coref(para)
#         print(coref)
#         para = " "
#         index = 10
# ner = nlp.ner(para)
# nameentityrecognision(ner)
# print(NAME)
# print(TIME)
# words = word_tokenize(story)
# pos = pos_tag(words)
# for p in pos:
#     if p[1] == 'PRP' or p[1] == 'PRP$':
#         PRNN.append(p[0])
# print(PRNN)