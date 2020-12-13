import re
import pickle


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
path='fakelos.txt'
save_dict(thisdict,path)
newdict=load_dict(path)
print(newdict)
"""
Solution using pickle library for python object serialization

"""

def pickle_dict(dict,path):
    with open(path,"wb") as file:
        pickle.dump(dict,file)
def load_dict(path):
        with open(path,"rb") as file:
            return pickle.load(file)

pickle_dict(thisdict,path)
dictionary=load_dict(path)
print("Pickled dictionary: ",dictionary)
