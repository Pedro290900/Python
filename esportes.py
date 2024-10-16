from tkinter import *

i= Tk()
i.title("Pesquisa")
i.geometry("400x300")

escolha = Label(i, text="Esporte(s) favorito(s):")

futebol = Checkbutton(i, text="Futebol").pack()
basquete = Checkbutton(i, text="basquete").pack()
handebol = Checkbutton(i, text="handebol").pack()
volei = Checkbutton(i, text="volei").pack()

i.mainloop()
