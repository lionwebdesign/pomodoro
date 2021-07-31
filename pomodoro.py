import time 
import datetime as dt
import tkinter as tk
from tkinter import messagebox
import os
from pygame import mixer
mixer.init() 

class POMODORO:
    def __init__(self):
        #Main variables
        self.currentTime = dt.datetime.now()
        self.pomodoroTime = 25
        self.timer = self.pomodoroTime*60
        self.timeDelta = dt.timedelta(0, self.timer)
        self.futureTime = self.currentTime + self.timeDelta
        self.breakTime = 5*60
        self.finalTime = self.currentTime + dt.timedelta(0, self.timer + self.breakTime)
        self.totalPomodoros = 0
        self.totalBreaks = 0

    def SoundAlert(self):
        self.alert = mixer.Sound('assets/bell.wav')
        self.alert.play()

    def PomodoroStart(self):
        messagebox.showinfo("Pomodoro Started!", "\nIts now " + self.currentTime.strftime('%H:%M:%S') + " hrs. \nTimer set for " + str(self.pomodoroTime) + " mins.")
        self.currentTime = dt.datetime.now()
        self.futureTime = self.currentTime + dt.timedelta(0, self.timer)
        self.finalTime = self.currentTime + dt.timedelta(0, self.timer + self.breakTime)
    
    def pomodoroWorking(self):
        messagebox.showinfo("Pomodoro Started!", "\nIts now " + self.currentTime.strftime('%H:%M:%S') + " hrs. \nTimer set for " + str(self.pomodoroTime) + " mins.")

        while True:
            if (self.currentTime < self.futureTime):
                print('Pomodoro')
            elif (self.futureTime <= self.currentTime <= self.finalTime):
                print('In break')
                if (self.totalBreaks == 0):
                    print('In break')
                    for i in range(5):
                        self.SoundAlert()
                    print('Break time!')
                    self.totalBreaks += 1
            else:
                print('Finished')
                self.totalBreaks = 0
                for i in range(10):
                    self.SoundAlert()
                userAnswer = messagebox.askyesno("Pomodoro Finished!", "\n Would you like to statrt another pomodoro?")
                self.totalPomodoros += 1
                if (userAnswer == True):
                    self.PomodoroStart()
                    continue
                else:
                    messagebox.showinfo("Pomodoro Finished!", "\nYou completed " + str(self.totalPomodoros) + " pomodoros today!")
                    break
            print("Sleeping")
            time.sleep(20)
            self.currentTime = dt.datetime.now()
            timeNow = self.currentTime.strftime("%H:%M:%S")

    # GUI
    root = tk.Tk()
    root.withdraw()

p = POMODORO()
p.pomodoroWorking()