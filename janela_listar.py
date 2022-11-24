from tkinter import *

from lanche import Lanche
from lanche_repositorio import LancheRepositorio

lanche_repositorio = LancheRepositorio()

def JanelaListar():
    janela_listar = Toplevel()
    janela_listar.title('Janela de listar')
    janela_listar.configure(background="#363636")
    janela_listar.resizable(False, False)
    janela_listar.geometry('520x330')

    texto_nome = Label(janela_listar, text='Lista de lanches: ', bg='#4F4F4F', fg='#FFFFFF', font=('Arial Black', 12))
    texto_nome.grid(row=0, column=1, padx=2, pady=20)

    espaco = Label(janela_listar, text='', bg='#363636', fg='#FFFFFF', font=('Arial', 12))
    espaco.grid(row=1, column=0, padx=9, pady=0)

    lista = Listbox(janela_listar, width=50, height=10, font=('Arial', 12), bg='#1C1C1C', fg='#F5F5F5')
    lista.grid(row=1, column=1)

    scrollbar = Scrollbar(janela_listar) 
    scrollbar.grid(row=1, column=2, sticky='ns')
    scrollbar.config(command=lista.yview)

    for lanche in lanche_repositorio.listar():
        lista.insert(END, lanche, '\n')

    sair = Button(janela_listar, text='Sair', font=('Arial', 12), bg='#FF0000', fg='#000000', command=janela_listar.destroy)
    sair.grid(row=2, column=1, padx=10, pady=10)

    janela_listar.mainloop()

if __name__ == '__main__':
    JanelaListar()