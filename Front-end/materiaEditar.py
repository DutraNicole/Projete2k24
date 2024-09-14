import os #usado para construir caminhos para os arquivos de imagem
import tkinter as tk #Importa o módulo tkinter, que é a biblioteca padrão para criar interfaces gráficas em Python
from tkinter import messagebox
from tkinter import PhotoImage #Importa a classe PhotoImage do tkinter, usada para exibir imagens em janelas gráficas
from PIL import Image, ImageTk #Importa as classes Image e ImageTk da biblioteca Pillow (PIL), que é usada para manipulação avançada de imagens
import datetime as dt
import hashlib
import inicio
from config import lista_materias

def editar_materia(index):
    novo_titulo = entry_editar_materia.get()
    '''novo_corpo = entry_editar_texto.get()'''
    novo_corpo = editar_text_corpo.get("1.0", tk.END).strip()  # Obtém o texto completo do widget Text

    if not novo_titulo or not novo_corpo:
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    lista_materias[index - 1] = (novo_titulo, novo_corpo, lista_materias[index - 1][2])

    messagebox.showinfo("Sucesso", "Matéria editada com sucesso!")
    janela_editar_materia.destroy()

def criar_janela_editar_materia(index):
    global entry_editar_materia, entry_editar_texto, janela_editar_materia

    janela_editar_materia = tk.Toplevel()
    janela_editar_materia.title('Editar Matéria')
    janela_editar_materia.geometry('400x600')  # tamanho da janela
    janela_editar_materia.configure(bg='#a2d8f1')

    titulo, corpo, _ = lista_materias[index - 1]

    label_editar_materia = tk.Label(janela_editar_materia, text="Título da matéria", font = ("Helvetica", 14, "bold"), bg = '#a2d8f1', fg = '#f9e653')
    label_editar_materia.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_editar_materia = tk.Entry(janela_editar_materia)
    entry_editar_materia.insert(0, titulo)
    entry_editar_materia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_editar_texto = tk.Label(janela_editar_materia, text="Corpo da matéria", font = ("Helvetica", 14, "bold"), bg = '#a2d8f1', fg = '#f9e653')
    label_editar_texto.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    entry_editar_texto = tk.Text(janela_editar_materia, height=10, width=40,wrap=tk.WORD)  # 'wrap=tk.WORD' quebra o texto automaticamente
    entry_editar_texto.insert("1.0", corpo)
    entry_editar_texto.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    botao_editar = tk.Button(janela_editar_materia, text="Salvar Alterações", font=("Helvetica", 12), bg="#5fa3f1", fg="#f9f58a", width=20, height=2, command=lambda: editar_materia(index))
    botao_editar.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    janela_editar_materia.transient(inicio.janela_inicial)
    janela_editar_materia.grab_set()
    inicio.janela_inicial.wait_window(janela_editar_materia)
    
