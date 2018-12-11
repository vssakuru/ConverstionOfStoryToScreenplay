import glob
import os
import namedentityrecognition
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

nlp = StanfordCoreNLP('http://localhost',port=9000, timeout=100000)
#nlp = StanfordCoreNLP(r'/home/sai/stanford-corenlp-full-2018-10-05', quiet=True, timeout=100000)
path = './Data/Test/*.txt'
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
erStory = namedentityrecognition.getentity(storyList, nlp)
nlp.close()

for story in erStory:
    head, tail = os.path.split(story['file'])
    print(tail+"-----")
    paragraphTokens = story['pTokens']
    #for i in range(0,len(paragraphTokens)):
     #   print(i)
     # print(paragraphTokens[i])
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
        #print(paragraphTokens[i])
        #print(listER[i])
        if i == 0:
            scene = token
            print("i="+str(i+1)+": ")
        elif (startsWith(token)):
            time = listER[i-1]['TIME']
            location = listER[i-1]['LOCATION']
            dict = {'chars':characters, 'time':time, 'location':location}
            entities.append(dict)
            scenes.append(scene)
            print('i=' + str(i+1)+": NEW SCENE")
            characters = []
            scene = token
            #print("cond starts with met")
        elif token.startswith("\""):
            scene = scene + token
            #print("cond \" ")
            print('i=' + str(i+1)+": ")
        elif (listER[i]['LOCATION'] != listER[i - 1]['LOCATION']) or ((listER[i]['TIME'] != listER[i - 1]['TIME']) and \
                (listER[i]['TIME'] != 'UNK' and listER[i-1]['TIME'] != 'UNK')):
            time = listER[i-1]['TIME']
            location = listER[i-1]['LOCATION']
            dict = {'chars':characters, 'time':time, 'location':location}
            entities.append(dict)
            scenes.append(scene)
            print('i=' + str(i+1)+": NEW SCENE")
            characters = []
            scene = token
            #print("cond location time change")
        else:
            scene = scene + token
            #print("No cond met")
            print('i=' + str(i+1)+": ")
            #print(scene)

        tempchars = listER[i]['NAME']
        for j in range(0, len(tempchars)):
            if tempchars[j] not in characters:
                characters.append(tempchars[j])

        if i == (len(paragraphTokens)-1):
            #print("i=len of tokens---last scene"+scene)
            time = listER[i-1]['TIME']
            location = listER[i-1]['LOCATION']
            dict = {'chars':characters, 'time':time, 'location':location}
            entities.append(dict)
            scenes.append(scene)

    #for i in range(0,len(scenes)):
     #   print(str(i)+"--\n"+scenes[i])


    print("\nNo of scenes "+str(len(scenes)))


    #scenes.append(scene)

    ##Print output of scenes to the file
    head, tail = os.path.split(story['file'])
    f = open("./Data/Output/Test/" + tail, "w")
    for i in range(0,len(scenes)):
        f.write("\n----SCENE----\n")
        f.write("CHARACTERS:"+', '.join(entities[i]['chars']))
        f.write("\n")
        #f.write("TIME:"+entities[i]['time']+"\n")
        f.write("LOCATION:"+entities[i]['location']+"\n")
        f.write(scenes[i])
