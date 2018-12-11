from nltk.tokenize import TextTilingTokenizer
import glob
import os

path = './Data/Test/*.txt'
files=glob.glob(path)
for name in files:

    with open(name) as file:
        head, tail = os.path.split(name)
        f = open("./Data/Output/TextTiling/Test/"+tail, "w")
        s = file.read()

        ttt = TextTilingTokenizer(20, 10, 0, None, [0], 2, 1, 1, False)

        tokens = ttt.tokenize(s)
        for token in tokens:
            #paragraph = token.replace("\n", " ")
            f.write("\n\n---SCENE----\n\n")
            f.write(token)
            f.write("\n")