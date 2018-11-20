import preprocessdata as dp

def tokenizaParagraphs(fileName):
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
    with open("./SceneTransitionLexicon.txt") as lexicon:
        for line in lexicon:
            #print(line)
            line = line.replace('\n', '').replace('\r', '')
            if token.startswith(line):
                #print(line)
                return True
    return False


paragraphTokens = tokenizeParagraphs("./Data/Train/adventuresOfTomThumb.txt")


##detecting entities for each paragraph
## listER = getEntities(paragraphTokens)

listER = []
for i in range(0,len(paragraphTokens)):
    #....detect character ... location and time as string
    character = ['a','b','c'] ## call method to detect character in the paragraph
    location = 'palace'
    time = 'day'
    dict = {'paragraphText':paragraphTokens[i], 'character':character, 'location':location, 'time':time}
    listER.append(dict)

for i in range(0,len(listER)):
    print(listER[i]['paragraphText'])
    print(listER[i]['character'])
    print(listER[i]['location'])
    print(listER[i]['time'])
    print("\n\n")



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
    #elif change in Entity from paragraphToken[i]
        ##do the changes
    else:
        scene=scene+token
        #print(scene)

scenes.append(scene)

#print(scenes)

f = open("./Data/Output/out.txt", "w")
for scene in scenes:
    f.write("\n----SCENE----\n")
    f.write(scene)
