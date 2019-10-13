
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:12:15 2019

@author: abhijithneilabraham
"""
import random
import time
from playsound import playsound
from tkinter import *
from tkinter import messagebox
def katran():
    
    kat_sounds = ["cat1.mp3", "cat2.mp3", "cat3.mp3", "cat4.mp3", "cat5.mp3", "cat6.mp3"]
    
    print('cat is running through ya keyboard.Press ctrl+c two times to exit')
      
    
    
    
    r = 0.05
    i=1
    while i%2!=0:
        try:
            if i % 5 == 0:
                r = random.uniform(0.01,0.2)
                playsound("cataudios/" + random.choice(kat_sounds))
            a = random.randint(97, 136)
            print(chr(a), end="")        
            time.sleep(r)
    
            i+=2        
        except KeyboardInterrupt:
            print("\n Oops, cat ran through ya keyboard!")
            break
        

window=Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())

#Defining a kitty pic
box=Canvas(window, width=220, height=220)
box.pack()
kitty=PhotoImage(file='[insert directory path here]\\kat_ran\\kat.gif')        
box.create_image(0, 0, anchor=NW, image=kitty)

consentbox=messagebox.askyesno('Hey puss!', 'Do you wanna let your cat run on your keyboard?')

if consentbox==True:
    katran()
    window.withdraw()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    stopbox=messagebox.askokcancel('Calm Down Kitty', 'Press OK to take your cat off the keyboard')

    window.deiconify()
    window.destroy()
    window.quit()

    if stopbox==True:
        exit()
else:
    window.withdraw()
    exit()

window.deiconify()
window.destroy()
window.quit()



