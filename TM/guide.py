from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

doc1 = "Sugar is bad to consume. My sister likes to have sugar, but not my father."
doc2 = "My father spends a lot of time driving my sister around to dance practice."
doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
doc4 = "Sometimes I feel pressure to perform well at school, but my father never seems to drive my sister to do better."
doc5 = "Health experts say that Sugar is not good for your lifestyle."

# compile documents
doc_complete = [doc1, doc2, doc3, doc4, doc5]


stop=set(stopwords.words('english'))
exclude=set(string.punctuation)
lemma=WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized
doc_clean = [clean(doc).split() for doc in doc_complete]
print(doc_clean)
"""
[['sugar', 'bad', 'consume', 'sister', 'like', 'sugar', 'father'],
['father', 'spends', 'lot', 'time', 'driving', 'sister', 'around', 'dance', 'practice'],
['doctor', 'suggest', 'driving', 'may', 'cause', 'increased', 'stress', 'blood', 'pressure'],
['sometimes','feel','pressure','perform','well','school','father','never','seems','drive','sister','better'],
 ['health', 'expert', 'say', 'sugar', 'good', 'lifestyle']]
"""
import gensim
from gensim import corpora
#Creating the term dictionary of our courpus, where every unique term is assigned an index.
dictionary = corpora.Dictionary(doc_clean)
print(dictionary.values())
"""ValuesView(<gensim.corpora.dictionary.Dictionary object at 0x00000286394A6BC8>)
[(0, '0.079*"driving" + 0.045*"suggest" + 0.045*"cause"'),
 (1, '0.076*"sister" + 0.076*"father" + 0.076*"sugar"'),
 (2, '0.076*"sugar" + 0.075*"lifestyle" + 0.075*"health"')]"""
# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

print(ldamodel.print_topics(num_topics=3, num_words=3))
"""
[(0, '0.045*"pressure" + 0.045*"father" + 0.045*"sister"'),
(1, '0.029*"sugar" + 0.029*"sister" + 0.029*"father"'),
 (2, '0.064*"sugar" + 0.064*"sister" + 0.064*"father"')]
"""
