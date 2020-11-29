import spacy
nlp=spacy.load('en_core_web_sm')


doc=nlp("Tea is healthy and calming, don't you think?")#doc object
for token in doc:
    print(token)
#important ones are token.lemma_ and token.is_stop
print(f"Token \t\tLemma \t\tStopword".format('Token', 'Lemma', 'Stopword'))
print("-"*40)
for token in doc:
    print(f"{str(token)}\t\t{token.lemma_}\t\t{token.is_stop}")
#PREPROCESSING

#PATTERN MATCHING

from spacy.matcher import PhraseMatcher
matcher=PhraseMatcher(nlp.vocab,attr='LOWER')#to match a list of terms, it's easier and more efficient to use PhraseMatcher
#The phrase matcher needs the patterns as document objects. The easiest way to get these is with a list comprehension using the nlp model.
terms=['Galaxy Note', 'iPhone 11', 'iPhone XS', 'Google Pixel']
patterns=[nlp(text) for text in terms]
matcher.add("TerminologyList",patterns)
