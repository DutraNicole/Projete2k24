import os  # usado para construir caminhos para os arquivos de imagem
import tkinter as tk  # Importa o módulo tkinter, que é a biblioteca padrão para criar interfaces gráficas em Python
from tkinter import PhotoImage, messagebox  # Importa a classe PhotoImage do tkinter, usada para exibir imagens
from PIL import Image, ImageTk  # Importa as classes Image e ImageTk da biblioteca Pillow (PIL)
import datetime as dt  # Importa a biblioteca datetime para manipulação de datas
import hashlib  # (Se for necessário, dependendo do uso futuro)

from config import lista_materias  # Supondo que 'config' é um módulo externo
from materiaEditar import criar_janela_editar_materia

def acessar_materia():
    if not lista_materias:
        messagebox.showinfo("Informação", "Nenhuma matéria disponível")
        return

    janela_acessar_materia = tk.Toplevel()
    janela_acessar_materia.title('Acessar Matéria')
    janela_acessar_materia.geometry('400x600')  # tamanho da janela
    janela_acessar_materia.configure(bg='#a2d8f1')  # Cor de fundo semelhante à da imagem

    for i, materia in enumerate(lista_materias, start=1):
        titulo, corpo, data = materia
        tk.Label(janela_acessar_materia, text=f"Matéria {i}").pack()
        tk.Label(janela_acessar_materia, text=f"Título: {titulo}").pack()
        tk.Label(janela_acessar_materia, text=f"Data: {data}").pack()
        tk.Label(janela_acessar_materia, text=f"Corpo: {corpo}").pack()
        tk.Label(janela_acessar_materia, text="").pack()  # Espaçamento

        # Botão para editar a matéria
        botao_editar = tk.Button(janela_acessar_materia, text="Editar",
                                 command=lambda i=i: criar_janela_editar_materia(i))
        botao_editar.pack(padx=10, pady=5, fill=tk.BOTH)

def criar_materia():
    titulo = entry_materia.get()
    corpo = entry_texto.get()

    if not titulo or not corpo:
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    # Salvar matéria na lista de matérias
    data_criacao = dt.datetime.now().strftime("%d/%m/%y %H:%M")
    lista_materias.append((titulo, corpo, data_criacao))

    messagebox.showinfo("Sucesso", "Matéria criada com sucesso!")
    janela_materia.destroy()

def criar_janela_materia():
    global entry_materia, entry_texto, janela_materia

    janela_materia = tk.Toplevel()
    janela_materia.title('Criar Matéria')
    janela_materia.geometry('400x600')  # tamanho da janela
    janela_materia.configure(bg='#a2d8f1')  # Cor de fundo semelhante à da imagem

    label_materia = tk.Label(janela_materia, text="Título da matéria",  font=("Helvetica", 14, "bold"), bg='#a2d8f1', fg='#f9e653')
    label_materia.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_materia = tk.Entry(janela_materia)
    entry_materia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_texto = tk.Label(janela_materia, text="Corpo da matéria", font=("Helvetica", 14, "bold"), bg='#a2d8f1', fg='#f9e653')
    label_texto.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_texto = tk.Entry(janela_materia)
    entry_texto.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    botao_materia = tk.Button(janela_materia, text="Criar Matéria", font=("Helvetica", 12), bg="#5fa3f1", fg="#f9f58a", width=20, height=2, command=criar_materia)
    botao_materia.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    janela_materia.transient(janela_inicial)
    janela_materia.grab_set()
    janela_inicial.wait_window(janela_materia)
