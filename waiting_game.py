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
