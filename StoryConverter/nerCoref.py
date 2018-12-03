from stanfordcorenlp import StanfordCoreNLP
from nltk import ne_chunk, Tree
from nltk import pos_tag
from nltk import word_tokenize


charglobal = []
time = 'UNK'


def nameentityrecognision(ner, dict):
    global charglobal
    global time
    char = []
    dict.update({'NAME': []})
    dict.update({'TIME': 'UNK'})
    for tuple in ner:
        if tuple[1] == 'PERSON' or tuple[1] == 'TITLE':
            if not tuple[0] in char:
                char.append(tuple[0])
                # NAME.append(tuple[0])
        elif tuple[1] == 'TIME' or tuple[1] == 'DATE' or tuple[1] == 'SET' or tuple[1] == 'DURATION':
            time = tuple[0]
            # TIME.append(tuple[0])
        dict.update(TIME=time)
        dict.update(NAME=char)
    charglobal = char

location = 'UNK'

def locationrecognision(para, dict):
    global charglobal
    global location
    dict.update({'LOCATION': 'UNK'})
    p = word_tokenize(para)
    p = pos_tag(p)
    p = ne_chunk(p)
    for words in p:
        if type(words) == Tree:
            for i in range(0, len(words)):
                if words.label() == 'GPE':
                    #LOCA.append
                    if not words[0][0] in charglobal:
                        location = words[0][0]
    dict.update(LOCATION=location)

# fsstory = open("./Data/Train/sleepingBeauty.txt")
#nlp = StanfordCoreNLP(r'/home/sai/stanford-corenlp-full-2018-10-05', quiet=True, timeout=100000)
#nlp = StanfordCoreNLP(r'/Users/unaizafaiz/Documents/UIC/Fall2018/SNLP/Project/ConverstionOfStoryToScreenplay/stanford-corenlp-full-2018-10-05', quiet=False, timeout=100000)
# story = fstory.read()


def getentity(storyList, nlp):
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

