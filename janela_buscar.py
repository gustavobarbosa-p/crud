from tkinter import *

from lanche_repositorio import LancheRepositorio

lanche_repositorio = LancheRepositorio()

def buscar_lanche(nome, lista_buscar_lanches):
    lista_buscar_lanches.delete(0, END)

    for lanche in lanche_repositorio.listar():
        if lanche.nome.lower().startswith(nome.get().lower()):
            lista_buscar_lanches.insert(END, lanche, '\n')

def excluir(lista_buscar_lanches):
    variavel = ''
    lista = lista_buscar_lanches.get(ANCHOR)

    for i in lista:
        if i != ' ':
            variavel += i
        else:
            break

    if lista_buscar_lanches.get(ANCHOR) != '\n':
        lanche_repositorio.excluir(variavel)
        lista_buscar_lanches.delete(ANCHOR)

# parei aqui (mostrar no botão excluir o nome do lanche selecionado)
def editar_variaveis(lista_buscar_lanches, botao_delete):
    variavel = ''
    lista = lista_buscar_lanches.get(ANCHOR)

    for i in lista:
        if i != ' ':
            variavel += i
        else:
            break
    print(variavel)
    botao_delete['text'] = f'Excluir {variavel}'

def JanelaBuscar():
    janela_buscar = Toplevel()
    janela_buscar.title('Janela de busca')
    janela_buscar.configure(background="#363636")
    janela_buscar.resizable(False, False)
    janela_buscar.geometry('650x410')

    texto_nome = Label(janela_buscar, text='Digite um nome: ', bg='#4F4F4F', fg='#FFFFFF', font=('Arial Black', 12))
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

    buscar_nome = Button(janela_buscar, text='Buscar', bg='#00FF00', fg='#000000', font=('Arial', 12), command=lambda: buscar_lanche(nome, lista_buscar_lanches))
    buscar_nome.grid(row=0, column=2, padx=10, pady=10)

    sair = Button(janela_buscar, text='Sair', bg='#FF0000', fg='#000000', font=('Arial', 12), command=janela_buscar.destroy)
    sair.grid(row=3, column=2, padx=10, pady=10)

    botao_delete = Button(janela_buscar, text='Excluir', bg='#FF0000', fg='#000000', font=('Arial', 12), command=lambda: excluir(lista_buscar_lanches))
    botao_delete.grid(row=3, column=0, padx=10, pady=10)

    print(lista_buscar_lanches.get(ANCHOR))
    
    janela_buscar.mainloop()

if __name__ == '__main__':
    JanelaBuscar()