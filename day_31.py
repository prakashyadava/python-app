from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
current_card = {}
data_dict = {}
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("french_words.csv")
    data_dict = data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")



def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    current_word = current_card["French"]

    canvas.itemconfig(card_word,text=current_word,fill="black")
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_background,image=front_img)
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_background,image=back_img)
    canvas.itemconfig(card_title,text="English",fill="white")
    current_word = current_card["English"]
    canvas.itemconfig(card_word,text=current_word,fill="white")
flip_timer = window.after(3000,func=flip_card)

def known():
    data_dict.remove(current_card)
    to_learn = pandas.DataFrame(data_dict)
    to_learn.to_csv("words_to_learn.csv",index=False)
    next_card()

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
back_img = PhotoImage(file="card_back.png")
front_img = PhotoImage(file="card_front.png")
card_background = canvas.create_image(400,263,image=front_img)
card_title = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Arial",40,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)

right_img = PhotoImage(file="right.png")
right_button = Button(image=right_img, highlightthickness=0,command=known)
right_button.grid(column=1,row=1)
next_card()

window.mainloop()