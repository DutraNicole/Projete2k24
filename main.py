import os #usado para construir caminhos para os arquivos de imagem
import tkinter as tk #Importa o módulo tkinter, que é a biblioteca padrão para criar interfaces gráficas em Python
from tkinter import PhotoImage #Importa a classe PhotoImage do tkinter, usada para exibir imagens em janelas gráficas
from PIL import Image, ImageTk #Importa as classes Image e ImageTk da biblioteca Pillow (PIL), que é usada para manipulação avançada de imagens

def criar_interface(): #Criação da janela principal
    janela_principal = tk.Tk() #primeira janela criada(janela inteira)
    janela_principal.title('Koala Helper')
    janela_principal.geometry('400x600')#tamanho da janela
    janela_principal.configure(bg='#a2d8f1') #Cor de fundo semelhante à da imagem

    # Frame para centralizar o conteúdo
    frame = tk.Frame(janela_principal, bg='#a2d8f1')
    frame.pack(expand=True)

    caminho_imagem = os.path.join("assets", "logo.png")# Caminho relativo para a imagem na pasta assets

    # Carregar a imagem do koala
    img = Image.open(caminho_imagem)
    img = img.resize((200, 200), Image.Resampling.LANCZOS)  # Redimensionar a imagem
    img_tk = ImageTk.PhotoImage(img)#converte a imagem para o tkinter exibir

    # Label para exibir a imagem
    label_img = tk.Label(frame, image=img_tk, bg='#a2d8f1')
    label_img.pack(pady=20)

    # Label para o título
    label_titulo = tk.Label(frame, text="KOALA HELPER", font=("Helvetica", 24, "bold"), bg='#a2d8f1', fg='#f9e653')
    label_titulo.pack(pady=10)

    # Botão de Entrar
    botao_entrar = tk.Button(frame, text="ENTRAR", font=("Helvetica", 16), bg="#5fa3f1", fg="white", width=20, height=2)
    botao_entrar.pack(pady=10)

    # Botão de Criar Conta
    botao_criar = tk.Button(frame, text="CRIAR CONTA", font=("Helvetica", 16), bg="#5fa3f1", fg="white", width=20, height=2)
    botao_criar.pack(pady=10)

    janela_principal.mainloop()

criar_interface()
