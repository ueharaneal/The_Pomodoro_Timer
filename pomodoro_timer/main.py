from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    timer.config(text = "Timer" )
    checkmark.config(text= "")
    global reps 
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec  = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    
    if reps == 8:
        title_label.config(text = "Break", fg = RED)
        count_timer(long_break_sec)
        
    elif reps % 2 == 0:
        title_label.config(text = "Break", fg = PINK)
        count_timer(short_break_sec)
        
    else:
        title_label.config(text = "Work", fg = GREEN)
        count_timer(work_sec)
        
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_timer(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_timer, count -1 )
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"

        checkmark.config(text = mark)



# ---------------------------- UI SETUP ------------ ------------------- #

window = Tk()
window.title("Pomorodo")
window.config(padx = 100,pady = 50, bg = YELLOW)



#in the after you are able to place as many args as you want 


canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_image = PhotoImage(file = "pomodoro-start/tomato.png")
canvas.create_image(100, 112, image = tomato_image )
canvas.grid(column =1 , row = 1)

timer_text = canvas.create_text(100, 130, text = "00:00",fill = "white" ,font = (FONT_NAME, 30, "bold"))

title_label = Label(text = "Timer", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 35, "bold"))
title_label.grid(column = 1 , row = 0)



start_button = Button(text = "Start", command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button =Button(text = "Reset", command = reset_timer)
reset_button.grid(column = 2, row = 2)

checkmark = Label(text = "", fg = GREEN, bg = YELLOW)
checkmark.grid(column = 1, row = 3)




window.mainloop()