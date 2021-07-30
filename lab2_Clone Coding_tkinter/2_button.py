from tkinter import *

window = Tk()

window.title("My Window")

B1 = Button(window, text="버튼 1")
B1.pack()

B2 = Button(window, padx=5, pady=10, text="버튼 2") # 버튼 내 여백 (버튼 상대 크기 설정)
B2.pack()

B3 = Button(window, padx=10, pady=5, text="버튼 3")
B3.pack()

B4 = Button(window, text="버튼 4", width=10, height=3) # 버튼 자체의 절대 크기
B4.pack()

B5 = Button(window, fg="red", bg="yellow", text="버튼 5") # 버튼 색과 글자 색
B5.pack()

# 이미지 버튼
photo = PhotoImage(file="img.png")
B6 = Button(window, image=photo)
B6.pack()

# 버튼에 동작 삽입
def btncmd():
    print("버튼 클릭됨")

B7 = Button(window, text="동작하는 버튼", command=btncmd)
B7.pack()

window.mainloop()
