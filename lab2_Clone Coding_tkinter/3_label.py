from tkinter import *

window = Tk()

window.title("My Window")

L1 = Label(window, text="안녕하세요")
L1.pack()

photo = PhotoImage(file="img.png")
L2 = Label(window, image=photo)
L2.pack()

def change():
    L1.config(text="또 만나요")

    global photo2
    photo2 = PhotoImage(file="img2.png")
    L2.config(image=photo2)

B1 = Button(window, text="클릭", command=change)
B1.pack()



window.mainloop()
