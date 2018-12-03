import glob
import os
import nerCoref
import ner
from stanfordcorenlp import StanfordCoreNLP


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

nlp = StanfordCoreNLP(r'/home/sai/stanford-corenlp-full-2018-10-05', quiet=False, timeout=100000)
path = './Data/Train/*.txt'
files = glob.glob(path)
storyList = []

for file in files:
    with open(file) as filename:
        story = ner.preprocessing(filename, nlp)
        # paragraphTokens = tokenizeParagraphs(story)
        dict = {'file': file, 'pTokens': story}
        storyList.append(dict)

erStory = nerCoref.getentity(storyList, nlp)

for story in erStory:
    paragraphTokens = story['pTokens']

    ##detecting entities for each paragraph
    listER = story['Entities']


    ##Using lexicon to detect scenes
    scenes = []
    scene = ""
    for i in range(0, len(paragraphTokens)):
        token = paragraphTokens[i]
        print('i=' + str(i))
        print(paragraphTokens[i])
        print(listER[i])
        if i == 0:
            scene = token
            # print(scene)
        elif startsWith(token):
            scenes.append(scene)
            scene = token
            # print(scene)
        elif token.startswith("\""):
            scene = scene + token
        elif listER[i]['LOCATION'] != listER[i - 1]['LOCATION'] or listER[i]['TIME'] != listER[i - 1]['TIME'] and \
                listER[i]['TIME'] != 'UNK':
            scenes.append(scene)
            scene = token
        else:
            scene = scene + token
            # print(scene)

    scenes.append(scene)

    ##Print output of scenes to the file
    head, tail = os.path.split(story['file'])
    f = open("./Data/Output/SceneDetector/" + tail, "w")
    for scene in scenes:
        f.write("\n----SCENE----\n")
        f.write(scene)
