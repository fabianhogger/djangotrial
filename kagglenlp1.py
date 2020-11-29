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

text_doc = nlp("Glowing review overall, and some really interesting side-by-side "
               "photography tests pitting the iPhone 11 Pro against the "
               "Galaxy Note 10 Plus and last year’s iPhone XS and Google Pixel 3.")
    matches=matcher(text_doc)

print(matches)
"""
[(3766102292120407359, 17, 19), (3766102292120407359, 22, 24), (3766102292120407359, 30, 32), (3766102292120407359, 33, 35)]


The matches here are a tuple of the match id and the positions of the start and end of the phrase.

"""
