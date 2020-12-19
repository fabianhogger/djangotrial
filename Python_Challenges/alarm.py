import time
import sched
import winsound as ws
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

#alarm()
#playsound('Horn.mp3')
"""
localtime=list(time.localtime())
print(type(localtime[3]),type(localtime[4]),type(localtime[5]))
print(localtime)

localtime=list(time.localtime())
if localtime[3]==hour and localtime[4]==min and localtime[5]==sec:
    print("DRING DRING MOTHERFUCKA TIME TO SLAVE AWAY LIKE A NICE CAPITALIST VICTIM")
"""
def set_alarm(alarm_time,wav_file,message):
    s=sched.scheduler(time.time,time.sleep)
    s.enterabs(alarm_time,1,print,argument=(message,))
    a.enterabs(alarm_time,ws.PlaySound,argument=(wav_file,ws.SND_FILENAME))
    print("Alarm set for ",time.asctime(time.localtime(alarm_time))
    s.run()
