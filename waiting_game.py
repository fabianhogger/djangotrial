import time
import keyboard
flag=False
print("WELCOME TO THE WAITING GAME")
print("Press enter to start and than press again to win,you win if you press after 4 seconds")
while True:
    if not keyboard.is_pressed('Enter') and flag:
        flag=False  # making a loop
    elif keyboard.is_pressed('Enter') and not flag:  # if key 'q' is pressed
        result = time.localtime()
        start=time.mktime(result)
        flag=True
        print("1st LOOP")
        while True:
            if not keyboard.is_pressed('Enter') and flag:
                flag=False
                print("1st if")
            elif keyboard.is_pressed("Enter") and not flag:
                result2 = time.localtime()
                end=time.mktime(result2)
                flag=True
                print("Elapsed time: ",end-start)
                if (end-start)==4.0 :
                    print("you win!")
                else:
                    print("LOST ,PRESS ENTER TO TRY AGAIN")
                print("2nd if ")
                break
          # finishing the loop
import random

def waiting_game():
    target=random.randint(2,4)
    print("Your target time is {} seconds".format(target))
    input("---Press Enter to Begin---")
    start=time.perf_counter()
    input("---Press again after {} seconds---".format(target))
    elapsed=time.perf_counter()-start
    print("Elapsed time is {} seconds".format(elapsed))
    if elapsed==target:
        print("Unbelievable !Perfect Timing!")
    elif elapsed<target:
        print("{} seconds too fast".format(target-elapsed))
    else:
        print("{} seconds too slow".format(elapsed-target))
