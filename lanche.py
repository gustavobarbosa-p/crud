class Lanche:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome}-----R${self.preco} reais'
    
    def __repr__(self):
        return str(self)