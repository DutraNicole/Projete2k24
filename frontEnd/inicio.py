import os
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import datetime as dt
import hashlib
#import teste

def criar_janela_materia():
    pass

def acessar_materia():
    pass

def criar_janela_inicial():
    global janela_inicial
    janela_inicial = tk.Tk()
    janela_inicial.title('Bem-vindo(a)')
    janela_inicial.geometry('400x600')
    janela_inicial.configure(bg='#a2d8f1')

    botao_criar_materia = tk.Button(janela_inicial, text="Criar matéria", font=("Helvetica", 12), bg="#5fa3f1", fg="#f9f58a", width=20, height=2, command=criar_janela_materia)
    botao_criar_materia.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    botao_acessar_materia = tk.Button(janela_inicial, text="Acessar matérias", font=("Helvetica", 12), bg="#5fa3f1", fg="#f9f58a", width=20, height=2, command=acessar_materia)
    botao_acessar_materia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    botao_sair = tk.Button(janela_inicial, text="Sair", font=("Helvetica", 12), bg="#5fa3f1", fg="#f9f58a", width=20, height=2, command=janela_inicial.destroy)
    botao_sair.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    janela_inicial.mainloop()

criar_janela_inicial()
