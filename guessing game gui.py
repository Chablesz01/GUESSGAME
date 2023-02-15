from  tkinter import *
import random

root = Tk()

f = random.randint(1,31)

def Submit():
    g = 1
    h = int(c.get())

    while g<=5:
        if h == f:
            i = Label (root, text= "You guessed right!")
            i.pack()
        elif h>30:
            j = Label (root, text= "Guess between 1 and 30")
            j.pack()
        elif h<f:
            k = Label (root, text= "Your guess is low, Guess High")
            k.pack()
        elif h>f:
            l = Label (root, text= "Your guess is high, Guess Low")
            l.pack()
        else:
            m = Label (root, text= "Guess between 1 and 30")
            m.pack()

        """if g == 5 and h != f:
            n = Label (root, text= "\nOops! No more attempts")
            n.pack()"""
        g+=1
    

a = Label(root, text = "THE GUESSING GAME", font=("Cambria Bold", 20), bg="Black", fg="White").pack()
b = Label(root, text = "Guess a number: ", font=("Cambria", 16), bg="White", fg="Black").pack()
c = Entry(root, width=30)
c.pack()
d = Button(root, text = "Submit",font=("Cambria", 14), bg="Dark Green", fg="White", command = Submit).pack()

root.mainloop()