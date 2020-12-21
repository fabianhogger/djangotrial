import re

def count_unique(file_path):
    words=[]
    with open(file_path,'r') as file:
        for line in file:
            a=re.split('\W+',line.lower())
            words+=a
    word_count=[(word,words.count(word)) for word in words ]
    res=sorted(word_count,key=lambda x:x[1],reverse=True)
    return res[:20]

res=count_unique("file.txt")
print(res)
