from tkinter import *

# Constant
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = NONE
# -------------------------------------------------------------------#
#breakTime
# def break_time(short_br=SHORT_BREAK_MIN*60,long_br = LONG_BREAK_MIN*60):
#     global reps
#     if reps %2 != 0:
#         if short_br % 60 == 0:
#             canvas.itemconfig(canvas_text, text=f"{short_br // 60}:00")
#         elif short_br % 60 < 10:
#             canvas.itemconfig(canvas_text, text=f"{short_br // 60}:0{short_br % 60}")
#         elif short_br % 60 != 0:
#             canvas.itemconfig(canvas_text, text=f"{short_br // 60}:{short_br % 60}")
#         if short_br>0:
#             window.after(100, break_time, short_br - 1)
#         if short_br==0:
#             countdown()
#     else:
#         if long_br % 60 == 0:
#             canvas.itemconfig(canvas_text, text=f"{long_br // 60}:00")
#         elif long_br % 60 < 10:
#             canvas.itemconfig(canvas_text, text=f"{long_br // 60}:0{long_br % 60}")
#         elif long_br % 60 != 0:
#             canvas.itemconfig(canvas_text, text=f"{long_br // 60}:{long_br % 60}")
#         if long_br>0:
#             window.after(100, break_time, long_br - 1)
#         if long_br==0:
#             countdown()

def reset_timer():
    window.after_cancel(timer)
    check_label.config(text="")
    canvas.itemconfig(canvas_text,text="00:00")
    timer_label.config(text="Timer")
    global reps
    reps =0

def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60

    if reps %8==0:
        countdown(long_break)
        timer_label.config(text="Long Break",fg=RED)
    elif reps % 2 ==0:
        countdown(short_break)
        timer_label.config(text="Short Break", fg=RED)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=PINK)

# countdown ---------------------------------------------#
def countdown(count):

    if count%60==0:
        canvas.itemconfig(canvas_text, text=f"{count // 60}:00")
    elif count%60<10:
        canvas.itemconfig(canvas_text, text=f"{count // 60}:0{count % 60}")
    elif count%60!=0:
        canvas.itemconfig(canvas_text, text=f"{count // 60}:{count % 60}")
    if count>0:
        global timer
        timer =window.after(10,countdown,count-1)
    if count==0:
        start_timer()
        mark = ""
        work_sessions = int(reps/2)
        for _ in range(work_sessions):
            mark +="✓"
        check_label.config(text=mark)



window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timer_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))
timer_label.grid(column=1,row=0)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas_text =canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start",bg="white",command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",bg="white",command=reset_timer)
reset_button.grid(column=2,row=2)

check_label = Label(text="",fg=GREEN,bg=YELLOW)
check_label.grid(column=1,row=3)


window.mainloop()