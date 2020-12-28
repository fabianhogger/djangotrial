

def find_items(itemlist,value):
    indexlist=[]
    for item in itemlist:
        if isinstance(item,list):
            result=find_items(item,value)
            indexlist.append(result)
        elif item==value:
            indexlist.append(1)
        else:
                indexlist.append(0)
    print(itemlist)
    print(indexlist)
    print("ENDS")
    return indexlist

lista=[0,1,2,3,1,[0,2,1],4,5,1]
find_items(lista,2)


def index_all(lista,item):
    indices=list()
    for i in range(len(lista)):
        if lista[i]==item:
            indices.append([i])
        elif isinstance(lista[i],list):
            for index in index_all(lista[i],item):
                indices.append([i]+index)
    print(lista)
    print(indices)
    return indices


index_all(lista,2)
