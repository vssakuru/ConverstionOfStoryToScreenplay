from preProcess import preprocessdata
import nltk


file = open("./Data/Train/sleepingBeauty.txt", "r")
s = file.read()
chunk = nltk.ne_chunk(preprocessdata(s))

#re = 'NP : {<DT>?<JJ>*<NN>}'

#chunk = nltk.RegexpParser(re)
#chunk = chunk.parse(preprocessdata(s))
# print(chunk)

#for lab in chunk:
#    if type(lab) == nltk.tree.Tree:
#        print(lab)

