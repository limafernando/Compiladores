"""
Classe automato
Cada objeto automato possui: lista com os nós (estados), o estado inicial e uma lista com os estados finais
Só existe um objeto automato
"""

class automato:

    def __init__(self, estados, estadoInicial, estadosFinais):
        self.estados = estados
        self.estadoInicial = estadoInicial
        self.estadosFinais = estadosFinais