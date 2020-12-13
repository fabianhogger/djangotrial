import re
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964.0
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
            if re.search("class 'str'",valuelist[i]):
                value=re.split(" type",valuelist[i])
                newdict[keylist[i]]=value[0]
            elif re.search("class 'int'",valuelist[i]):
                value=re.split(" type",valuelist[i])
                newdict[keylist[i]]=int(value[0])
            elif re.search("class 'float'",valuelist[i]):
                value=re.split(" type",valuelist[i])
                newdict[keylist[i]]=float(value[0])
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
        f.write(" type:{}".format(type(value)))
        f.write(",")
    f.close()

print("THIS IS WHAT COMES OUT WHEN YOU PRINT DICTIONARY",thisdict)
print("DICT KEYS",thisdict.keys())
print("DICT VALUES",thisdict.values())
path='fakelos.txt'
save_dict(thisdict,path)
newdict=load_dict(path)
print(newdict)
