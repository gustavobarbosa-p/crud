from tkinter import *

from janela_cadastro import *
from janela_listar import *
from janela_buscar import *


janela = Tk()
janela.title('CRUD')
janela.configure(background="#363636")
janela.resizable(False, False)
janela.geometry('300x436')
Grid.rowconfigure(janela,0,weight=1)
Grid.columnconfigure(janela,0,weight=1)
Grid.rowconfigure(janela,1,weight=1)

cadastrar = Button(janela, text='Cadastrar', bg='#2E8B57', fg='#000000', font=('Arial', 12), command=JanelaCadastro)
cadastrar.grid(row=0, column=0, padx=20, pady=20, sticky='NSEW')

buscar = Button(janela, text='Buscar', bg='#2E8B57', fg='#000000', font=('Arial', 12), command=JanelaBuscar)
buscar.grid(row=1, column=0, padx=20, pady=20, sticky='NSEW')

listar = Button(janela, text='Listar', bg='#2E8B57', fg='#000000', font=('Arial', 12), command=JanelaListar)
listar.grid(row=2, column=0, padx=20, pady=20, sticky='NSEW')

fechar = Button(janela, text='Fechar Programa', font=('Arial', 12), command=janela.destroy)
fechar.grid(row=3, column=0, padx=20, pady=20, sticky='NSEW')

janela.mainloop()