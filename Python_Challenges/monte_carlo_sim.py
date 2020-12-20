import pandas
import random
def sim(*args):
    max_value=sum(args)
    table=dict()
    dice_list=[arg for arg in args]
    for i in range(0,1000000):
        num_list=[(random.randint(1,dice)) for dice in dice_list]
        newval=sum(num_list)
        #print("new sum ",newval)
        #print(table.get(str(newval),1))
        d={str(newval):table.get(str(newval),0)+1}
        #print(d)
        table.update(d)

    print(table)
val1=4
val2=6
val3=6
sim(val1,val2,val3)
