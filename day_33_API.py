import requests

# from tkinter import *
# quote = []
# def get_quote():
#     response = requests.get(url="https://api.kanye.rest")
#     data = response.json()
#     quote = data["quote"]
#     canvas.itemconfig(canvas_text,text=quote,fill="white")
# window = Tk()
# window.title("Kanye Quotes")
# window.minsize(width=600,height=800)
# window.config(padx=15,pady=15,bg="pink")
#
# canvas = Canvas(width=300,height=414,bg="pink",highlightthickness=0)
# back_img = PhotoImage(file="day_33_bg.png")
# canvas.create_image(150,212,image=back_img)
#
# canvas_text = canvas.create_text(150,207,text=quote,width=250,font=("Arial",25,"bold"),fill="white")
# canvas.place(x=100,y=80)
#
#
# kanye_img = PhotoImage(file="day_33_kanye.png")
# kanye_button = Button(image=kanye_img,highlightthickness=0,command=get_quote)
#
# kanye_button.place(x=200,y=500)
# get_quote()
#
# window.mainloop()

My_lat = 26.206300
My_long = 83.970600

parameters = {
    "lat": My_lat,
    "lng": My_long
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
print(data)
