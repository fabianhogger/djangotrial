

def sort_words(word):
    lowered=word.lower()
    Original=word.split(' ')
    Original.sort()
    ListOfWords=lowered.split(' ')
    ListOfWords.sort()
    final=[]
    for word in ListOfWords:
        for word2 in Original:
            if word==word2.lower():
                final.append(word2)
    return ' '.join(final)

    #return alphabetically
a=sort_words("amesos KATALABA oti einai MALAKAS")
print(a)


def sortWords(word):
    wordlist=word.split()
    wordlist=[w.lower()+w for w in wordlist]
    wordlist.sort()
    wordlist=[w[len(w)//2:] for w in wordlist]
    return ' '.join(wordlist)

b=sortWords("amesos KATALABA oti einai MALAKAS")
print(b)
#amesos einai KATALABA MALAKAS oti
