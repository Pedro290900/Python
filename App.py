from tkinter import *

def func():
    nome = entrada.get()
    if nome.strip():
        resultado.config(text=f"Bem-vindo, {nome}!")
    else:
        resultado.config(text="⚠️ Por favor, digite seu nome.")

# Criando a janela
i = Tk()
i.title("Aplicativo")
i.geometry("400x300")
i.configure(bg="#f0f0f0")

# Texto inicial
texto = Label(i, text="Olá, mundo!", font=("Arial", 14), bg="#f0f0f0")
texto.pack(pady=10)

# Caixa de entrada
entrada_label = Label(i, text="Digite seu nome:", font=("Arial", 12), bg="#f0f0f0")
entrada_label.pack()
entrada = Entry(i, font=("Arial", 12), width=25)
entrada.pack(pady=5)

# Botão
botao = Button(i, text="Clique aqui!", command=func, bg="#004080", fg="white", font=("Arial", 12))
botao.pack(pady=10)

# Resultado
resultado = Label(i, text="", font=("Arial", 12), bg="#f0f0f0")
resultado.pack(pady=20)

# Loop principal
i.mainloop()
