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
    print(token)
    with open("./SceneTransitionLexicon.txt") as lexicon:
        for line in lexicon:
            #print(line)
            line = line.replace('\n', '').replace('\r', '')
            if token.startswith(line):
                print(line)
                return True
    return False

#startsWith("One day they made the porridge for their breakfast, and poured it into their porridge-pots, and then went out in the wood for a walk while the porridge for their breakfast was cooling. And while they were out walking, a little Old Woman came to the house in the wood and peeped inside.")

paragraphTokens = tokenizaParagraphs("./Data/Train/adventuresOfTomThumb.txt")

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
    else:
        scene=scene+token
        #print(scene)

scenes.append(scene)

#print(scenes)

f = open("./Data/Output/out.txt", "w")
for scene in scenes:
    f.write("\n----SCENE----\n")
    f.write(scene)
