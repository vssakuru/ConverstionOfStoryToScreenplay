import glob
import os
import nerCoref
import ner
from stanfordcorenlp import StanfordCoreNLP



def tokenizeparagraphs(fileName):
    paragraphTokens = []
    for line in fileName:
        # print(line)
        if line not in ['\n', '\r\n']:
            paragraphTokens.append(line)
            # print(paragraphTokens)
    return paragraphTokens

def startsWith(token):
    # token = dp.removePunctuations(token)
    # print(token)
    with open("./Lexicon/SceneTransitionLexicon.txt") as lexicon:
        for line in lexicon:
            # print(line)
            line = line.replace('\n', '').replace('\r', '')
            if token.startswith(line):
                # print(line)
                return True
    return False

# nlp = StanfordCoreNLP('http://localhost',port=9000, timeout=100000)
nlp = StanfordCoreNLP(r'/home/sai/stanford-corenlp-full-2018-10-05', quiet=True, timeout=100000)
path = './Data/Train/*.txt'
#print("file path detected")
files = glob.glob(path)
storyList = []


for file in files:
    #print("for each story")
    with open(file) as filename:
        story = ner.preprocessing(filename, nlp)
        #story = tokenizeparagraphs(filename)
        dict = {'file': file, 'pTokens': story}
        storyList.append(dict)

#print("NER coref")
erStory = nerCoref.getentity(storyList, nlp)
nlp.close()

for story in erStory:
    paragraphTokens = story['pTokens']
    print(story)
    ##detecting entities for each paragraph
    listER = story['Entities']
    characters = []
    time = ''
    location = ''

    ##Using lexicon to detect scenes
    scenes = []
    entities = []
    scene = ""
    for i in range(0, len(paragraphTokens)):
        token = paragraphTokens[i]
        print('i=' + str(i))
        print(paragraphTokens[i])
        print(listER[i])
        if i == 0:
            scene = token
            # print(scene)
        elif (startsWith(token)):
            time = listER[i-1]['TIME']
            location = listER[i-1]['LOCATION']
            dict = {'chars':characters, 'time':time, 'location':location}
            entities.append(dict)
            scenes.append(scene)
            characters = []
            scene = token
        elif token.startswith("\""):
            scene = scene + token
        elif listER[i]['LOCATION'] != listER[i - 1]['LOCATION'] or listER[i]['TIME'] != listER[i - 1]['TIME'] and \
                listER[i]['TIME'] != 'UNK':
            time = listER[i-1]['TIME']
            location = listER[i-1]['LOCATION']
            dict = {'chars':characters, 'time':time, 'location':location}
            entities.append(dict)
            scenes.append(scene)
            characters = []
            scene = token
        else:
            scene = scene + token
            # print(scene)
        tempchars = listER[i]['NAME']
        for i in range(0, len(tempchars)):
            if tempchars[i] not in characters:
                characters.append(tempchars[i])
        if i == len(paragraphTokens)-1:
            time = listER[i-1]['TIME']
            location = listER[i-1]['LOCATION']
            dict = {'chars':characters, 'time':time, 'location':location}
            entities.append(dict)
            scenes.append(scene)



    #scenes.append(scene)

    ##Print output of scenes to the file
    head, tail = os.path.split(story['file'])
    f = open("./Data/Output/SceneDetector/" + tail, "w")
    for i in range(0,len(scenes)):
        f.write("\n----SCENE----\n")
        f.write("CHARACTERS:"+', '.join(entities[i]['chars']))
        f.write("\n")
        #f.write("TIME:"+entities[i]['time']+"\n")
        f.write("LOCATION:"+entities[i]['location']+"\n")
        f.write(scenes[i])
