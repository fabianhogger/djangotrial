import re
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


def load_dict(path):
    f=open(path,"r")
    file=f.read()
    filesplit=file.split("\n")
    newdict=dict()
    keylist=filesplit[0].split(',')
    valuelist=filesplit[1].split(',')
    for i in range(len(keylist)):
        if keylist[i]!='':
            newdict[keylist[i]]=valuelist[i]
    return newdict


def save_dict(dict,path):
    f=open(path,"w")
    keylist=dict.keys()
    valuelist=dict.values()
    for key in keylist:
        f.write(key)
        f.write(",")
    f.write("\n")
    for value in valuelist:
        f.write(str(value))
        f.write(",")
    f.close()
    print("done")


print("THIS IS WHAT COMES OUT WHEN YOU PRINT DICTIONARY",thisdict)
print("DICT KEYS",thisdict.keys)
path='fakelos.txt'
save_dict(thisdict,path)
newdict=load_dict(path)
print(newdict)
