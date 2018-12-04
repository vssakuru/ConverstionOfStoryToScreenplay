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



def getentity(storyList, nlp):
    global time
    global location
    for story in storyList:
        time = "UNK"
        location = "UNK"
        ER = []

        for para in story['pTokens']:

            dict = {}
            ner = nlp.ner(para)
            nameentityrecognision(ner, dict)
            locationrecognision(para, dict)
            ER.append(dict)

        story.update({'Entities': ER})
    return storyList
