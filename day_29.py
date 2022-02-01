from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import pandas
from csv import writer


#===========================Search=================#
def search():
    find = website_text.get()
    data = pandas.read_csv("my_password.csv")
    data_web = data["Website"].to_list()
    data_user = data["Username"].to_list()
    data_pass = data["Password"].to_list()

    if find in data_web:
        index = data_web.index(find)
        messagebox.showinfo(title=find, message=f"Username :      {data_user[index]}\n"
                                                f"Password :      {data_pass[index]}")
    else:
        messagebox.showinfo(title="oops",message="Data Not Found")




    # if(len(password)>0):
    #     messagebox.showinfo(title=find, message=f"{name}")




#--------------------------------#



# data_dict = {
#     "Website":[],
#     "Email/Username":[],
#     "Password":[]
# }
#=============================Pssword Generator===========================#
def generate_password():
    lower_case_charactors = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    symbols = ['!', '@', '#', '$', '%', '^', '&', "*", '-', '_', '(', ')', '=', '+', '/', '{', '}', '[', ']', '"', "'",
               '\\', '|', '/', '?', '<', '>', ',', '.', ':', ';']
    upper_case_charactors = []
    for i in range(0, 26):
        upper_case_charactors.append(lower_case_charactors[i].upper())
    letters = lower_case_charactors + upper_case_charactors
    len_letters = random.randint(8,10)
    len_symbols = random.randint(2,4)
    len_numbers = random.randint(2,4)
    password_letters = [random.choice(letters) for n in range(len_letters)]
    password_symbols = [random.choice(symbols) for n in range(len_symbols)]
    password_numbers = [str(random.choice(numbers)) for n in range(len_numbers)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    final_password = "".join(password_list)
    pyperclip.copy(final_password)

    password_text.delete(0,END)
    password_text.insert(END,final_password)
#-------------------------------------------------------------------------#

def save():
    data_list = []

    website = website_text.get()
    email = email_text.get()
    password = password_text.get()
    sahi_hai = True
    is_ok = False
    if(len(website)==0 or len(email)==0 or len(password)==0):
        sahi_hai = False
        messagebox.showinfo(title="oops",message="Please make sure you haven't left any field empty!!!")
    if(sahi_hai):
        is_ok = messagebox.askokcancel(title="Confirmation Dialog", message=f"Website:{website}\n"
                                                             f"Email:{email}\n"
                                                             f"Password:{password}\n"
                                                             f"Click Ok if you want to save")

    if is_ok:
        data_list.append(website)
        data_list.append(email)
        data_list.append(password)
        website_text.delete(0, END)
        password_text.delete(0, END)
        with open('my_password.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(data_list)
            f_object.close()





window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200,width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:" )
website_label.grid(column=0,row=1,pady=10)

website_text = Entry(width=35)
website_text.focus()
website_text.grid(column=1,row=1,columnspan=2,pady=10)

search_button = Button(text="Search",command=search)
search_button.grid(column=2,row=1)

email_label = Label(text="Email/Username:" )
email_label.grid(column=0,row=2,pady=10)

email_text = Entry(width=35)
email_text.insert(END,"duke12prakash@gmail.com")
email_text.grid(column=1,row=2,columnspan=2,pady=10)

password_label = Label(text="Password:" )
password_label.grid(column=0,row=3,pady=10)

password_text = Entry(width=25)
password_text.grid(column=1,row=3,pady=10)

generate_pass_button = Button(text="Generate Password",bg="white",width=14,command=generate_password)
generate_pass_button.grid(column=2,row=3,pady=10)

add_button = Button(text="Add",bg="white",width=35,command=save)
add_button.grid(column=1,row=4,columnspan=2,pady=10)




window.mainloop()