from cProfile import label
from cgitb import text
from tkinter import*
from turtle import title
import random

maList = ["yohann","vivian","gregory","Isaia","angelina","jonathan","brandon","corentin","leon","colin","noah","anselm","mavrick","elias"]


def  group():

    random.shuffle(maList)

    global groupe1
    global groupe2
    global groupe3
    global groupe4
    global groupe5

    listRandom=[]
    groupe1=[]
    groupe2=[]
    groupe3=[]
    groupe4=[]
    groupe5=[]

    for i in range(0, len(maList)):
        listRandom.append(maList[i])
    
    groupe1.append(listRandom[0:3])
    team1 = Text(myWindow,height=5, width=30)
    team1.place(x=15, y=210)
    for people in groupe1:
        team1.insert(END, people)

    groupe2.append(listRandom[3:6])
    team2 = Text(myWindow,height=5, width=30)
    team2.place(x=335, y=210)
    for people in groupe2:
        team2.insert(END, people)

    groupe3.append(listRandom[6:9])
    team3 = Text(myWindow,height=5, width=30)
    team3.place(x=15, y=355)
    for people in groupe3:
        team3.insert(END, people)

    groupe4.append(listRandom[9:12])
    team4 = Text(myWindow,height=5, width=30)
    team4.place(x=335, y=355)
    for people in groupe4:
        team4.insert(END, people)
    
    groupe5.append(listRandom[12:14])
    team5 = Text(myWindow,height=5, width=30)
    team5.place(x=175, y=510)
    for people in groupe5:
        team5.insert(END, people)




#création de l'interfacce---------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()

root.title("Team Maker")
root.geometry("600x700")

myWindow=Canvas(root, width=600, height=700, bg= "grey")

#Encadrement Titre
myWindow.create_rectangle(10, 10, 590, 100, fill="blue")

#Titre
titre = Label(myWindow, text="Team Maker", bg="blue", fg="white", font=("courier",30))

#bouton start
go = Button(myWindow, width=45,bg="dark grey", text="Start", command=group)

#groupe 1
myWindow.create_text(120, 190, text="GROUPE 1")

#groupe 2
myWindow.create_text(430, 190, text="GROUPE 2")

#groupe 3
myWindow.create_text(120, 340, text="GROUPE 3")

#groupe 4
myWindow.create_text(430, 340, text="GROUPE 4")

#groupe 5
myWindow.create_text(300, 500, text="GROUPE 5")



titre.place(x=180, y=30)
go.place(x=120, y=130)
myWindow.pack()
root.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------