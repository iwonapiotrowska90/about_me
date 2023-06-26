from tkinter import *
from PIL import ImageTk, Image

#OKNO_PIERWSZE
root = Tk()
root.title("Iwona.Kosz")

#tekst
tekst1 = Label(root, text="Hi :) I'm Iwona!"
               "\nNice to meeting you!")
tekst1.grid(row=0, column=0)

#zdjecie
image1 = ImageTk.PhotoImage(Image.open("C:/Users/mento/OneDrive/Pulpit/python/pyt-ze1 — 2/IWONA/iwpio1.jpg"))
my_label = Label(root, image=image1)
my_label.grid(row=2, column=0)

#przycisk
my_button = Button(root, text="Click here to get to know me :)", command=root.destroy)
my_button.grid(row=1, column=0)

root.mainloop()

#OKNO_DRUGIE
root2 = Tk()
root2.title("resume")

#przycisk
my_button2 = Button(root2, text="Click here to get to know me :)", command=root2.destroy)
my_button2.pack()

#cv
image2 = ImageTk.PhotoImage(Image.open("C:/Users/mento/OneDrive/Pulpit/python/pyt-ze1 — 2/IWONA/resume1.jpg"))
my_label2 = Label(root2, image=image2)
my_label2.pack()

root2.mainloop()

#OKNO_TRZECIE
root3 = Tk()
root3.title("private & hobbies")

#tekst
tekst3 = Label(root3, text="In 2022 I become a mom!"
               "\nThat is the greatest achievement of my life :)")
tekst3.grid(row=0, column=0)

#zdjecie
image3 = ImageTk.PhotoImage(Image.open("C:/Users/mento/OneDrive/Pulpit/python/pyt-ze1 — 2/IWONA/maksio.jpg"))
my_label3 = Label(root3, image=image3)
my_label3.grid(row=2, column=0)

#przycisk
my_button3 = Button(root3, text="Click here to get to know me :)", command=root3.destroy)
my_button3.grid(row=1, column=0)

root3.mainloop()


#OKNO_CZWARTE
root4 = Tk()
root4.title("private & hobbies")

#tekst
tekst4 = Label(root4, text="In 2018 I started to play piano."
               "\nBecause for passion is never too late.")
tekst4.grid(row=0, column=0)

#zdjecie
image4 = ImageTk.PhotoImage(Image.open("C:/Users/mento/OneDrive/Pulpit/python/pyt-ze1 — 2/IWONA/piano.jpg"))
my_label4 = Label(root4, image=image4)
my_label4.grid(row=2, column=0)

#przycisk
my_button4 = Button(root4, text="Click here to get to know me :)", command=root4.destroy)
my_button4.grid(row=1, column=0)

root4.mainloop()


#OKNO_PIATE
root5 = Tk()
root5.title("private & hobbies")

#tekst
tekst5 = Label(root5, text="I'm also big football fan."
               "\nI played as a child and like watching matches :D")
tekst5.grid(row=0, column=0)

#zdjecie
image5 = ImageTk.PhotoImage(Image.open("C:/Users/mento/OneDrive/Pulpit/python/pyt-ze1 — 2/IWONA/iwpio3.jpg"))
my_label5 = Label(root5, image=image5)
my_label5.grid(row=2, column=0)

#przycisk
my_button5 = Button(root5, text="Thank you for your time!", command=root5.quit)
my_button5.grid(row=1, column=0)

root5.mainloop()



