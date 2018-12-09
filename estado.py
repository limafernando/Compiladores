"""
Classe estado
Cada objeto estado possui: um nome, um dicionario com as transições e a classificaçao caso o estado seja final
"""

class estado:

    def __init__(self, nome, transicoes, classificacao):
        self.nome = nome
        self.transicoes = transicoes
        self.classificacao = classificacao