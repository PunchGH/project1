
from tkinter import *
import random as rd
import time


window = Tk()


def setting_num(s_n1,b_n1,s_n2,b_n2,opt):
        
    
   
    global ans
    global num_1
    global num_2

    num_1 = rd.randrange(s_n1,b_n1)
    num_2 = rd.randrange(s_n2,b_n2)
        
    
    if num_1 < num_2:

        backup = num_1

        num_1 = num_2
        num_2 = backup
        
    
    if opt == 1:
        
        
        ans = num_1 + num_2

        


        
    
    elif opt == 2:
                
        
        ans = num_1 - num_2 
        
    
    elif opt == 3:
                
        
        ans = num_1 * num_2 
    
    
    elif opt == 4:
                
        rnd_c = rd.choice([1,2])
        
        
        if rnd_c == 1:

            ans_backup = num_1

            ans = num_1 * num_2

            num_1 = ans

            num_2 = num_2
            
           
            
            ans = ans_backup

        elif rnd_c == 2:

            ans_backup = num_2

            ans = num_1 * num_2

            num_2 = ans

            num_1 = num_1
            
            
            
            ans = ans_backup
        






class color_font():
    
    bg_color = "grey3"
    tx_color = "green2"
    font = ("Great Vibes", 15)




        
        
    


class quiz_setup(color_font):

    global user_name
    global user_score

    user_name = None
    user_score = None
    
    
    def quiz_win():

        
        global exam_window
        
        exam_window = Toplevel(window)
        exam_window.configure(bg=color_font.bg_color)
    
    
        
        
        
        
        Label(exam_window,text="You get score every question. Answer the following : ",fg = color_font.tx_color, bg= color_font.bg_color,font=color_font.font).grid(column=1,row=0)

        exam_window.grab_set()

    

        



def countdown(count):
         
    label['text'] = count

    if count > 0:
       
        exam_window.after(1000, countdown, count-1)

    else:

        exam_window.destroy()

        time_up_win = Toplevel(window)

        time_up_win.configure(bg = color_font.bg_color)

        Label(time_up_win,text="Times ",fg = color_font.tx_color, bg= color_font.bg_color,font=color_font.font).grid(column=0,row=0)

        Label(time_up_win,text="Up ",fg = color_font.tx_color, bg= color_font.bg_color,font=color_font.font).grid(row = 1,column=0)


        time_up_win.grab_set()

def coundown_display(time):

        global label
        label = Label(exam_window,fg = color_font.tx_color,bg= color_font.bg_color,font=("Great Vibes" ,40))
        
        label.grid(column=0,row=0)


        
        countdown(time)





global score
score = 0

def QuesAndAns(test_level):


        
    opt = ""
    
    int(test_level)

        
        
        
    if test_level == 1:

        setting_num(101,999,101,999,1)
        opt = '+'
        
    elif test_level == 2:

        choice = rd.randrange(1,2)

        setting_num(101,999,101,999,choice)

        if choice == 1:

            opt = '+'

        
        elif choice == 2:

            opt = '-'
        
        
    elif test_level == 3:

        setting_num(11,99,2,9,3)
        opt = 'x'
        
        
    elif test_level == 4:

        choice = rd.randrange(3,4)

        setting_num(11,99,2,9,choice) 

        if choice == 3:

           opt = "x"

        elif choice == 4:

            opt = "/"

        
    elif test_level == 5:

        choice = rd.randrange(1,4)  

        if choice == 1:

            setting_num(101,999,101,999,choice)
            opt = '+'

        if choice == 2:

            setting_num(101,999,101,999,choice)
            opt = "-"

        if choice == 3:

            setting_num(11,99,2,9,choice)
            opt = 'x'

        if choice == 4:

            setting_num(11,99,2,9,choice)
            opt = '/'


    global display_question

    display_question = str(num_1) + " " + str(opt) + " " + str(num_2) + " :"

    Label(exam_window,text=display_question,bg = color_font.bg_color,fg=color_font.tx_color,font=("Great Vibes", 30)).grid(column=0,row=1)
    
    user_ans = Entry(exam_window,fg=color_font.tx_color,bg=color_font.bg_color,font=('Great Vibes', 30))
    
    user_ans.grid(column=1,row=1)
    

    
    def submit_button():
        


        if str(ans) == user_ans.get():
            
           

            score = score + 1
            
            correct_window = Toplevel(window)
            
            correct_window.configure(bg=color_font.bg_color)
            
            Label(correct_window,text="Correct",bg=color_font.bg_color,fg=color_font.tx_color,font=('Great Vibes',30)).grid(row=0,column=0)
    
            correct_window.grab_set()

        else:

            
            
            score = score - 1
            
            incorrect_window = Toplevel(window)
            
            incorrect_window.configure(bg=color_font.bg_color)
            
            Label(incorrect_window,text="Incorrect,score : " + str(score),bg=color_font.bg_color,fg=color_font.tx_color,font=("Great Vibes", 30)).grid(row=0,column=0)

            exit = Button(incorrect_window,text="Ok,let's go",bg=color_font.bg_color,fg=color_font.tx_color,font=('Great Vibes',25),command=incorrect_window.destroy())
            
            incorrect_window.grab_set()

        QuesAndAns(test_level)

        
    
    submit_button = Button(exam_window,text="submit",bg=color_font.bg_color,fg=color_font.tx_color,font=("Great Vibes", 20),command=submit_button)
    
    submit_button.grid(row=1,column=2)


