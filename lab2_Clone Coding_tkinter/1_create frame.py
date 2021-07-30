from tkinter import *

window = Tk()

window.title("My Window") # 창 제목
window.geometry("640x480+100+300") # 창의 가로 크기 x 세로 크기 + 창의 x좌표 + 창의 y좌표

window.resizable(0, 0) # x(너비), y(높이) 창 크기 변경 불가

window.mainloop()
