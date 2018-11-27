import nltk
import re

def removePunctuations(cleanText):
    cleanText = re.sub(r'[?;!$:+*",\']*','',cleanText) #remove punctuations
    cleanText = re.sub(r'[./()\-=_]',' ',cleanText)
    return cleanText

def preprocessdata(story):
    story = nltk.word_tokenize(story)
    stopWordsSet = nltk.corpus.stopwords.words('english')
    for words in story:
        if words in stopWordsSet:
            story.remove(words)

    cleantext = ''
    wnl = nltk.stem.WordNetLemmatizer()
    for word in story:
        cleantext += wnl.lemmatize(word) + ' '

    return cleantext

def processStoryText(fileName):
    story =""
    with open(fileName) as f:
        for line in f:
            #print(line)
            if line in ['\n', '\r\n']:
                story+="\n\n"
                #print(story)
            else:
                line = line.replace('\n', ' ').replace('\r', '')
                story+=" "+line
                #print("not empty"+story)

    #print(story)
    return story


f = open("./Data/Output/processedStory.txt", "w")
f.write(processStoryText("./Data/Test/storyOfBlueBeard.txt"))