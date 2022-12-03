from tkinter import *

from janela_cadastro import *
from janela_buscar import *

janela = Tk()
janela.title('CRUD')
janela.configure(background="#000000")
janela.resizable(False, False)
janela.geometry('300x436')
Grid.rowconfigure(janela,0,weight=1)
Grid.columnconfigure(janela,0,weight=1)
Grid.rowconfigure(janela,1,weight=1)

cadastrar = Button(janela, text='Cadastrar um Lanche', fg='#32CD32', bg='#000000', font=('Arial Black', 15), command=JanelaCadastro)
cadastrar.grid(row=0, column=0, padx=20, pady=20, sticky='NSEW')

buscar = Button(janela, text='Buscar um Lanche', fg='#32CD32', bg='#000000', font=('Arial Black', 15), command=JanelaBuscar)
buscar.grid(row=1, column=0, padx=20, pady=20, sticky='NSEW')

fechar = Button(janela, text='Fechar Programa', fg='#FF0000', bg='#000000', font=('Arial Black', 12), command=janela.destroy)
fechar.grid(row=2, column=0, padx=20, pady=20, sticky='NSEW')

janela.mainloop()