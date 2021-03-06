"""
Classe da pilha de escopo (tabela de símbolos)
"""

class pilhaEscopo:

    def __init__(self): #definição, pilha vazia
        self.pilhaTdS = []
        self.pilhaTipos = []
        self.pilhaPcT = []
        self.functions = {}



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

    def getPilhaPcT(self):
        return self.pilhaPcT

    def pushFunctions(self, nome, tipoRetorno):
        self.functions[nome] = tipoRetorno

###################

    def pushPcT(self, ident, tipo, linha): #Adiciona o tipo utilizado na pilha de tipos para as operações			
        
        #print('indentificador', ident)
        #print('tipo', tipo)
        #print('linha', linha)

        #print('aqui', ident, self.tipoIdentificador(ident))
        
        if tipo == "variavel":

            if self.tipoIdentificador(ident) == "function":
                #print('AQUIII function')

                aux = self.functions[ident]
                self.pilhaPcT.append(aux)

                #print(tipo)
            else:
	
                aux = self.tipoIdentificador(ident)
            
                self.pilhaPcT.append(aux)

        else:
            self.pilhaPcT.append(tipo)
        
        #print de acompanhamento de programa
        #print("Pilha tipo: ")
        #print(self.pilhaPcT)
        #print(self.pilhaTipos)
        
        if len(self.pilhaPcT) == 2:
            self.atualizaPcT(linha)	

    def atualizaPcT(self, linha): #Faz a operação de tipos
        
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
            print('oi')
        
        elif self.pilhaPcT[0] == "real" and self.pilhaPcT[1] == "inteiro":
            self.pilhaPcT.pop()
            self.pilhaPcT.pop()
            self.pilhaPcT.append("real")
        
        elif self.pilhaPcT[0] == "logico" and self.pilhaPcT[1] == "logico":
            
            self.pilhaPcT.pop()
            self.pilhaPcT.pop()
            self.pilhaPcT.append("logico")

        elif self.pilhaPcT[0] == "function" or self.pilhaPcT[1] == "function":
            #print(linha + ' tem function')
            self.pilhaPcT.pop()
            self.pilhaPcT.pop()
            self.pilhaPcT.append('inteiro')
        
        else:
            #print(self.pilhaPcT[0], self.pilhaPcT[1])
            print(linha + ": ERRO! Semantica inválida. Incopatibilidade de tipos")
            
        #print de acompanhamento de programa   
        #print("Pilha de tipos atualizadas: ")
        #print(self.pilhaPcT)

    def tipoIdentificador(self, ident): #Retorna o tipo de um identificador da tabela de identificadores
        indice = 0
        tipo = ''

        for i in self.pilhaTdS:
            
            if i == ident:
                tipo = self.pilhaTipos[indice]
            
            indice += 1       
        
        return tipo

    def atribuicao(self, var, linha): #Verifica se a atribuição segue as regras da linguagem
        
        #Para a atribuição ser compatível o tipo da variável utilizada deve ser igual ao topo da pilha
        
        #print de acompanhamento de programa
        #print('aq',self.tipoIdentificador(var))
        #print(self.pilhaPcT[0])

        #print(var)

        #print(var, self.tipoIdentificador(var), self.pilhaPcT[0])

        '''if self.tipoIdentificador(var) != self.pilhaPcT[0] and self.pilhaPcT[0] == 'logico':
            self.pilhaPcT[0] = self.tipoIdentificador(var)'''        
        
        if self.tipoIdentificador(var) == self.pilhaPcT[0]:
            #print de acompanhamento de programa
            #print("Atribuição compatível")
            pass

        elif self.tipoIdentificador(var) == 'function':
            #print('aqui')
            pass
                
        else:
           print(linha + ": ERRO! Semantica inválida. Incompatibilidade de tipos na atribuição")

    #Verifica se os tipos utilizados em um operador são os aceitos
    def tipoOperador(self, op, linha):

        #print de acompanhamento de programa
        #print(op)
        #print(self.pilhaPcT[0])

        if op == "+" or op == "-" or op == "*" or op == "/":
            
            if self.pilhaPcT[0] == "inteiro" or self.pilhaPcT[0] == "real":
                #print de acompanhamento de programa
                #print("Operação está sendo realizada com os tipos aceitos")
                pass
            else:
                print(linha + ": ERRO! Semantica inválida. O operador não suporta os tipos utilizados")
                
        elif op == "=" or op == ">" or op == "<" or op == ">=" or op == "<=" or op == "<>":
            
            if self.pilhaPcT[0] == "inteiro" or self.pilhaPcT[0] == "real":
                #print de acompanhamento de programa
                #print("Operação está sendo realizada com os tipos aceitos")
                pass
            else:
                print(linha + ": ERRO! Semantica inválida. O operador não suporta os tipos utilizados")
                
        elif op == "and" or op == "or":
            
            if self.pilhaPcT[0] == "logico":
                #print de acompanhamento de programa
                #print("Operação está sendo realizada com os tipos aceitos")
                pass
            else:
                print(linha + ": ERRO! Semantica inválida. O operador não suporta os tipos utilizados")

    #Limpa a pilha dos tipos quando é terminada uma avaliação
    def limpaPilhaPcT(self):
             
        self.pilhaPcT = []
