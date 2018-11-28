import glob
import os


def tokenizeParagraphs(fileName):
    paragraphTokens = []
    with open(fileName) as f:
        for line in f:
            #print(line)
            if line not in ['\n', '\r\n']:
                paragraphTokens.append(line)
        #print(paragraphTokens)
    return paragraphTokens

def startsWith(token):
    #token = dp.removePunctuations(token)
    #print(token)
    with open("./Lexicon/SceneTransitionLexicon.txt") as lexicon:
        for line in lexicon:
            #print(line)
            line = line.replace('\n', '').replace('\r', '')
            if token.startswith(line):
                #print(line)
                return True
    return False

path = './Data/Train/*.txt'
files=glob.glob(path)
storyList = []

for file in files:
    paragraphTokens = tokenizeParagraphs(file)
    dict={'file':file, 'pTokens':paragraphTokens}
    storyList.append(dict)

#erStory = getEntities(storyList)

for story in storyList:
    paragraphTokens = story['pTokens']

    ##detecting entities for each paragraph
    ## listER = getEntities(paragraphTok ens)

    listER = []
  #  for i in range(0,5):
  #      #....detect character ... location and time as string
  #      character = ['a','b','c'] ## call method to detect character in the paragraph
  #      location = 'village'
  #      time = 'day'
  #      dict = {'paragraphText':paragraphTokens[i], 'character':character, 'location':location, 'time':time}
  #      listER.append(dict)

  #  for i in range(5,len(paragraphTokens)):
  #      #....detect character ... location and time as string
  #      character = ['a','b','c'] ## call method to detect character in the paragraph
  #      location = 'palace'
  #      time = 'day'
  #      dict = {'paragraphText':paragraphTokens[i], 'character':character, 'location':location, 'time':time}
  #      listER.append(dict)

  #  for i in range(0,len(listER)):
  #      print(listER[i]['paragraphText'])
  #      print(listER[i]['character'])
  #      print(listER[i]['location'])
  #      print(listER[i]['time'])
  #      print("\n\n")



    ##Using lexicon to detect scenes
    scenes = []
    scene = ""
    for i in range(0,len(paragraphTokens)):
        token = paragraphTokens[i]
        if i==0:
            scene = token
            #print(scene)
        elif startsWith(token):
            scenes.append(scene)
            scene = token
            #print(scene)
        #elif listER[i]['location']!=listER[i-1]['location'] or listER[i]['time']!=listER[i-1]['time']:
          #  scenes.append(scene)
          #  scene = token
        else:
            scene=scene+token
            #print(scene)

    scenes.append(scene)


    ##Print output of scenes to the file
    head, tail = os.path.split(story['file'])
    f = open("./Data/Output/SceneDetector/"+tail, "w")
    for scene in scenes:
        f.write("\n----SCENE----\n")
        f.write(scene)
