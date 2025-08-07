import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# Reset the full program and back to initial position
def reset():
    window.after_cancel(timer) #Stop the loop and set initial position
    text_label.config(text="Timer") #Initial title label
    canvas.itemconfig(timer_text, text="00:00")#Initial timer_text label
    check_mark.config()
    global reps
    reps = 0


def start_count():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0: #Check repeat 8 times and set count as long break
        cound_down(long_break)
        text_label.config(text="Break", fg=RED)
    elif reps % 2 == 0: #Check if repeat even time and set count as short break
        cound_down(short_break)
        text_label.config(text="Break", fg=PINK)
    else:  #Check if repeat odd time and set count as working time
        cound_down(work_time)
        text_label.config(text="Work", fg=GREEN)

def cound_down(count):
    count_min = math.floor(count / 60) #Convert count second into min using floor which take lower integer
    count_sec = count % 60 #Rest of sec
    if count_min < 10: #Check if min less than 10 then it will show 2 digit mean that digit with 0 infont
        count_min = f"0{count_min}"
    if count_sec < 10:  #Check if sec less than 10 then it will show 2 digit mean that digit with 0 infont
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}") #Send the text on canvas and show the change
    if count > 0:
        global timer
        timer = window.after(1000, cound_down, count - 1) #Creat the count-down with function itself
    else:
        start_count() #When the loop once end it will call start count again and print check once after completing 2 loop
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "✔"
        check_mark.config(text=mark)

#Configure window
window = Tk()
title = window.title("Pomodoro Game")
window.config(padx=100, pady=50, background=YELLOW)

#Create canvas so that rewrite on image
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)

#Take image into canvas
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= image)

#Crate text on image
timer_text = canvas.create_text(100, 112, text="00:00", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)
#Create timer title
text_label = Label(text="Timer", background=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
text_label.grid(row=0, column=1)

#Create start button
start_button = Button(text="Start", highlightthickness=0, command=start_count)
start_button.grid(row=2, column=0)

#Create reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

#Create blank label which used as check mark later
check_mark = Label(fg=GREEN, background=YELLOW)
check_mark.grid(row=3, column=1)


window.mainloop()