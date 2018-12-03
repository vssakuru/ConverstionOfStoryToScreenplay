from stanfordcorenlp import StanfordCoreNLP
from nltk import sent_tokenize

def tokenizeparagraphs(fileName):
    paragraphTokens = []
    for line in fileName:
        # print(line)
        if line not in ['\n', '\r\n']:
            paragraphTokens.append(line)
        # print(paragraphTokens)
    return paragraphTokens


pronouns = ["he", "He", "she", "She", "his", "His", "her", "Her"]

def preprocessing(file, nlp):
    story = ""
    pTokens = tokenizeparagraphs(file)
    for index in range(len(pTokens)):
        if index == 0:
            p = nlp.coref(pTokens[0])

        else:
            pTokens[index-1] = pTokens[index-1] + pTokens[index]
            p = nlp.coref(pTokens[index-1])
        sentList = sent_tokenize(pTokens[index])
        st = ""
        for i in p:
            for index2 in range(1, len(i)):
                if i[index2][3] in pronouns:
                    if i[index2][0]-1 < len(sentList):
                        sent = sentList[i[index2][0]-1]
                        sentList[i[index2][0] - 1] = sent.replace(" "+i[index2][3]+" ", " "+i[0][3]+" ")
        for sent in sentList:
            st = st + sent
        pTokens[index] = st
    for tok in pTokens:
        story += tok
    # print(story)
    return pTokens
