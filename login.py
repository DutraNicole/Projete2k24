import os #usado para construir caminhos para os arquivos de imagem
import tkinter as tk #Importa o módulo tkinter, que é a biblioteca padrão para criar interfaces gráficas em Python
from tkinter import messagebox
from tkinter import PhotoImage #Importa a classe PhotoImage do tkinter, usada para exibir imagens em janelas gráficas
from PIL import Image, ImageTk #Importa as classes Image e ImageTk da biblioteca Pillow (PIL), que é usada para manipulação avançada de imagens
import datetime as dt
import hashlib

def fazer_login():
    email = entry_email_login.get()
    senha = entry_senha_login.get()
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    from config import lista_cadastros

    for cadastro in lista_cadastros:
        if cadastro[2] == email and cadastro[3] == senha_hash:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            janela_login.destroy()
            #criar_janela_inicial()
            return

    messagebox.showerror("Erro", "Email ou senha incorretos")

def criar_janela_login():
    global entry_email_login, entry_senha_login, janela_login

    janela_login = tk.Tk() #primeira janela criada(janela inteira)
    janela_login.title('Login')
    janela_login.geometry('400x400')#tamanho da janela
    janela_login.configure(bg='#a2d8f1') #Cor de fundo semelhante à da imagem

    label_email = tk.Label(janela_login, text="Email", font = ("Helvetica", 14, "bold"), bg = '#a2d8f1', fg = '#f9e653')
    label_email.pack(pady=10)
    entry_email_login = tk.Entry(janela_login,font=("Helvetica", 12),bg='#539AFF',fg="white")
    entry_email_login.pack(pady=10)

    label_senha = tk.Label(janela_login, text="Senha", font = ("Helvetica", 14, "bold"), bg = '#a2d8f1', fg = '#f9e653')
    label_senha.pack(pady=10)
    entry_senha_login = tk.Entry(janela_login,font=("Helvetica", 12),bg='#539AFF',fg="white", show='*')
    entry_senha_login.pack(pady=10)

    botao_login = tk.Button(janela_login, text="Fazer login",font=("Helvetica", 12), bg="#5fa3f1", fg="white", width=20, height=2, command=fazer_login)
    botao_login.pack(pady=10)

    from main import janela_principal

    janela_login.transient(janela_principal)
    janela_login.grab_set()
    janela_principal.wait_window(janela_login)