

def sort_words(word):
    lowered=word.lower()
    Original=word.split(' ')
    Original.sort()
    print(Original)
    ListOfWords=lowered.split(' ')
    ListOfWords.sort()
    print(ListOfWords)
    final=[]
    for word in ListOfWords:
        for word2 in Original:
            if word==word2.lower():
                final.append(word2)
    print(final)
    return ListOfWords

    #return alphabetically
a=sortwords("amesos KATALABA oti einai MALAKAS")
