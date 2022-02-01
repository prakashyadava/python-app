from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500,height=300)
window.config(padx=250,pady=150)

input = Entry(width=10)
input.grid(column=1,row=0)


mile_label = Label(text="Miles")
mile_label.grid(column=2,row=0)
mile_label.config(padx=5)

equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)

result_label = Label(text="0",font=("Arial",14,"bold"))
result_label.grid(column=1,row=1)
result_label.config(padx=5)

Km_label = Label(text="Km")
Km_label.grid(column=2,row=1)
Km_label.config(padx=5)

def Reset():
    result_label.config(text="0")
    button.config(text="Calculate", command=Calculate)
def Calculate():
    mile = float(input.get())
    km = 1.609*mile
    km = str(km)
    result_label.config(text=km)
    button.config(text="Reset",command=Reset)
button = Button(text="Calculate",command=Calculate)
button.grid(column=1,row=2)




window.mainloop()