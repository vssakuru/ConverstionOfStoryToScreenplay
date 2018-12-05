from stanfordcorenlp import StanfordCoreNLP
from nltk import sent_tokenize
import string

def tokenizeparagraphs(fileName):
    paragraphTokens = []
    for line in fileName:
        # print(line)
        if line not in ['\n', '\r\n']:
            paragraphTokens.append(line)
        # print(paragraphTokens)
    return paragraphTokens


pronouns = ["he", "He", "she", "She"]

def preprocessing(file, nlp):
    story = ''
    pTokens = tokenizeparagraphs(file)
    for index in range(len(pTokens)):
        if index == 0:
            p = nlp.coref(pTokens[0])

        else:
            tempToken = ''
            tempToken = pTokens[index-1] + pTokens[index]
            #print("*******"+str(pTokens[index-1]))
            p = nlp.coref(tempToken)
        sentList = sent_tokenize(pTokens[index])
        st = ''
        #print(p)
        for i in p:
            #print("i="+str(i))
            for index2 in range(1, len(i)):
                if i[index2][3] in pronouns:
                    #print("---pronoun detected---"+str(i[index2][3]))
                    if (i[index2][0]-1) < len(sentList):
                        #print("Before --- "+str(sentList))
                        sent = sentList[((i[index2][0])-1)]
                        #print(sent)
                        #print(i[index2][3])
                        #print(i[0][3])
                        sentList[(i[index2][0]-1)] = string.replace(sent," "+str(i[index2][3])+" ", " "+str(i[0][3])+" ")
                        #print(("After ---"+str(sentList)))
        for sent in sentList:
            st = st + sent
        pTokens[index] = st+'\n'
    # for tok in pTokens:
    #     story += tok
    # print(story)
    return pTokens
