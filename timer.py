# New timer
# Hello!

import time
import os
import sys
import datetime
import signal

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def timer():
    print("Please enter the time you want to set the timer for in minutes: ")
    time_input = int(input())
    time_input = time_input * 60
    print("Timer set for " + str(time_input) + " seconds.")
    time.sleep(time_input)
    print("Time's up!")
    os.system('aplay /home/pi/Downloads/Alarm.wav')
    return

timer()
# print("Hello Branch!")
print ("welcome be new conflict")
## another confict heehh
