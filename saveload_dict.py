import re
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict.keys())
print(thisdict.values())
def load_dict(path):
    f=open(path,"r")
    file=f.read()
    filesplit=file.split("\n")
    dict=dict()
    
def save_dict(dict,path):
    f=open(path,"w")
    keylist=dict.keys()
    list(keylist)
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

path='fakelos.txt'
save_dict(thisdict,path)
load_dict(path)
