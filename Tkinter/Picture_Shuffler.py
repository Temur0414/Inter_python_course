from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Banana')
root.configure(bg="lightgray")

my_img = ImageTk.PhotoImage(Image.open("Bird.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("Bird_2.jpeg"))
my_img3 = ImageTk.PhotoImage(Image.open("Bird_3.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("Bird_4.jpeg"))
my_img5 = ImageTk.PhotoImage(Image.open("Bird_5.jpeg"))


image_list = [my_img, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=3, relief=SUNKEN, anchor=E)

my_label = Label(root, image=my_img)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])

    button_forward = Button(root, text=">>", highlightbackground="lightgray", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", highlightbackground="lightgray", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED, highlightbackground="lightgray")

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=3, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])

    button_forward = Button(root, text=">>", highlightbackground="lightgray", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", highlightbackground="lightgray", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED, highlightbackground = "lightgray")

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=3, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_exit = Button(root, text="Exit Window", command=root.quit, highlightbackground="lightgray")
button_back = Button(root, text="<<", highlightbackground="lightgray", command=back)
button_forward = Button(root, text=">>", highlightbackground="lightgray", command=lambda: forward(2))

button_exit.grid(row=1, column=1)
button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()

# this is a comment to test vi <file_name.txt> and hit "i" and start entering our new text, then we need to save the changes before we exit the "vi", this is to save and exit the file hit "Esc" and then ":wq!"

