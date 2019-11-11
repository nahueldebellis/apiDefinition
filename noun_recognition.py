import nltk

def noun(sentence):
    tokens = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(tokens)
    return tags
