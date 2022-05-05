from tkinter import *
import math
def leftclick(event):
    
    bmi = float(Textbox_weight.get()) / math.pow(float(Textbox_height.get())/100,2)
    
    levels = ["under level","normal level","over level","obersity"]
    
    
    if bmi <= 18.5:
        levelresult.configure(text = levels[0])   
    
    elif bmi <= 25.0:             
        levelresult.configure(text = levels[1])
    
    elif bmi < 30.0:
        levelresult.configure(text = levels[2])
    
    else:
        levelresult.configure(text = levels[3])
    
    print(float(Textbox_weight.get()) / math.pow(float(Textbox_height.get())/100,2))
    labelresult.configure(text = int(float(Textbox_weight.get()) / math.pow(float(Textbox_height.get())/100,2)))
        


Main = Tk()

labelheight = Label(Main,text="Height (cm.)")    

labelheight.grid(row=0,column = 0)

Textbox_height = Entry(Main)

Textbox_height.grid(row = 0,column = 1)

labelweight = Label(Main,text="weight (Kg.)")

labelweight.grid(row=1,column = 0)    

Textbox_weight = Entry(Main)

Textbox_weight.grid(row = 1,column = 1)

calculatebutton = Button(Main,text = "calculate")

calculatebutton.bind('<Button-1>',leftclick)

calculatebutton.grid(row = 2,column = 0)

labelresult = Label(Main,text="result")    
levelresult = Label(Main,text = "level")

labelresult.grid(row=2,column = 1   )
levelresult.grid(row=2,column = 2)

Main.mainloop()