from lanche import Lanche
from lanche_repositorio import LancheRepositorio

lanche_repositorio = LancheRepositorio()

nome = 'teste'
preco = '101'
obj1 = Lanche(nome, preco)
lanche_repositorio.cadastrar(obj1)

# depois que rodar esse arquivo pela primeira vez, pode excluir ele e rodar o arquivo main_window.py