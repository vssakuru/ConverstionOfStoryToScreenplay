import nltk


def preprocessdata(story):
    story = nltk.word_tokenize(story)
    stopWordsSet = nltk.corpus.stopwords.words('english')
    for words in story:
        if words in stopWordsSet:
            story.remove(words)

    cleantext = ''
    wnl = nltk.stem.WordNetLemmatizer()
    for word in story:
        cleantext += wnl.lemmatize(word) + ' '

    return cleantext
