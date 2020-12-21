import re

def count_unique(file_path):
    words=[]
    with open(file_path,'r') as file:
        for line in file:
            a=re.split('\W+',line.lower())
            words+=a
    word_count=[(word,words.count(word)) for word in words if word !='']
    res=sorted(word_count,key=lambda x:x[1],reverse=True)
    return res[:20]

res=count_unique("file.txt")
print(res)


from collections import Counter

def count_words(path):
    with open(path,encoding='UTF-8') as file:
        all_words=re.findall(r'[0-9a-zA-Z-]+',file.read())
        all_words=[word.upper() for word in all_words]
        print('\nTotal words:',len(all_words))

        word_counts=Counter()
        for word in  all_words:
            word_counts[word]+=1
        print("\n Top 20 words")
        for word in word_counts.most_common(20):
            print(word[0],'\t',word[1])

count_words("file.txt")
