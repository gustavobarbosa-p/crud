from tkinter import *

from lanche import Lanche
from lanche_repositorio import LancheRepositorio

lanche_repositorio = LancheRepositorio()

def cadastrar(nome, preco, mensagem, janela_cadastro, operacao, botao_submit, sair, variavel_excluir, nome_edit, lista_buscar_lanches, buscar_lanche, preco_edit):
    texto_nome = nome.get()
    texto_preco = preco.get()

    if operacao == 'cadastrado':
        lanche = lanche_repositorio.buscar(texto_nome)
        for i in lanche:
            if i.nome == texto_nome:
                mensagem['text'] = 'Esse lanche já existe'
                mensagem['fg'] = '#FF0000'
                return
        
        if texto_nome != '' and texto_preco != '':
            obj1 = Lanche(texto_nome, texto_preco)
            lanche_repositorio.cadastrar(obj1)
            nome['state'] = 'disabled'
            preco['state'] = 'disabled'
            botao_submit['state'] = 'disabled'
            sair['state'] = 'disabled'
            mensagem['fg'] = '#00FF7F'
            lanche_repositorio.excluir(variavel_excluir)
        else:
            mensagem['text'] = 'Preencha todos os campos'
            mensagem['fg'] = '#FF0000'
            return
    
    if operacao == 'editado':
        if texto_nome == '':
            texto_nome = variavel_excluir
        if texto_preco == '':
            texto_preco = preco_edit
            
        obj1 = Lanche(texto_nome, texto_preco)
        lanche_repositorio.cadastrar(obj1)
        nome['state'] = 'disabled'
        preco['state'] = 'disabled'
        botao_submit['state'] = 'disabled'
        sair['state'] = 'disabled'
        mensagem['fg'] = '#00FF7F'
        lanche_repositorio.excluir(variavel_excluir)
            
    i = 3
    while i >= 0:
        mensagem['text'] = f'Lanche {operacao} com sucesso, \nessa janela será fechada em {i} segundos'
        i-=1
        janela_cadastro.after(900)
        janela_cadastro.update()
    
    if operacao == 'cadastrado':
        janela_cadastro.destroy()
    else:
        buscar_lanche(nome_edit, lista_buscar_lanches)
        janela_cadastro.destroy()


def JanelaCadastro(nome='Digite um nome: ', preco='Digite um preço: ', submit='Cadastrar', operacao='cadastrado', titulo='Janela de Cadastro', variavel_excluir='', nome_edit='', lista_buscar_lanches='', buscar_lanche='', preco_edit=''):
    janela_cadastro = Toplevel()
    janela_cadastro.title(titulo)
    janela_cadastro.configure(background="#000000")
    janela_cadastro.resizable(False, False)
    janela_cadastro.geometry('510x270')
    janela_cadastro.grab_set()

    texto_nome = Label(janela_cadastro, text=nome, bg='#000000', fg='#FFFFFF', font=('Arial Black', 12))
    texto_nome.grid(row=0, column=0, padx=10, pady=10)

    nome = Entry(janela_cadastro, bd=2, width=30, justify='left', state='normal', font=('Arial', 13))
    nome.grid(row=0, column=1, pady=10)

    texto_preco = Label(janela_cadastro, text=preco, bg='#000000', fg='#FFFFFF', font=('Arial Black', 12))   
    texto_preco.grid(row=1, column=0, padx=10, pady=10)

    preco = Entry(janela_cadastro, bd=2, width=30, justify='left', state='normal', font=('Arial', 13))
    preco.grid(row=1, column=1, pady=10)

    mensagem = Label(janela_cadastro, text='', fg='#363636', bg='#000000', font=('Arial', 12))
    mensagem.grid(row=3, column=1, padx=10, pady=10)

    sair = Button(janela_cadastro, text='Sair', fg='#FF0000', bg='#000000', font=('Arial', 12), command=janela_cadastro.destroy)
    sair.grid(row=2, column=0, padx=10, pady=40)
    
    botao_submit = Button(janela_cadastro, text=submit, fg='#00FF00', bg='#000000', font=('Arial', 12), width=10, height=2, state='normal', command=lambda: cadastrar(nome, preco, mensagem, janela_cadastro, operacao, botao_submit, sair, variavel_excluir, nome_edit, lista_buscar_lanches, buscar_lanche, preco_edit))
    botao_submit.grid(row=2, column=1, padx=20, pady=0)
    
    return True