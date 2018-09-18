import tkinter
from tkinter import *
import guicontroller


root = Tk()
frame = Frame(root,width=500,height=300)
frame.pack()
controllerGui = guicontroller.GuiController()
C = tkinter.Canvas(frame, height=100,width=400)
C.pack()
C.create_text(200, 20, text="Pengolahan Citra Digital",font='Helvetica 18 bold')
C.create_text(200, 50, text="Charly Haholongan Situmorang",font='Helvetica 14 bold')
C.create_text(200, 80, text="1301150023", font='Helvetica 14 bold')
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

blackbutton = Button(bottomframe, text="Browse Photos", fg="black", command=controllerGui.browse_photoButton)
blackbutton.pack(side=BOTTOM)
root.mainloop()


#==========Pengolahan Citra Digital=============
# Nama : Charly Haholongan Situmorang
# NIM  : 1301150023
