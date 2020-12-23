
import random
import regex as re
def pass_gen(nofwords):
    values=[]
    for j in range(1,nofwords):
        value=[]
        for i in range(1,6):
            value.append(random.randint(1,6))
        value=''.join([str(num) for num in value])
        values.append(value)
    print(values)
    password=[]
    with open('diceware.txt','r') as file:
        for val in values:
            for line in file:
                pair=line.split("\t")
                if val==pair[0]:
                    word=re.sub('\n','',pair[1])
                    password.append(word)
    print(password)
pass_gen(5)
