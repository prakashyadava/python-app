from tkinter import *
window = Tk()
window.title("My first Gui Program")
window.minsize(width=900,height=500)

# Label

my_label =  Label(text="I am a label",font=("Arial" ,24,"bold"))
my_label.pack()

# my_label["text"] = "New Text"
my_label.config(text="Hello Prakash")


# button
def reset():

    my_label.config(text="New Text")
    button.config(text="Click Me", command=button_clicked)
def button_clicked():
    msg = input.get()
    my_label.config(text=msg)
    button.config(text="Reset",command=reset)
button  = Button(text="Click Me",command=button_clicked)
button.pack()
# Entry
input = Entry(width=30)
input.pack()

# text
text = Text(height=5,width=30)
# puts cursor in textbox
text.focus()
# Adds some text to begin with
text.insert(END,"Example of multiline text entry")
# Get's current value in textbox ar line 1 and charactor 0
print(text.get("2.0",END))
text.pack()

# spinbox
def spinbox_used():
    print(spinbox.get())
 #get the current value in spinbox

spinbox = Spinbox(from_=0,to =10,width=5,command=spinbox_used)
spinbox.pack()

# scale
# called with current scale value
def scale_used(value):
    print(value)

scale = Scale(from_=0,to=100,command=scale_used)
scale.pack()

# checkbutton
def check_button_used():
    #PRINTS 1 IF ON BUTTON CHECKED,OTHERWISE 0
    print(checked_state.get())

checked_state = IntVar()
check_button = Checkbutton(text="Is On", variable=checked_state,command=check_button_used)
# checked_state.get()
check_button.pack()

# radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radioButton1 = Radiobutton(text="Option-1",value=1,variable=radio_state,command=radio_used)
radioButton2 = Radiobutton(text="Option-2",value=2,variable=radio_state,command=radio_used)
radioButton1.pack()
radioButton2.pack()

# List box
def listbox_used(event):
    print(list.get(list.curselection()))

list = Listbox(height=4)
fruits = ["Apple","Banana","Cherry","DragonFruit"]
for item in fruits:
    list.insert(fruits.index(item),item)
list.bind("<<ListboxSelect>>",listbox_used)
list.pack()
window.mainloop()