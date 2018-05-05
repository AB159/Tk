#Tk Shapes and Buttons
from tkinter import *
root = Tk()
root.title("Shapes and Buttons")
canvas = Canvas(root, width=400, height=400)
canvas.pack()
canvas.create_polygon(10,10, 10,60, 50,35)
def drawCircle():
    canvas.create_oval(170,170, 200,200, fill ="blue", outline = "red")
def drawRec():
    canvas.create_rectangle(300,300, 250,200, fill = "blue", outline = "red")
def drawSquare():
    canvas.create_rectangle(150,150, 100,100, fill = "blue", outline = "red")
def moveTri(event):
    if event.keysm == "w":
        canvas.move(1, 0, -3)
    if event.keysm == "s":
        canvas.move(1, 0, 3)
    if event.keysm == "a":
        canvas.move(1, -3, 0)
    if event.keysm == "d":
        canvas.move(1, 3, 0)
canvas.bind_all('KeyPress>', moveTri)
    


btn1 = Button(root, text= "Circle", command=drawCircle)
btn1.pack()
btn2 = Button(root, text= "Rectangle", command=drawRec)
btn2.pack()
btn3 = Button(root, text= "Quit", command=root.destroy)
btn3.pack()
btn4 = Button(root, text= "Square", command=drawSquare)
btn4.pack()
