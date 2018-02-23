'''
Created on Jan 9, 2018

@author: sharina

Resources: GUI Programming with Python from Lynda 
radiobutton resource - 
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/radiobutton.html
checkbutton resource - 
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/checkbutton.html
Tk concepts - https://www.devdungeon.com/content/gui-programming-python
radiobutton discussion - https://stackoverflow.com/questions/35660342/radio-button-values-in-python-tkinter
Serial data and Tkinter - https://stackoverflow.com/questions/10574821/dynamically-updating-tkinter-window-based-on-serial-data
'''

import tkinter as tk
from tkinter import ttk
import random
import time

win = tk.Tk()
win.title("Chords to Play")


'''
Chord Theater Presentation Box
'''
# Container to hold Chord Theater
labelsFrame = ttk.LabelFrame(win, text='Chord Theater')
labelsFrame.grid(column=1, row=0, padx=40, pady=40)
 
# Place labels into the container element
chordPresenter = ttk.Label(labelsFrame, text=" ")
chordPresenter.grid(column=0, row=0, padx=80, pady=50)


'''chord radiobuttons'''
#Container for radiobuttons
chordtype_frame = tk.Frame(win)
chordtype_frame.grid(column=0, row=0)

#RadioControls:
def RadioControls():
    if radVar.get() ==1:
        chordPresenter.configure(text="Let's Play \n Major Chords!")
    elif radVar.get()==2:
        chordPresenter.configure(text="Let's Play \n Minor Chords!")
    elif radVar.get()==3:
        chordPresenter.configure(text="Let's Play \n Major & Minor \n Chords!")
     
#create Radiobuttons 
radVar = tk.IntVar()
radVar.set(1)
   
rad1 = tk.Radiobutton(chordtype_frame, text="Major Chords", variable=radVar, value=1, command=RadioControls)
rad1.grid(column=0, row=0, sticky=tk.W)
   
rad2 = tk.Radiobutton(chordtype_frame, text="Minor Chords", variable=radVar, value=2, command=RadioControls)
rad2.grid(column=0, row=1, sticky=tk.W)
   
rad3 = tk.Radiobutton(chordtype_frame, text="Major & Minor Chords", variable=radVar, value=3, command=RadioControls)
rad3.grid(column=0, row=2, sticky=tk.W)
  
#creates space around each radiobutton by using winfo
for child in chordtype_frame.children.values():
    child.grid_configure(padx=8, pady=9)
    #child.configure(indicatoron=0)


'''Timer, Seconds and Cycles'''
#container for timer and combobox
timerFrame = tk.Frame(win)
timerFrame.grid(column=0, row=1)

#Timer checkbutton
chVarYes = tk.IntVar()
checkbox = tk.Checkbutton(timerFrame, text="Show Chords in a Series?", variable=chVarYes)
checkbox.deselect()
checkbox.grid(column=0, row=0, padx=20)

#Enable Comboboxes
def checkTimer():
    # changes state of chord delay combobox based on checked state
    if chVarYes.get():
        secondsChosen.configure(state="normal")
        #cycleChosen.configure(state="normal")
    else:
        secondsChosen.configure(state="disabled")
        #cycleChosen.configure(state="disabled")
    
# trace the state of the checkbutton
chVarYes.trace('w', lambda unused0, unused1, unused2 : checkTimer())    

#Chord delay (in seconds) using combobox
ttk.Label(timerFrame, text="Delay between chords (in sec)").grid(column=0, row=1)

seconds = tk.IntVar()
secondsChosen = ttk.Combobox(timerFrame, width=5, textvariable=seconds, state='disabled')
secondsChosen['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30)
secondsChosen.grid(column=0, row=2)
secondsChosen.current(3)

#===============================================================================
# #Cycles to choose from
# ttk.Label(timerFrame, text="How Many rounds?").grid(column=1, row=1)
# cycles = tk.IntVar()
# cycleChosen = ttk.Combobox(timerFrame, width=5, textvariable=cycles, state='disabled')
# cycleChosen['values'] = (1, 2, 3, 4, 5)
# cycleChosen.grid(column=1, row=2)
# cycleChosen.current(2)
#===============================================================================

'''Go Button'''

majorChords = ["A Major",
               "B Major",
               "C Major",
               "D Major",
               "E Major",
               "F Major",
               "G Major",
               ]
minorChords = ["a minor",
               "b minor",
               "c minor",
               "d minor",
               "e minor",
               "f minor",
               "g minor"
               ]
majorMinor = majorChords + minorChords


def GoButton(): 
    delay_time = (seconds.get()) * 1000
    major_random = random.choice(majorChords)
    minor_random = random.choice(minorChords)
    both_random = random.choice(majorMinor)
    #cycles_chosen = cycles.get() #3
    
    if radVar.get() == 1 and chVarYes.get():
        chordPresenter.configure(text=major_random)
        win.after(delay_time, GoButton)

    elif radVar.get() == 2 and chVarYes.get():
        chordPresenter.configure(text=minor_random)
        win.after(delay_time, GoButton)
        
    elif radVar.get() == 3 and chVarYes.get():
        chordPresenter.configure(text=both_random)
        win.after(delay_time, GoButton)
         
    elif radVar.get() == 1: 
        chordPresenter.configure(text=major_random)
         
    elif radVar.get() == 2:
        chordPresenter.configure(text=minor_random)
     
    elif radVar.get() == 3:
        chordPresenter.configure(text=both_random)
        
#win.bind("<space>", ...??? )  

''' Exit GUI cleanly'''
def _quit():
    win.quit()
    win.destroy()
    exit()

'''Go and Quit Button frame'''
buttonFrame = ttk.Frame(win)
buttonFrame.grid(column=1, row=1)

actionButton = ttk.Button(buttonFrame, text="Go!", command=GoButton)   
actionButton.grid(column=0, row=0, padx=10, pady=20)

quitButton = ttk.Button(buttonFrame, text='Quit', command=_quit).grid(column=1, row=0, padx=10, pady=20)


win.mainloop()




#===============================================================================
# #Radiobutton creation using a for loop --- format is not right...
# radVar = tk.IntVar()
# radVar.set(1) #initializing the choice, ie Major Chords
# 
# chords = [
#     ("Major Chords", 1),
#     ("Minor Chords", 2),
#     ("Major & Minor Chords", 3),
#     ("Augmented Chords", 4)
#     ]
# 
# def ShowChoice():
#     print(radVar.get())
# 
# tk.Label(chordtype_frame,
#          text="Choose A Category to Practice:", justify = tk.LEFT, padx = 20).grid()
#          
# for val, chord in enumerate(chords):
#     tk.Radiobutton(chordtype_frame, text=chord, padx=20, variable=radVar, command=ShowChoice, value=val).grid(sticky=tk.W)
#===============================================================================