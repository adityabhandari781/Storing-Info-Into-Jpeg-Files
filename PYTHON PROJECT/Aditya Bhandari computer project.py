from tkinter import *
from tkinter import ttk
import PIL.Image
import PIL.ImageTk
import io
import os
import sys
root = Tk()
root.title("STORING INFORMATION IN JPG FILES")
root.geometry("1000x500")
root.iconbitmap(r"C:\Users\adity\Desktop\aditya  folder\PYTHON PROJECT STUFF\icon.ico")
root.configure(bg = 'lightblue')

def start(x, y):
    match x, y:
        case 1,4: insert_text()
        case 2,4: load_text()
        case 1,5: insert_img()
        case 2,5: load_img()
        case 1,6: insert_exe()
        case 2,6: load_exe()
        case 3,_: delete_content()


def insert_text():
    def text():
        with open(E.get(), 'ab') as f:
            f.write(bytes(f"{e.get()}", encoding = 'utf-8'))
        l_ = Label(root, text = '\nText successfully inserted.', bg = 'lightblue').pack()

    l = Label(root, text = '\nEnter desired text here: ', bg = 'lightblue').pack()
    e = Entry(root, width = 50)
    e.pack()
    confirm_b = Button(root, text = 'Enter', command = text).pack()


def load_text():
    with open(E.get(), 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))            
        f.seek(offset + 2)
        if bool(f.read()):
            l = Label(root, text = b'\nThe hidden text is: "' + f.read() + b'"', bg = 'lightblue').pack()
        else: l = Label(root, text = '\nNo text has been hidden yet', bg = 'lightblue').pack()


def insert_img():
    def image_():
        img = PIL.Image.open(e.get())
        byte_arr = io.BytesIO()
        img.save(byte_arr, format='PNG')

        with open(E.get(), 'ab') as f:
            f.write(byte_arr.getvalue())
        l = Label(root, text = '\nImage successfully inserted', bg = 'lightblue').pack()

    l = Label(root, text = '\nEnter new image location here: ', bg = 'lightblue').pack()
    e = Entry(root, width = 50)
    e.pack()
    b = Button(root, text = 'Enter', command = image_).pack()


def load_img():
    def image_1():
        with open(E.get(), 'rb') as f:
            content = f.read()
            offset = content.index(bytes.fromhex('FFD9'))
            f.seek(offset + 2)
            extracted_image = PIL.Image.open(io.BytesIO(f.read()))                      #69th line
            image_path = e1.get() + r'\\' + e2.get() + '.png'
            extracted_image.save(image_path)
            im = PIL.Image.open(image_path)
            im.show()
        l = Label(root, text = 'Loading image...', bg = 'lightblue').pack()

    l = Label(root, text = '\nEnter the path/folder in which the extracted image needs to be stored: ', bg = 'lightblue').pack()
    e1 = Entry(root, width = 50)
    e1.pack()
    l = Label(root, text = '\nEnter the name of the extracted image: ', bg = 'lightblue').pack()
    e2 = Entry(root, width = 50)
    e2.pack()
    b = Button(root, text = 'Enter', command = image_1).pack()

def insert_exe():
    def exe_():
        with open(E.get(), 'ab') as f, open(e.get(), 'rb') as ef:
            f.write(ef.read())
        l = Label(root, text = '\nExe successfully inserted', bg = 'lightblue').pack()

    l = Label(root, text = 'Enter exe file location here: ', bg = 'lightblue').pack()
    e = Entry(root, width = 50)
    e.pack()
    b = Button(root, text = 'Enter', command = exe_).pack()


def load_exe():
    def exe_1():
        with open(E.get(), 'rb') as f:
            content = f.read()
            offset = content.index(bytes.fromhex('FFD9'))
            f.seek(offset + 2)
            exe_path = e1.get() + r'\\' + e2.get() + '.exe'
            with open(exe_path, 'wb') as ef:
                ef.write(f.read())
            l = Label(root, text = '\nFile successfully stored in ' + e1.get(), bg = 'lightblue').pack()

    l = Label(root, text = 'Enter the path/folder in which the extracted exe needs to be stored: ', bg = 'lightblue').pack()
    e1 = Entry(root, width = 50)
    e1.pack()
    l = Label(root, text = 'Enter name of the exe that needs to be extracted: ', bg = 'lightblue').pack()
    e2 = Entry(root, width = 50)
    e2.pack()
    b = Button(root, text = 'Enter', command = exe_1).pack()


def delete_content():
    with open(E.get(), 'rb') as f:
        f.seek(0)
        content = f.read()
        new_content = content.split(b'\xff\xd9')[0] + b'\xff\xd9'

    with open(E.get(), 'wb') as f:
        f.write(new_content)
    l = Label(root, text = '\nContent successfully deleted', bg = 'lightblue').pack()


l = Label(root, text = 'STORING INFORMATION IN JPG\'s \nBY ADITYA BHANDARI', font=("Arial", 15), bg = 'lightblue').pack()

l = Label(root, text = '\nEnter path of image in which you want to store data here: ', bg = 'lightblue').pack()
E = Entry(root, width = 50)
#e.insert(0, r'C:\Users\adity\Desktop\aditya  folder\PYTHON PROJECT STUFF\cat.jpg')
E.pack()

l = Label(root, text = '\nWhat action would you like to do?', bg = 'lightblue').pack()

v = IntVar()
v.set(1)
radio1 = {" Insert data " : 1,
        "Extract data" : 2,
        "Delete data " : 3}

for (text, val) in radio1.items():
    Radiobutton(root, text = text, variable = v,
                value = val, indicator = 0,
                background = "light grey").pack(ipadx = 75, ipady = 5)

l = Label(root, text = '\n\nWhat data type will you use?', bg = 'lightblue').pack()
l = Label(root, text = '', bg = 'lightblue')

v_ = IntVar()
v_.set(4)
radio2 = {'   text  ': 4,
          ' image ': 5,
          '.exe file': 6}
for (text_, val_) in radio2.items():
    Radiobutton(root, text = text_, variable = v_,
                value = val_, indicator = 0,
                background = "lightgrey").pack(ipadx = 75, ipady = 5)

l.pack()
b = Button(root, text = 'CONFIRM', command = lambda: start(v.get(), v_.get())).pack()
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

b_reload = Button(root, text="RESTART PROGRAM", command = restart_program).place(x = 25, y = 40)
b_quit = Button(root, text = 'END PROGRAM', command = root.destroy)
b_quit.place(x = 25, y = 10)

root.mainloop()
