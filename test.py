from tkinter import *
from PIL import ImageTk, Image

root = Tk()

image1 = ImageTk.PhotoImage(Image.open("C:/Users/mento/OneDrive/Pulpit/python/pyt-ze1 — 2/IWONA/iwpio1.jpg"))
my_label = Label(root, image=image1)
my_label.grid(row=2, column=0)

root.mainloop()