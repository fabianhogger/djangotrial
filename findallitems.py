

def find_items(itemlist,value):
    indexlist=[]
    for item in itemlist:
        print("item, ",item)
        if isinstance(item,list):
            print("isinstance")
            result=find_items(item,value)
            indexlist.append(result)
        else:
            if item==value:
                indexlist.append(1)
            else:
                indexlist.append(0)
    return indexlist

lista=[0,1,2,3,1,[0,2,1],4,5,1]
find_items(lista,1)
