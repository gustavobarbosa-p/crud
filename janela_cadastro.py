from tkinter import *

from lanche import Lanche
from lanche_repositorio import LancheRepositorio

lanche_repositorio = LancheRepositorio()

def cadastrar(nome, preco, mensagem, janela_cadastro):
    texto_nome = nome.get()
    texto_preco = preco.get()

    lanche = lanche_repositorio.buscar(texto_nome)
    for i in lanche:
        if i.nome == texto_nome:
            mensagem['text'] = 'Lanche já cadastrado'
            mensagem['bg'] = '#FF0000'
            return

    if texto_nome != '' and texto_preco != '':
        obj1 = Lanche(texto_nome, texto_preco)
        lanche_repositorio.cadastrar(obj1)
        nome['state'] = 'disabled'
        preco['state'] = 'disabled'
        
        i = 3
        while i >= 0:
            mensagem['text'] = f'Lanche cadastrado com sucesso, \nessa janela será fechada em {i} segundos'
            i-=1
            mensagem['bg'] = '#00FF7F'
            janela_cadastro.after(1000)
            janela_cadastro.update()

        janela_cadastro.destroy()
    else:
        mensagem['text'] = 'Preencha todos os campos'
        mensagem['bg'] = '#FF0000'
        

def JanelaCadastro():
    janela_cadastro = Toplevel()
    janela_cadastro.title('Janela de cadastro')
    janela_cadastro.configure(background="#363636")
    janela_cadastro.resizable(False, False)
    janela_cadastro.geometry('500x220')
    janela_cadastro.focus_force()

    texto_nome = Label(janela_cadastro, text='Digite um nome: ', bg='#4F4F4F', fg='#FFFFFF', font=('Arial Black', 12))
    texto_nome.grid(row=0, column=0, padx=10, pady=10)

    nome = Entry(janela_cadastro, bd=2, width=30, justify='left', state='normal')
    nome.grid(row=0, column=1, pady=10)

    texto_preco = Label(janela_cadastro, text='Digite um preço: ', bg='#4F4F4F', fg='#FFFFFF', font=('Arial Black', 12))   
    texto_preco.grid(row=1, column=0, padx=10, pady=10)

    preco = Entry(janela_cadastro, bd=2, width=30, justify='left', state='normal')
    preco.grid(row=1, column=1, pady=10)

    mensagem = Label(janela_cadastro, text='', bg='#363636', fg='#000000', font=('Arial', 12))
    mensagem.grid(row=3, column=1, padx=10, pady=10)

    submit = Button(janela_cadastro, text='Cadastrar', bg='#00FF00', fg='#000000', font=('Arial', 12), width=10, height=2, command=lambda: cadastrar(nome, preco, mensagem, janela_cadastro))
    submit.grid(row=2, column=1, padx=20, pady=0)

    sair = Button(janela_cadastro, text='Sair', bg='#FF0000', fg='#000000', font=('Arial', 12), command=janela_cadastro.destroy)
    sair.grid(row=2, column=0, padx=10, pady=40)

    janela_cadastro.mainloop()