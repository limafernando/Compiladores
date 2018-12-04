"""
Classe de token
Cada objeto token possui: string identificadora, classificação e linha que se encontra
"""

class token:

    def __init__(self, sIdentificador, classificacao, nLinha):
        self.sIdentificador = sIdentificador
        self.classificacao = classificacao
        self.nLinha = nLinha

    def getTokenInfo():
        return self.sIdentificador + ' ' + self.classificacao + ' ' + self.nLinha