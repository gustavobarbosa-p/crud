from tkinter import *

from lanche_repositorio import LancheRepositorio
from janela_cadastro import *

lanche_repositorio = LancheRepositorio()

def buscar_lanche(nome, lista_buscar_lanches):
    lista_buscar_lanches.delete(0, END)

    for lanche in lanche_repositorio.listar():
        if lanche.nome.lower().startswith(nome.get().lower()):
            lista_buscar_lanches.insert(END, lanche, '\n')

def excluir_da_lista(nome, lista_buscar_lanches):
    variavel = ''
    lista = lista_buscar_lanches.get(ANCHOR)

    for l in lista:
        if l != '-':
            variavel += l
        else:
            break

    if lista_buscar_lanches.get(ANCHOR) != '\n':
        lanche_repositorio.excluir(variavel)
        buscar_lanche(nome, lista_buscar_lanches)
        lista_buscar_lanches.delete(ANCHOR)

def criar_janela_editar(nome, lista_buscar_lanches):
    lanche = lista_buscar_lanches.get(ANCHOR)
    variavel = ''

    if lanche == '\n' or lanche == '':
        return
    
    for l in lanche:
        if l != '-':
            variavel += l
        else:
            break

    preco = ''
    rBusca = lanche_repositorio.buscar(variavel)
    for i in rBusca:
        if i.nome == variavel:
            preco = i.preco
            break

    JanelaCadastro('Digite o novo nome: ', 'Digite o novo preço: ', 'Editar', 'editado', f'Editar {lanche}', variavel, nome, lista_buscar_lanches, buscar_lanche, preco)


def editar_variaveis(event, lista_buscar_lanches, botao_delete, botao_edit):
    lanche = ''
    lista = lista_buscar_lanches.get(ANCHOR)

    if lista == '\n' or lista == '':
        botao_delete['text'] = 'Excluir'
        botao_delete['fg'] = '#FF6347'
        botao_edit['text'] = f'Editar {lanche}'
        botao_edit['fg'] = '#F0E68C'
        return

    for l in lista:
        if l != '-':
            lanche += l
        else:
            break

    botao_delete['text'] = f'Excluir {lanche}'
    botao_delete['fg'] = '#FF0000'
    botao_edit['text'] = f'Editar {lanche}'
    botao_edit['fg'] = '#FFFF00'

def JanelaBuscar():
    janela_buscar = Toplevel()
    janela_buscar.title('Janela de busca')
    janela_buscar.configure(background="#000000")
    janela_buscar.resizable(False, False)
    janela_buscar.grab_set()
    
    texto_nome = Label(janela_buscar, text='Digite um nome: ', bg='#000000', fg='#FFFFFF', font=('Arial Black', 12))
    texto_nome.grid(row=0, column=0, padx=10, pady=10)

    nome = Entry(janela_buscar, bd=2, width=30, justify='left', state='normal')
    nome.grid(row=0, column=1, padx=10, pady=10)

    lista_buscar_lanches = Listbox(janela_buscar, width=26, height=15, font=('Arial', 12), bg='#1C1C1C', fg='#F5F5F5')       
    lista_buscar_lanches.grid(row=1, column=2)
    
    scrollbar = Scrollbar(janela_buscar) 
    scrollbar.grid(row=1, column=3, sticky='ns')
    scrollbar.config(command=lista_buscar_lanches.yview)

    scrollbar2 = Scrollbar(janela_buscar, orient=HORIZONTAL)
    scrollbar2.grid(row=2, column=2, sticky='we')
    scrollbar2.config(command=lista_buscar_lanches.xview)

    for lanche in lanche_repositorio.listar():
        if lanche.nome.lower().startswith(nome.get().lower()):
            lista_buscar_lanches.insert(END, lanche, '\n')

    buscar_nome = Button(janela_buscar, text='Buscar', fg='#00FF00', bg='#000000', font=('Arial', 12), command=lambda: buscar_lanche(nome, lista_buscar_lanches))
    buscar_nome.grid(row=0, column=2, padx=10, pady=10)

    sair = Button(janela_buscar, text='Sair', fg='#FF0000', bg='#000000', font=('Arial', 12), command=janela_buscar.destroy)
    sair.grid(row=3, column=0, padx=10, pady=10)

    botao_delete = Button(janela_buscar, text='Excluir', fg='#FF6347', bg='#000000', font=('Arial Black', 12), command=lambda: excluir_da_lista(nome, lista_buscar_lanches))
    botao_delete.grid(row=3, column=2)

    botao_edit = Button(janela_buscar, text='Editar', fg='#F0E68C', bg='#000000', font=('Arial Black', 12), command=lambda: criar_janela_editar(nome, lista_buscar_lanches))
    botao_edit.grid(row=3, column=1, padx=10, pady=10)
    
    janela_buscar.bind('<Button-1>', lambda event: editar_variaveis(event, lista_buscar_lanches, botao_delete, botao_edit))