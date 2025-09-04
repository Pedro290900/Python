from tkinter import *

# Criando a janela principal
app = Tk()
app.title("Aplicativo")
app.geometry("400x300")
app.configure(bg="#f0f0f0")  # fundo cinza claro

# Função para quando o botão for clicado
def aceitar():
    nome = entrada_nome.get()
    if nome.strip():
        resultado.config(text=f"Olá, {nome}! Seja bem-vindo(a)!")
    else:
        resultado.config(text="⚠️ Por favor, digite um nome.")

# Rótulo
label_nome = Label(app, text="Digite o seu nome:", bg="white", font=("Arial", 12))
label_nome.pack(pady=10)

# Caixa de entrada
entrada_nome = Entry(app, font=("Arial", 12), width=25)
entrada_nome.pack(pady=5)

# Botão
botao = Button(app, text="Aceitar", command=aceitar, bg="#004080", fg="white", font=("Arial", 12))
botao.pack(pady=10)

# Rótulo para mostrar resultado
resultado = Label(app, text="", bg="#f0f0f0", font=("Arial", 12))
resultado.pack(pady=20)

# Loop principal
app.mainloop()
