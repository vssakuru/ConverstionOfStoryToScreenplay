from stanfordcorenlp import StanfordCoreNLP
from nltk import Tree
from nltk import pos_tag
from nltk import word_tokenize


def nameentityrecognision(ner, dict):
    dict.update({'NAME': []})
    dict.update({'TIME': 'UNK'})

    for tuple in ner:
        if tuple[1] == 'PERSON' or tuple[1] == 'TITLE':
            # NAME.append(tuple[0])
            dict.update(NAME=tuple[0])
        elif tuple[1] == 'TIME' or tuple[1] == 'DATE' or tuple[1] == 'SET' or tuple[1] == 'DURATION':
            # TIME.append(tuple[0])
            dict.update(TIME = tuple[0])

def locationrecognision(para, dict):
    dict.update({'LOCATION': 'UNK'})
    for words in para:
        if type(words) == Tree:
            for i in range(0, len(words)):
                if words.label() == 'GPE':
                    #LOCA.append(words[0][0])
                    dict.update(LOCATION=words[0][0])

# fsstory = open("./Data/Train/sleepingBeauty.txt")
nlp = StanfordCoreNLP(r'/home/sai/stanford-corenlp-full-2018-10-05', quiet=True, timeout=100000)
# story = fstory.read()


def getentity(storyList):
    for story in storyList:
        ER = []

        for para in story['pTokens']:
            # ....detect character ... location and time as string
            #      character = ['a','b','c'] ## call method to detect character in the paragraph
            #      location = 'village'
            #      time = 'day'
            #      dict = {'paragraphText':paragraphTokens[i], 'character':character, 'location':location, 'time':time}
            #      listER.append(dict)

            # sentences = sent_tokenize(story)\
            dict = {}
            ner = nlp.ner(para)
            nameentityrecognision(ner, dict)
            locationrecognision(para, dict)
            ER.append(dict)

        story.update({'Entities':ER})
    return storyList

    # nlp = StanfordCoreNLP(r'/Users/unaizafaiz/Documents/UIC/Spring2017/NLP/StandfordNLP/stanford-corenlp-full-2017-06-09', quiet=True, timeout=100000)


    # index = 10
    # para = " "


    # NER for each paragraph
    # for sent in sentences:
    #     if index > 0:
    #         para += sent
    #         index -= 1
    #     else:
    #         ner = nlp.ner(para)
    #         nameentityrecognision(ner)
    #         locationrecognision(para)
    #         para = " "
    #         index = 10

