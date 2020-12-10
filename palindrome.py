import re

def is_palindrome(word):
    word=re.sub('\W+','', word)
    letterlist=[letter for letter in word]
    letterlist.reverse()
    drow=''.join(letterlist)
    return drow==word
a=is_palindrome("Lev-e l")
print(a)



def is_pal(phrase):
    forwards=''.join(re.findall(r'[a-z]+',phrase.lower()))
    backwards=forwards[::-1]
    return backwards==forwards
b=is_pal("Lev-e l")
print(b)
