from nltk.tokenize import TextTilingTokenizer

file = open("./Data/Train/theGooseGirl.txt", "r")
f = open("./Data/Output/textTilingOutput1.txt", "w")
s = file.read()

ttt = TextTilingTokenizer(20, 10, 0, None, [0], 2, 1, 1, False)

tokens = ttt.tokenize(s)
for token in tokens:
    #paragraph = token.replace("\n", " ")
    f.write("\n\n---SCENE----\n\n")
    f.write(token)
    f.write("\n")