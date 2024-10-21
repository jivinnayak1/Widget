from tkinter import *

window = Tk()

window.config(bg="lightblue")
window.geometry("300x300")

Header = Label(text="Welcome to my age calculator",fg="black",bg="lightblue",font=("Times",12,"bold"))
Header.pack()


def CalculateAge():
    birthday_year = int(Age_input.get())
    my_age = 2024 - birthday_year
    Result.config(text=f"Your age is {my_age}")

Age_input = Entry(font=("Arial",12,"bold"))
Age_input.pack()

Check = Button(text="Calculate Age",pady=2,command=CalculateAge)
Check.pack()

Result = Label(text="",fg="black",bg="lightblue",font=("Times",12,"bold"))
Result.pack()

window.mainloop()