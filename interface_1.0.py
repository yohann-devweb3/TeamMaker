from cProfile import label
from cgitb import text
from tkinter import*
from turtle import title
#from PIL import Image

root = Tk()

root.title("Team Maker")
root.geometry("600x700")

myWindow=Canvas(root, width=600, height=700, bg= "grey")

#Encadrement Titre
myWindow.create_rectangle(10, 10, 590, 100, fill="blue")

#Titre
titre = Label(myWindow, text="Team Maker", bg="blue", fg="white", font=("courier",30))

#bouton start
go = Button(myWindow, width=45,bg="dark grey", text="Start")

#groupe 1
myWindow.create_text(120, 190, text="GROUPE 1")
myWindow.create_rectangle(10, 200, 270, 300, fill="white")

#groupe 2
myWindow.create_text(430, 190, text="GROUPE 2")
myWindow.create_rectangle(330, 200, 590, 300, fill="white")

#groupe 3
myWindow.create_text(120, 340, text="GROUPE 3")
myWindow.create_rectangle(10, 350, 270, 450, fill="white")

#groupe 4
myWindow.create_text(430, 340, text="GROUPE 4")
myWindow.create_rectangle(330, 350, 590, 450, fill="white")

#groupe 5
myWindow.create_text(300, 500, text="GROUPE 5")
myWindow.create_rectangle(155, 510, 425, 610, fill="white")

titre.place(x=180, y=30)
go.place(x=120, y=130)
myWindow.pack()
root.mainloop()