import shelve

from lanche import Lanche

class LancheRepositorio:
    def __init__(self):
        self.tabela = 'Lanches'

    def cadastrar(self, lanche):
        banco_de_dados = shelve.open('banco_de_dados')
        try:
            banco_de_dados[self.tabela]
        except:
            banco_de_dados[self.tabela] = []
        
        lista_lanches = banco_de_dados[self.tabela]
        lista_lanches.append(lanche)
        banco_de_dados[self.tabela] = lista_lanches
        banco_de_dados.close()
    
    def listar(self):
        banco_de_dados = shelve.open('banco_de_dados')
        lista_lanches = banco_de_dados[self.tabela]
        banco_de_dados.close()
        return lista_lanches
    
    def buscar(self, nome):
        banco_de_dados = shelve.open('banco_de_dados')
        lista_lanches = banco_de_dados[self.tabela]
        banco_de_dados.close()
        lista_de_busca = []
        
        for lanche in lista_lanches:
            if lanche.nome.lower().startswith(nome.lower()):
                lista_de_busca.append(lanche)

        return lista_de_busca

    def excluir(self, termo):
        banco_de_dados = shelve.open('banco_de_dados')
        lista_lanches = banco_de_dados[self.tabela]

        for lanche in lista_lanches:
            if lanche.nome.lower() == termo.lower():
                lista_lanches.remove(lanche)    
                banco_de_dados[self.tabela] = lista_lanches
                banco_de_dados.close()
                break

    def editar(self, novo_nome, novo_preco):
        banco_de_dados = shelve.open('banco_de_dados')
        lista_lanches = banco_de_dados[self.tabela]

        for lanche in lista_lanches:
            if lanche.nome.lower() == novo_nome.lower():
                lanche.nome = novo_nome
                banco_de_dados[self.tabela] = lista_lanches
                banco_de_dados.close()
                
            if lanche.preco.lower() == novo_preco.lower():
                lista_lanches.preco = novo_preco
                banco_de_dados[self.tabela] = lista_lanches
                banco_de_dados.close()

            return print('Lanche editado com sucesso!')