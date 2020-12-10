import re

def is_palindrome(word):
    word=re.sub('\W+','', word)
    letterlist=[letter for letter in word]
    letterlist.reverse()
    drow=''.join(letterlist)
    if drow==word:
        return True
    else:
        return False
a=is_palindrome("lev-e l")
print(a)
