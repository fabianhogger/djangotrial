import time
from playsound import playsound
def alarm():
    while(True):
        try:
            hour=int(input('Set alarm hour please:  '))
            if hour<23 and hour>=0:
                break;
            else:
                print("Invalid hour value")
        except:
            print("Invalid time value")
    while(True):
        try:
            min=int(input('Set alarm min please:  '))
            if min>=0 and min<=59:
                break;
            else:
                print("invalid second value")
        except:
            print("Invalid time value")
    while(True):
        try:
            sec=int(input('Set alarm sec please:  '))
            if sec>=0 and sec<=61:
                break;
            else:
                print("invalid second value")
        except:
            print("Invalid time value")

    while(True):
        localtime=list(time.localtime())
        print(localtime[3],hour)
        if localtime[3]==hour :
            print("check hour")
            if localtime[4]==min and localtime[5]>sec:
                print("DRING DRING MOTHERFUCKA TIME TO SLAVE AWAY LIKE A NICE CAPITALIST VICTIM")
                playsound('Horn.mp3')

alarm()
playsound('Horn.mp3')
"""
localtime=list(time.localtime())
print(type(localtime[3]),type(localtime[4]),type(localtime[5]))
print(localtime)

localtime=list(time.localtime())
if localtime[3]==hour and localtime[4]==min and localtime[5]==sec:
    print("DRING DRING MOTHERFUCKA TIME TO SLAVE AWAY LIKE A NICE CAPITALIST VICTIM")
"""
print(localtime)
