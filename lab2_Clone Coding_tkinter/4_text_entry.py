from tkinter import *

window = Tk()
window.title("My window")

T1 = Text(window, width=30, height=5)
T1.pack()
T1.insert(END, "글자를 입력하세요")

E1 = Entry(window, width=30)
E1.pack()
E1.insert(0, "한 줄만 입력")

def btncmd():
    # 출력
    print(T1.get("1.0", END)) # row 1 column 0부터 get
    print(E1.get())

    # 삭제
    T1.delete("1.0", END)
    E1.delete(0, END)

B1 = Button(window, text="클릭", command=btncmd)
B1.pack()

window.mainloop()