# import tkinter
#
# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=900, height=300)
#
# # Label
#
# my_label = tkinter.Label(text="I am a Label", font=("Arial",24,"bold"))
# my_label.pack()
# window.mainloop()

# *args create a tuple
# def sum(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
# print(sum(1,2,3,6,7,8,6,6))
#
# # **kwargs create a dict
# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add=3,multiply=5)

class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")  # benifit of get is if key is not present in method then it will not throw an error
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Mahindra",model="Xylo",color="white")
print(my_car.color)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)