import smtplib
import datetime as dt
import random
import pandas
PLACEHOLDER = "[NAME]"
# data = pandas.read_csv("birthdays.csv")
# data_dict = data.to_dict(orient="records")
# month_list =  data["month"].to_list()
# day_list =  data["day"].to_list()
#

def send_msg(my_message,to):
    my_email = "Your Email id"
    password = "Your passswword"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # these 2 lines secure the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to,
                            msg=f"Subject:Happy Birthday\n\n {my_message}")
        connection.close()
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# index = [day_list.index(day) for mon in month_list if mon==month and month_list.index(mon)== day_list.index(day) ]
#
# print(index)
#
#
#
txt_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
#
# name_list = []
# for location in index:
#     with open(random.choice(txt_list)) as txt:
#         txt_data = txt.read()
#     name =data_dict[location]["name"]
#     my_message = txt_data.replace(PLACEHOLDER,name)
#     send_msg(my_message)
#
#
#
#
#
#

today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    with open(random.choice(txt_list)) as txt:
        txt_data = txt.read()
        my_msg = txt_data.replace(PLACEHOLDER,birthdays_dict[today_tuple]["name"])

    to = birthdays_dict[today_tuple]["email"]
    send_msg(my_msg,to)



