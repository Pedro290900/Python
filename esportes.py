from tkinter import *

# Criar janela
i = Tk()
i.title("Pesquisa")
i.geometry("400x300")
i.configure(bg="#f0f0f0")

# Label
escolha = Label(i, text="Esporte(s) favorito(s):", font=("Arial", 14), bg="#f0f0f0")
escolha.pack(pady=10)

# Variáveis para capturar seleções
var_futebol = BooleanVar()
var_basquete = BooleanVar()
var_handebol = BooleanVar()
var_volei = BooleanVar()

# Checkbuttons
chk_futebol = Checkbutton(i, text="Futebol", variable=var_futebol, bg="#f0f0f0", font=("Arial", 12))
chk_basquete = Checkbutton(i, text="Basquete", variable=var_basquete, bg="#f0f0f0", font=("Arial", 12))
chk_handebol = Checkbutton(i, text="Handebol", variable=var_handebol, bg="#f0f0f0", font=("Arial", 12))
chk_volei = Checkbutton(i, text="Vôlei", variable=var_volei, bg="#f0f0f0", font=("Arial", 12))

chk_futebol.pack(anchor="w", padx=100)
chk_basquete.pack(anchor="w", padx=100)
chk_handebol.pack(anchor="w", padx=100)
chk_volei.pack(anchor="w", padx=100)

# Label para resultado
resultado = Label(i, text="", font=("Arial", 12), bg="#f0f0f0")
resultado.pack(pady=20)

# Função para mostrar escolhas
def mostrar():
    escolhidos = []
    if var_futebol.get(): escolhidos.append("Futebol")
    if var_basquete.get(): escolhidos.append("Basquete")
    if var_handebol.get(): escolhidos.append("Handebol")
    if var_volei.get(): escolhidos.append("Vôlei")

    if escolhidos:
        resultado.config(text="Você escolheu: " + ", ".join(escolhidos))
    else:
        resultado.config(text="⚠️ Nenhum esporte selecionado.")

# Botão confirmar
btn = Button(i, text="Confirmar", command=mostrar, bg="#004080", fg="white", font=("Arial", 12))
btn.pack(pady=10)

# Loop principal
i.mainloop()
