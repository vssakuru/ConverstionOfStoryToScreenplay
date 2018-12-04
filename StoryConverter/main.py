

file = open("./animal.txt", "r+")
s = file.read()
file.write(s.lower())



#re = 'NP : {<DT>?<JJ>*<NN>}'

#chunk = nltk.RegexpParser(re)
#chunk = chunk.parse(preprocessdata(s))
# print(chunk)

#for lab in chunk:
#    if type(lab) == nltk.tree.Tree:
#        print(lab)

