from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title('Banana')
root.geometry("600x575")


Img1 = ImageTk.PhotoImage(Image.open("Bird.jpeg"))
Img2 = ImageTk.PhotoImage(Image.open("Bird_2.jpeg"))
Img3 = ImageTk.PhotoImage(Image.open("Bird_3.jpeg"))
Img4 = ImageTk.PhotoImage(Image.open("Bird_4.jpeg"))
Img5 = ImageTk.PhotoImage(Image.open("Bird_5.jpeg"))
Img6 = ImageTk.PhotoImage(Image.open("Bird_6.jpeg"))


label_1 = Label(root, image=Img1)
label_2 = Label(root, image=Img2)
label_3 = Label(root, image=Img3)
label_4 = Label(root, image=Img4)
label_5 = Label(root, image=Img5)
label_6 = Label(root, image=Img6)

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=1, column=0)
label_4.grid(row=1, column=1)
label_5.grid(row=2, column=0)
label_6.grid(row=2, column=1)


root.mainloop()
