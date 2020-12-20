import random
def sim(*args):
    table=dict()
    dice_list=[arg for arg in args]
    for i in range(0,1000000):
        num_list=[(random.randint(1,dice)) for dice in dice_list]
        newval=sum(num_list)
        d={str(newval):(table.get(str(newval),0)+1)/1000000}
        table.update(d)

    print(table)
    return table
val1=4
val2=6
val3=6
sim(val1,val2,val3)

from Collections import Counter

def roll_dice(*dice,num_trial=1_000_000):
    counts=Counter()
    for roll in range(num_trials):
        counts=[sum((randint(1,sides) for sides in dice))]+=1
    print('\n Outcome probability\n')
    for outcome in range(len(dice,sum(dice)+1)):
        print('{}\t{:0.2f}%'.format(outcome,counts[outcome]*100/num_trials))
