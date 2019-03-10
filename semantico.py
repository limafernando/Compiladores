"""
Classe da pilha de escopo (tabela de símbolos)
"""

class pilhaEscopo:

    def __init__(self): #definição, pilha vazia
        self.pilhaTdS = []
        self.pilhaTipos = []



    def abreEscopo(self):
        self.pilhaTdS.append('$')
        self.pilhaTipos.append('$')

    def fechaEscopo(self):
        for i in pilhaTdS[::-1]:
            
            if i == '$': #remove e para a procura pelo fechamento de escopo
                self.pilhaTdS.pop()
                self.pilhaTipos.pop()
                break
            
            self.pilhaTdS.pop() #vai removendo até achar o $
            self.pilhaTipos.pop() #vai removendo até achar o $

    def inserePilha(self, simbolo, tipo): #inserção
        self.pilhaTdS.append(simbolo)
        self.pilhaTipos.append(tipo)

    def procuraSimbolo(self, simbolo): #procura
        for i in pilhaTdS[::-1]:
            
            if i == simbolo:
                return True

            else:
                return False

    def declaraSimbolo(self, simbolo): #declaração
        for i in pilhaTdS[::-1]:
            
            if i == simbolo:
                return False #simbolo já declarado

            elif i == '$':
                return True #simbolo ainda não declarado no escopo

    def getPilhaTdS(self):
        return self.pilhaTdS

    def getPilhaTipos(self):
        return self.pilhaTipos