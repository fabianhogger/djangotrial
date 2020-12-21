import string
import re




def count_unique(file_path):
    words=[]
    with open(file_path,'r') as file:

        for line in file:
            a=re.split('\W+',line)
            words+=a
    word_count=[(word,words.count(word)) for word in words ]
    print(word_count)
count_unique("file.txt")
