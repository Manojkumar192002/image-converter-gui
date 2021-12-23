from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image
from tkinter.filedialog import asksaveasfile
from tkinter import ttk

root = Tk()
root.geometry("400x400")
root.title("Image_Conversion_App")


def jpg_to_png():
    filename = fd.askopenfilename()

    if filename.endswith(".jpg") or filename.endswith(".pdf") or filename.endswith(".gif"):
        Image.open(filename).save(fd.asksaveasfilename(defaultextension='.png'))



    else:
        Label_2 = Label(root, text="Error!", width=20, fg="red", font=("bold", 15))
        Label_2.place(x=80, y=280)


def rex():
    print('all done')


def jpg_to_pdf():
    filename = fd.askopenfilename()
    if filename.endswith(".jpg"):
        Image.open(filename).save("sample1.pdf", resolution=100.0)
    else:
        Label_2 = Label(root, text="Error!", width=20, fg="red", font=("bold", 15))
        Label_2.place(x=80, y=280)


Label_1 = Label(root, text="Browse A File", width=20, font=("bold", 15))
Label_1.place(x=80, y=80)

Label_3 = Label(root,
                text="</Developed By:-Shailendra kumar/> \n DM me for further querry:www.facebook/shailendrakr007",
                width=80, font=("bold", 8))
Label_3.place(x=10, y=365)

Button(root, text="to_PNG", width=20, height=2, bg="brown", fg="white", command=jpg_to_png).place(x=120, y=120)
Button(root, text="JPG_to_PDF", width=20, height=2, bg="brown", fg="white", command=jpg_to_pdf).place(x=120, y=220)
Button(root, text="Stx", width=20, height=2, bg="brown", fg="white", command=rex).place(x=120, y=260)
root.mainloop()