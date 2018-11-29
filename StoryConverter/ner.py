import glob
from stanfordcorenlp import StanfordCoreNLP

def tokenizeparagraphs(fileName):
    paragraphTokens = []
    for line in f:
        # print(line)
        if line not in ['\n', '\r\n']:
            paragraphTokens.append(line)
        # print(paragraphTokens)
    return paragraphTokens

path = './Data/Train/sinbad.txt'
files = glob.glob(path)
f = open('./Data/Train/sinbad.txt')

nlp = StanfordCoreNLP(r'/home/sai/stanford-corenlp-full-2018-10-05', quiet=True, timeout=100000)
pTokens = tokenizeparagraphs(f)

for para in pTokens:
    p = nlp.coref(para)
    print(p)

