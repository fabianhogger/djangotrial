import time

def alarm():

    while(True):
        try:
            x=float(input('Set alarm time please:  '))
            break;
        except:
            print("Invalid time value")

alarm()
