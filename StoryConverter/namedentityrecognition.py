from stanfordcorenlp import StanfordCoreNLP
from nltk import ne_chunk, Tree
from nltk import pos_tag
from nltk import word_tokenize


charglobal = []
time = 'UNK'
character = []


with open("./animal.txt") as fairyVocabFile:
    fairyVocab = fairyVocabFile.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
fairyVocab = [x.strip() for x in fairyVocab]


def nameentityrecognision(ner, dict):
    global charglobal
    global character
    global time
    relations = ['mother','Mother','father','Father','brother', 'Brother', 'sisters', 'Sisters','sister','Sister',
                 'brothers', 'Brothers', 'wife', 'husband', 'grandmother','Grandmother']
    char = []
    dict.update({'NAME': []})
    dict.update({'TIME': 'UNK'})
    for tuple in ner:
        if tuple[1] == 'PERSON' or tuple[1] == 'TITLE' or tuple[0].lower() in relations or tuple[0].lower() in fairyVocab:
            if not tuple[0].lower() in char:
                char.append(tuple[0].lower())
                if tuple[0].lower() not in character:
                    character.append(tuple[0].lower())
                # NAME.append(tuple[0])
        elif tuple[1] == 'TIME' or tuple[1] == 'DATE' or tuple[1] == 'SET' or tuple[1] == 'DURATION':
            time = tuple[0]
            # TIME.append(tuple[0])
        dict.update(TIME=time)
        dict.update(NAME=char)
    charglobal = char

location = 'UNK'

def locationrecognision(para, dict):
    global character
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
                    if not words[0][0].lower() in character:
                        location = words[0][0]
    dict.update(LOCATION=location)


def formatePara(para):
    str = ""
    for sent in para:
        if not sent.startswith("\""):
            str += sent
    return str

def getentity(storyList, nlp):
    global time
    global location
    for story in storyList:
        time = "UNK"
        location = "UNK"
        ER = []

        for para in story['pTokens']:
            para = formatePara(para)
            dict = {}
            ner = nlp.ner(para)
            nameentityrecognision(ner, dict)
            locationrecognision(para, dict)
            ER.append(dict)

        story.update({'Entities': ER})
    return storyList