class tests(quiz_setup):
    
    def test_level_1():
    
        quiz_setup.quiz_win()
        
        coundown_display(90)

        QuesAndAns(1)

    
        
        
        

        
    def test_level_2():
    
        quiz_setup.quiz_win()

        coundown_display(60)

        QuesAndAns(2)

        


        
        

    def test_level_3():
    
        quiz_setup.quiz_win()
        
        coundown_display(90)

        QuesAndAns(3)  
        
        


    def test_level_4():
    
        quiz_setup.quiz_win()

        coundown_display(60)
         

        QuesAndAns(4)        
    
 
 

    def test_level_5():
        
        
        quiz_setup.quiz_win()
        
 
        coundown_display(40)

        QuesAndAns(5)





bg_cl = color_font.bg_color
window.configure(bg=bg_cl)
Font_label = ("Great Vibes", 15)
Font_text = ("Great Vibes", 15)



heading = Label(window,text="Hello there, Welcome to this math test.(This Gui will not attack ur eye)",font=Font_label,fg=color_font.tx_color,bg=bg_cl).grid(column=0,row=0)
label_1 = Label(window,text="We have many levels that u can choose.",font=Font_text,fg=color_font.tx_color,bg=bg_cl).grid(column=0,row=2)
label_1 = Label(window,text="level 1 is the most easy one and level 5 is the hardest one:",font=Font_text,fg=color_font.tx_color,bg=bg_cl).grid(column=1,row=2)



lv_1_button = Button(window,text="level 1 click here",font=Font_text,fg=color_font.tx_color,bg=bg_cl,command=tests.test_level_1).grid(column=0,row=4)
lv_2_button = Button(window,text="level 2 click here",font=Font_text,fg=color_font.tx_color,bg=bg_cl,command=tests.test_level_2).grid(column=0,row=5)
lv_3_button = Button(window,text="level 3 click here",font=Font_text,fg=color_font.tx_color,bg=bg_cl,command=tests.test_level_3).grid(column=0,row=6)
lv_4_button = Button(window,text="level 4 click here",font=Font_text,fg=color_font.tx_color,bg=bg_cl,command=tests.test_level_4).grid(column=0,row=7)
lv_5_button = Button(window,text="level 5 click here",font=Font_text,fg=color_font.tx_color,bg=bg_cl,command=tests.test_level_5).grid(column=0,row=8)



Label(window,text="contains + and - with 2 digits number.",font=Font_text,fg=color_font.tx_color,bg=bg_cl).grid(column=1,row=4)
Label(window,text="contains + and - with 3 digits number.",font=Font_text,fg=color_font.tx_color,bg=bg_cl).grid(column=1,row=5)
Label(window,text="contains * with 2 and 1 digits number.",font=Font_text,fg=color_font.tx_color,bg=bg_cl).grid(column=1,row=6)
Label(window,text="contains *  and / with 2 and 1 digits number.",font=Font_text,fg=color_font.tx_color,bg=bg_cl).grid(column=1,row=7)
Label(window,text="contains level 1 and 4",font=Font_text,fg=color_font.tx_color,bg=bg_cl).grid(column=1,row=8)

window.mainloop()