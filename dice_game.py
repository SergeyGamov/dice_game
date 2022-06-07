from tkinter import *
import random, time

def brosok():
    x = random.choice(['one.png', 'two.png', 'three.png',
                       'four.png', 'five.png', 'six.png'])
    return x

def img(event):
    global b1, b2
    for i in range(18):
        b1 = PhotoImage(file=(brosok()))
        b2 = PhotoImage(file=(brosok()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.12)    

root = Tk()
root.geometry('700x393')
root.title('Игра в кости. Сделай бросок!')
root.resizable(height = False, width = False)
root.iconphoto(True, PhotoImage(file=('icon.png')))
background = PhotoImage(file=('background_700_393.png'))
Label(root, image=background).pack()
lab1 = Label(root)
lab1.place(relx=0.25, rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.55, rely=0.5, anchor=CENTER)
root.bind('<1>', img)
img('event')             
root.mainloop()
