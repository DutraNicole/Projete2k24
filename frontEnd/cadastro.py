import os #usado para construir caminhos para os arquivos de imagem
import tkinter as tk #Importa o módulo tkinter, que é a biblioteca padrão para criar interfaces gráficas em Python
from tkinter import messagebox
from tkinter import PhotoImage #Importa a classe PhotoImage do tkinter, usada para exibir imagens em janelas gráficas
from PIL import Image, ImageTk #Importa as classes Image e ImageTk da biblioteca Pillow (PIL), que é usada para manipulação avançada de imagens
import datetime as dt
import hashlib

def criar_cadastro():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    confirmar_senha = entry_confirmar_senha.get()

    if not nome or not email or not senha or not confirmar_senha:
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    if senha != confirmar_senha:
        messagebox.showerror("Erro", "As senhas são diferentes")
        return

    # Hash da senha
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    # Colocando data e hora no cadastro
    data_criacao = dt.datetime.now().strftime("%d/%m/%y %H:%M")

    from config import lista_cadastros

    # Adicionando cadastro à lista
    cadastros = len(lista_cadastros) + 1
    cadastros_str = f"cadastro-{cadastros}"
    lista_cadastros.append((cadastros_str, nome, email, senha_hash, data_criacao))

    # Limpar tudo depois de cadastrar
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    entry_confirmar_senha.delete(0, tk.END)

    # Mensagem de sucesso
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

    # Fecha a janela de cadastro e abre a janela inicial
    janela_cadastro.destroy()
    from login import criar_janela_login
    criar_janela_login()

def criar_janela_cadastro():
    global entry_nome, entry_email, entry_senha, entry_confirmar_senha, janela_cadastro

    janela_cadastro = tk.Tk()  #janela criada
    janela_cadastro.title('Cadastro')
    janela_cadastro.geometry('400x600')  # tamanho da janela
    janela_cadastro.configure(bg='#a2d8f1')  # Cor de fundo semelhante à da imagem

    #frame = tk.Frame(janela_cadastro, bg='#a2d8f1')
    #frame.pack(side='top', pady=10, fill='both')

    label_nome = tk.Label(janela_cadastro, text="Nome de usuário", font = ("Helvetica", 14, "bold"), bg = '#a2d8f1', fg = '#f9e653')
    label_nome.pack(pady=10)
    entry_nome = tk.Entry(janela_cadastro,font=("Helvetica", 12),bg='#539AFF',fg="white")
    entry_nome.pack(pady=10)

    label_email = tk.Label(janela_cadastro, text="Email", font = ("Helvetica", 14, "bold"), bg = '#a2d8f1', fg = '#f9e653')
    label_email.pack(pady=10)
    entry_email = tk.Entry(janela_cadastro,font=("Helvetica", 12),bg='#539AFF',fg="white")
    entry_email.pack(pady=10)

    label_senha = tk.Label(janela_cadastro, text="Senha", font = ("Helvetica", 14, "bold"), bg = '#a2d8f1', fg = '#f9e653')
    label_senha.pack(pady=10)
    entry_senha = tk.Entry(janela_cadastro,font=("Helvetica", 12),bg='#539AFF',fg="white", show='*')
    entry_senha.pack(pady=10)

    label_confirmar_senha = tk.Label(janela_cadastro, text="Confirmar senha", font = ("Helvetica", 14, "bold"), bg = '#a2d8f1', fg = '#f9e653')
    label_confirmar_senha.pack(pady=10)
    entry_confirmar_senha = tk.Entry(janela_cadastro,font=("Helvetica", 12),bg='#539AFF',fg="white",show='*')
    entry_confirmar_senha.pack(pady=10)

    botao_cadastrar = tk.Button(janela_cadastro, text="Cadastrar", font=("Helvetica", 12), bg="#5fa3f1", fg="white", width=20, height=2, command=criar_cadastro)
    botao_cadastrar.pack(pady=10)

    janela_cadastro.mainloop()

    # Inicializar a janela de cadastro
    #criar_janela_cadastro()