import time
import keyboard
import random
def wait_game():

    flag=False
    print("WELCOME TO THE WAITING GAME")
    target=random.randint(2,4)
    print("Your target time is {} seconds".format(target))
    while True:
        if not keyboard.is_pressed('Enter') and flag:
            flag=False  # making a loop
        elif keyboard.is_pressed('Enter') and not flag:  # if key 'q' is pressed
            result = time.localtime()
            start=time.mktime(result)
            flag=True
            while True:
                if not keyboard.is_pressed('Enter') and flag:
                    flag=False
                elif keyboard.is_pressed("Enter") and not flag:
                    result2 = time.localtime()
                    end=time.mktime(result2)
                    flag=True
                    print("Elapsed time: ",end-start)
                    if (end-start)==target:
                        print("you win!")
                    else:
                        print("LOST ,PRESS ENTER TO TRY AGAIN")
                    break
              # finishing the loop
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
wait_game()
