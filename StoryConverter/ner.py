from nltk import word_tokenize
from nltk import pos_tag
from nltk import Tree
from nltk import ne_chunk
from nltk import RegexpParser


from StoryConverter.preprocessdata import preprocessdata

file = open("./Data/Train/uglyDuckling.txt", "r")
fout = open("./Data/Output/output.txt", "w")
s = file.read()

vocab = []

# cleanstory = preprocessdata(s)
# cleanstory = s.lower()
cleanstory = pos_tag(word_tokenize(s))

# Tagging dialogue sentences.

per = 'PERSON: {<DET>?<JJ>+<NNP>+}'
loc = 'LOCATION: {<DT><NN>}'

story = RegexpParser(loc)
c = story.parse(cleanstory)

for words in c:
    if type(words) == Tree:
        print(words)


# NER using NLTK ne_chunk. Displaying all the words which are recognised as an entity.
# cleanstory = ne_chunk(cleanstory)
# for words in cleanstory:
#     if type(words) == Tree and words[0][0] not in vocab:
#         for i in range(0, len(words)):
#             print(words)
#             vocab.append(words[i][0])


# Print the POS tags to output file in-order to get regex

for word in cleanstory:
    fout.write(word[0]+' '+word[1]+'\n')

fout.close()
file.close()

