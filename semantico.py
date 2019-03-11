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
        for i in self.pilhaTdS[::-1]:
            
            if i == '$': #remove e para a procura pelo fechamento de escopo
                self.pilhaTdS.pop()
                self.pilhaTipos.pop()
                break
            
            self.pilhaTdS.pop() #vai removendo até achar o $
            self.pilhaTipos.pop() #vai removendo até achar o $

    def inserePilhaTdS(self, simbolo): #inserção
        self.pilhaTdS.append(simbolo)
        
        
    def inserePilhaTipos(self, tipo): #inserção
        self.pilhaTipos.append(tipo)

    def procuraSimbolo(self, simbolo): #procura
        declarada = False
        
        for i in self.pilhaTdS[::-1]:

            #print(i)
            
            if i == simbolo:
                #print('oi')
                declarada = True
                break

            else:
                #print('nao oi')
                declarada = False

        return declarada

    def declaraSimbolo(self, simbolo): #declaração
        for i in self.pilhaTdS[::-1]:
            
            if i == simbolo:
                return True #simbolo já declarado

            elif i == '$':
                return False #simbolo ainda não declarado no escopo

    def getPilhaTdS(self):
        return self.pilhaTdS

    def getPilhaTipos(self):
        return self.pilhaTipos