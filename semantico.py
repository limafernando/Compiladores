"""
Classe da pilha de escopo (tabela de símbolos)
"""

class pilhaEscopo:

    def __init__(self): #definição, pilha vazia
        self.pilhaTdS = []
        self.pilhaTipos = []
        self.pilhaPcT = []



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

###################

    def pushPcT(self, ident, tipo): #Adiciona o tipo utilizado na pilha de tipos para as operações			
        
        if tipo == "variavel":
	
            aux = self.tipoIdentificador(ident)
            
            self.pilhaPcT.append(aux)

        else:
            self.pilhaPcT.append(tipo)
        
        print("Pilha tipo: ")
        print(self.pilhaPcT)
        
        if len(self.pilhaPcT) == 2:
            self.atualizaPcT()	

    def atualizaPcT(self): #Faz a operação de tipos
        
        if self.pilhaPcT[0] == "inteiro" and self.pilhaPcT[1] == "inteiro":
            self.pilhaPcT.pop()
            self.pilhaPcT.pop()
            self.pilhaPcT.append("inteiro")
        
        elif self.pilhaPcT[0] == "real" and self.pilhaPcT[1] == "real":
            self.pilhaPcT.pop()
            self.pilhaPcT.pop()
            self.pilhaPcT.append("real")
        
        elif self.pilhaPcT[0] == "inteiro" and self.pilhaPcT[1] == "real":
            self.pilhaPcT.pop()
            self.pilhaPcT.pop()
            self.pilhaPcT.append("real")
        
        elif self.pilhaPcT[0] == "real" and self.pilhaPcT[1] == "inteiro":
            self.pilhaPcT.pop()
            self.pilhaPcT.pop()
            self.pilhaPcT.append("real")
        
        elif self.pilhaPcT[0] == "logico" and self.pilhaPcT[1] == "logico":
            
            self.pilhaPcT.pop()
            self.pilhaPcT.pop()
            self.pilhaPcT.append("logico")
        
        else:
            
            exit("SEMANTICO ERROR: Incopatibilidade de tipos")
            
            
        print("Pilha de tipos atualizadas: ")
        print(self.pilhaPcT)

    def tipoIdentificador(self, ident): #Retorna o tipo de um identificador da tabela de identificadores
        
        for i in self.pilhaTdS[::-1]:
            
            if i == ident:
                tipo = self.pilhaPcT[self.pilhaEscopo.index(i)]
                return tipo
