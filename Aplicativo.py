from tkinter import *

i = tk()

i.title("Aplicativo")
i.geometry("400x300")

Nome = i.Label(text="Digite o seu nome:",
              bg="white")
Botao = i.Button(text="Aceitar")

i.mainloop()
