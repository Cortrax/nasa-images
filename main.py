from tkinter import *
from tkinter import font

root = Tk()
root.geometry("800x800")
root.title("Nasa Images")


input_font = font.Font(size=16)
user_input = Entry(root, width=30, font=input_font)
user_input.place(x=180, y=20, height=45)


def get_user_input():
    try:
        return user_input.get()
    finally:
        user_input.delete(0, END)


def get_image():
    get_user_input()


enter_input = Button(root, text="🔍", font=input_font, height=1, command=get_image)
enter_input.place(x=560, y=20)


root.mainloop()