from tkinter import *


def func():
  print("Bem Vindo")


i = Tk()
i.title("Aplicativo")
i.geometry("400x300")
texto = Label(i, text="Olá, mundo!").pack()
pergunta = Entry(i, text="Digite seu nome").pack()
botao = Button(i, text="Clique aqui!", command=func).pack()
i.mainloop()
