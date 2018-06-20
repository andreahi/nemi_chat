import spacy

nlp = spacy.load('en')
doc = nlp(u"This is a sentence. Dette er noen tall 1 2 23 346 654 436h")
print([(w.text, w.pos_) for w in doc])

