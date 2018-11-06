import nltk

from preprocessdata import preprocessdata

file = open("./Data/Train/uglyDuckling.txt", "r")
f = open("./Data/Output/out.txt", "w")
s = file.read()
story = nltk.sent_tokenize(s)
index = 3
i = -1
vocab = []
# sentence = []
# for sent in story:
#     if index < 2:
#         sentence[i] = sentence[i] + ' ' + sent
#         index = index+1
#     else:
#         index = 0
#         i += 1
#         sentence.append(sent)

rank = []
for sent in story:
    sent = preprocessdata(sent)
    temp = len(vocab)
    for word in sent:
        if word not in vocab:
            vocab.append(word)
    rank.append(len(vocab) - temp)
    if len(vocab) - temp != 0:
        f.write("\n\n\n--------------------NEW SCENE-------------------------\n\n\n")
    f.write(sent + "\n")
f.close()
file.close()
