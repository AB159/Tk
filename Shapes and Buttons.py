#Tk Shapes and Buttons
from tkinter import *
root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()
def drawCircle():
    canvas.create_oval(100,100, 175,175, fill ="blue", outline = "red")
def drawRec():
    canvas.create_rectangle(10,10, 50,50, fill = "blue", outline = "red")
def drawSquare():
    canvas.create_rectangle(55,55, 110,110, fill = "blue", outline = "red")
def moveTri(event):
    if event.keysm == "w":
        canvas.move(1, 0, -3)
    if event.keysm == "s":
        canvas.move(1, 0, 3)
    if event.keysm == "a":
        canvas.move(1, 0, -3)
    if event.keysm == "s":
        canvas.move(1, 0, -3)


    
    


btn1 = Button(root, text= "Circle", command=drawCircle)
btn1.pack()
btn2 = Button(root, text= "Rectangle", command=drawRec)
btn2.pack()
btn3 = Button(root, text= "Quit", command=root.destroy)
btn3.pack()
btn4 = Button(root, text= "Square", command=drawSquare)
btn4.pack()
