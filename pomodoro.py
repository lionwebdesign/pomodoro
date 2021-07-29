import time 
import datetime as dt

import tkinter as tk
from tkinter import messagebox
import os

from pygame import mixer
mixer.init() 

#Main variables
currentTime = dt.datetime.now()
pomodoroTime = 25
timer = pomodoroTime*60
timeDelta = dt.timedelta(0, timer)
futureTime = currentTime + timeDelta
breakTime = 5*60
finalTime = currentTime + dt.timedelta(0, timer + breakTime)

# GUI
root = tk.Tk()
root.withdraw()

messagebox.showinfo("Pomodoro Started!", "\nIts now " + currentTime.strftime('%H:%M:%S') + " hrs. \nTimer set for " + str(pomodoroTime) + " mins.")

totalPomodoros = 0
totalBreaks = 0

def SoundAlert():
    alert = mixer.Sound('assets/bell.wav')
    alert.play()

def PomodoroStart():
    global currentTime
    messagebox.showinfo("Pomodoro Started!", "\nIts now " + currentTime.strftime('%H:%M:%S') + " hrs. \nTimer set for " + str(pomodoroTime) + " mins.")
    currentTime = dt.datetime.now()
    futureTime = currentTime + dt.timedelta(0, timer)
    finalTime = currentTime + dt.timedelta(0, timer + breakTime)


while True:
    if (currentTime < futureTime):
        print('Pomodoro')
    elif (futureTime <= currentTime <= finalTime):
        print('In break')
        if (totalBreaks == 0):
            print('In break')
            for i in range(5):
                SoundAlert()
            print('Break time!')
            totalBreaks += 1
    else:
        print('Finished')
        totalBreaks = 0
        for i in range(10):
            SoundAlert()
        userAnswer = messagebox.askyesno("Pomodoro Finished!", "\n Would you like to statrt another pomodoro?")
        totalPomodoros += 1
        if (userAnswer == True):
            PomodoroStart()
            continue
        elif (userAnswer == False):
            messagebox.showinfo("Pomodoro Finished!", "\nYou completed " + str(totalPomodoros) + " pomodoros today!")
            break
    print("Sleeping")
    time.sleep(20)
    currentTime = dt.datetime.now()
    timeNow = currentTime.strftime("%H:%M:%S")