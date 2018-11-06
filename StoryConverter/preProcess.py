import nltk


def preprocessdata(story):
    story = nltk.word_tokenize(story)
    story = nltk.pos_tag(story)
    return story