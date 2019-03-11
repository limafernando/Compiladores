from compiladorIO import leTokens
from semantico import pilhaEscopo

global tokens, indice, pilhaEscopo, contadorIdentificadores

def main():
    
    global tokens, indice, pilhaEscopo, contadorIdentificadores

    tokens = leTokens()
    indice = 0
    pilhaEscopo = pilhaEscopo()
    contadorIdentificadores = 0

    programa()

def programa():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == 'program':
        indice += 1

        pilhaEscopo.abreEscopo()
        print('abrindo escopo')
        print(pilhaEscopo.getPilhaTdS())
        print(pilhaEscopo.getPilhaTipos())
        
        if tokens[indice].classificacao == 'identificador':
            pilhaEscopo.inserePilhaTdS(tokens[indice].sIdentificador)
            pilhaEscopo.inserePilhaTipos('program')
            print(pilhaEscopo.getPilhaTdS())
            print(pilhaEscopo.getPilhaTipos())
            
            indice += 1

            if tokens[indice].sIdentificador == ';':
                indice += 1

                declaracao_de_variaveis()
                declaracoes_de_subprogramas()
                comando_composto()

                if tokens[indice].sIdentificador != '.':
                    
                    print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador '.'")

                else:
                    print('final:', pilhaEscopo.getPilhaTdS())
                    #print(pilhaEscopo.getPilhaTipos())

            else:
                print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ';'")

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado identificador após 'program'")    
    
    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'program'")

#####################################

def declaracao_de_variaveis():
    
    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == 'var':
        indice += 1

        lista_declaracoes_variaveis()
    
    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'var'")

def lista_declaracoes_variaveis():
    
    global tokens, indice, pilhaEscopo, contadorIdentificadores

    contadorIdentificadores = 0

    lista_de_identificadores()

    if tokens[indice].sIdentificador == ':':
        indice += 1

        tipo()

        print(pilhaEscopo.getPilhaTipos())

        if tokens[indice].sIdentificador == ';':
            indice += 1

            lista_declaracoes_variaveis2()

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um delimitador ';'")

    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um delimitador ':'")

def lista_declaracoes_variaveis2():
    
    global tokens, indice, pilhaEscopo, contadorIdentificadores

    contadorIdentificadores = 0

    if(lista_de_identificadores()):

        if tokens[indice].sIdentificador == ':':
            indice += 1

            tipo()

            print(pilhaEscopo.getPilhaTipos())

            if tokens[indice].sIdentificador == ';':
                indice += 1

                lista_declaracoes_variaveis2()

            else:
                print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um delimitador ';'")

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um delimitador ':'")

def lista_de_identificadores():
    
    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].classificacao == 'identificador':
        
        jaDeclarado = pilhaEscopo.declaraSimbolo(tokens[indice].sIdentificador)

        if jaDeclarado:
            #print(tokens[indice].sIdentificador)
            print(tokens[indice].nLinha + ': ERRO! Semântica inválida. Variável declarada duas vezes no mesmo escopo!')
        
        else:
            pilhaEscopo.inserePilhaTdS(tokens[indice].sIdentificador)
            #pilhaEscopo.inserePilhaTipos('ainda não sei como fazer')
            print(pilhaEscopo.getPilhaTdS())
            #print(pilhaEscopo.getPilhaTipos())

            contadorIdentificadores += 1

            

        indice += 1

        lista_de_identificadores2()

        return True

    else:
        return False

def lista_de_identificadores2():
    
    global tokens, indice, pilhaEscopo, contadorIdentificadores
    
    lista_de_identificadores()

    if tokens[indice].sIdentificador == ',':
        indice += 1

        if tokens[indice].classificacao == 'identificador':
            jaDeclarado = pilhaEscopo.declaraSimbolo(tokens[indice].sIdentificador)

            if jaDeclarado:
                #print(tokens[indice].sIdentificador)
                print(tokens[indice].nLinha + ': ERRO! Semântica inválida. Variável declarada duas vezes no mesmo escopo!')
            
            else:
                pilhaEscopo.inserePilhaTdS(tokens[indice].sIdentificador)
                #pilhaEscopo.inserePilhaTipos('ainda não sei como fazer')
                print(pilhaEscopo.getPilhaTdS())
                #print(pilhaEscopo.getPilhaTipos())
                
                contadorIdentificadores += 1

            indice += 1
            lista_de_identificadores2()

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um identificador após ','")
        

def tipo():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == 'integer':
        
        for i in range(contadorIdentificadores): #insere o tipo das variáveis declaradas
            pilhaEscopo.inserePilhaTipos('integer')
        
        indice += 1

    elif tokens[indice].sIdentificador == 'real':
        
        for i in range(contadorIdentificadores): #insere o tipo das variáveis declaradas
            pilhaEscopo.inserePilhaTipos('real')

        indice += 1

    elif tokens[indice].sIdentificador == 'boolean':
        
        for i in range(contadorIdentificadores): #insere o tipo das variáveis declaradas
            pilhaEscopo.inserePilhaTipos('boolean')

        indice += 1

    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um tipo integer, real ou boolean")

#####################################
def declaracoes_de_subprogramas():
    
    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if(declaracao_de_subprograma()):

        if tokens[indice].sIdentificador == ';':
            indice += 1

            declaracoes_de_subprogramas()

def declaracao_de_subprograma():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == 'procedure':
        indice += 1

        if tokens[indice].classificacao == 'identificador':
            jaDeclarado = pilhaEscopo.declaraSimbolo(tokens[indice].sIdentificador)

            if jaDeclarado:
                #print(tokens[indice].sIdentificador)
                print(tokens[indice].nLinha + ': ERRO! Semântica inválida. Subprograma declarado duas vezes no mesmo escopo!')
            
            else:
                pilhaEscopo.inserePilhaTdS(tokens[indice].sIdentificador)
                pilhaEscopo.inserePilhaTipos('procedure')
                print(pilhaEscopo.getPilhaTdS())
                print(pilhaEscopo.getPilhaTipos())
                pilhaEscopo.abreEscopo()
                print('abrindo escopo')
                print(pilhaEscopo.getPilhaTdS())
                print(pilhaEscopo.getPilhaTipos())

            indice += 1

            argumentos()

            if tokens[indice].sIdentificador == ';':
                indice += 1

                declaracao_de_variaveis()
                declaracoes_de_subprogramas()
                comando_composto()

            else:
                print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um delimitador ';'")

        else: 
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'procedure'")
        
        return True

    else: 
        #print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um delimitador ';'")
        return False

def argumentos():
    
    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == '(':
        indice += 1

        lista_de_parametros()

        if tokens[indice].sIdentificador == ')':
            indice += 1

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ')'")

def lista_de_parametros():
    
    global tokens, indice, pilhaEscopo, contadorIdentificadores

    lista_de_identificadores()

    if tokens[indice].sIdentificador == ':':
        indice += 1
        
        tipo()
        lista_de_parametros2()

    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ':'")

def lista_de_parametros2():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == ';':
        indice += 1
        
        lista_de_identificadores()

        if tokens[indice].sIdentificador == ':':
            indice += 1

            tipo()
            lista_de_parametros2()

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ':'")

def comando_composto():
    
    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == 'begin':
        indice += 1

        comandos_opcionais()

        if tokens[indice].sIdentificador == 'end':
            pilhaEscopo.fechaEscopo()
            print('fechando escopo')
            print(pilhaEscopo.getPilhaTdS())
            print(pilhaEscopo.getPilhaTipos())
            indice += 1
        
        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'end'")
        
        return True

    else:
        #print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'begin'")
        return False

def comandos_opcionais():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    lista_de_comandos()

def lista_de_comandos():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if (comando()):
        lista_de_comandos2()

def lista_de_comandos2():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == ';':
        indice += 1

        comando()

        lista_de_comandos2()

def comando():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    aux = False

    if(variavel()):
        
        if tokens[indice].sIdentificador == ':=':
            indice += 1

            expressao()

            return True

        else:
            aux = True
            indice -= 1

    elif aux == True:

        if(ativacao_de_procedimento()):

            return True

    elif comando_composto():

        return True

    elif tokens[indice].sIdentificador == 'if':
        indice += 1

        expressao()

        if tokens[indice].sIdentificador == 'then':
            indice += 1

            comando()

            parte_else()

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'then'")

        return True

    elif tokens[indice].sIdentificador == 'while':
        indice += 1

        expressao()

        if tokens[indice].sIdentificador == 'do':
            indice += 1

            comando()

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'do'")

        return True

    ######alteração case
    elif tokens[indice].sIdentificador == 'case':
        indice += 1

        seletor()

        if tokens[indice].sIdentificador == 'of':
            indice += 1

            lista_de_seletor()

            if tokens[indice].sIdentificador == 'else':
                indice += 1
                
                if tokens[indice].sIdentificador == ':':
                    indice += 1

                    comando()

                else:
                    print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ':'")

            else:
                print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'else'")

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'of'")

        return True

    else:
        return False

def parte_else():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == 'else':
        indice += 1
        comando()

def variavel():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].classificacao == 'identificador':
        jaDeclarado = pilhaEscopo.procuraSimbolo(tokens[indice].sIdentificador)
        
        if jaDeclarado:
            indice += 1
            return True

        else:
            print(tokens[indice].nLinha + ": ERRO! Erro semântico. Variável utilizada antes de declarada")
    else:
        return False

def ativacao_de_procedimento():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].classificacao == 'identificador':
        indice += 1

        ativacao_de_procedimento2()

        return True

    else:
        return False

def ativacao_de_procedimento2():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == '(':
        indice += 1

        lista_de_expressoes()

        if tokens[indice].sIdentificador == ')':
            indice += 1

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ')'")

def lista_de_expressoes():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    expressao()
    lista_de_expressoes2()

def lista_de_expressoes2():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == ',':
        indice += 1

        expressao()
        lista_de_expressoes2()

def expressao():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    expressao_simples()
    expressao2()

def expressao2():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if(op_relacional()):
        expressao_simples()

def expressao_simples():
    
    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if termo():
        expressao_simples2()

    elif sinal():
        expressao_simples2()

    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um termo ou um sinal")

def expressao_simples2():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if op_aditivo():
        termo()
        expressao_simples2()

def termo():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if fator():
        termo2()
        return True
    else:
        return False

def termo2():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if op_multiplicativo():
        fator()
        termo2()

def fator():

	global tokens, indice, pilhaEscopo, contadorIdentificadores
	
	if tokens[indice].classificacao == "identificador":
		indice += 1
		fator2()
		return True
	
	elif tokens[indice].classificacao == "integer":
		indice += 1
		return True
	
	elif tokens[indice].classificacao == "real":
		indice += 1
		return True
	
	elif tokens[indice].sIdentificador == "true":
		indice += 1
		return True
	
	elif tokens[indice].sIdentificador == "false":
		indice += 1
		return True
	
	elif tokens[indice].sIdentificador == "(":
		indice += 1
		
		expressao()
		
		if tokens[indice].sIdentificador == ")":
			indice += 1
			
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ')'")
			
		return True
	
	elif tokens[indice].sIdentificador == "not":
		indice += 1
		
		fator()
		
		return True
	else:
		#print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um fator")
		return False
		
def fator2():

	global tokens, indice, pilhaEscopo, contadorIdentificadores
	
	if tokens[indice].sIdentificador == "(":
		indice += 1
		
		lista_de_expressoes()
		
		if tokens[indice].sIdentificador == ")":
			indice += 1
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ')'")


def sinal():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == '+':
        indice += 1
        return True

    elif tokens[indice].sIdentificador == '-':
        indice += 1
        return True

    else:
        return False

def op_relacional():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == '=':
        indice += 1
        return True

    elif tokens[indice].sIdentificador == '>':
        indice += 1
        return True

    elif tokens[indice].sIdentificador == '<':
        indice += 1
        return True

    elif tokens[indice].sIdentificador == '>=':
        indice += 1
        return True

    elif tokens[indice].sIdentificador == '<=':
        indice += 1
        return True

    elif tokens[indice].sIdentificador == '<>':
        indice += 1
        return True

    else:
        return False


def op_aditivo():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == '+':
        indice += 1
        return True

    elif tokens[indice].sIdentificador == '-':
        indice += 1
        return True

    elif tokens[indice].sIdentificador == 'or':
        indice += 1
        return True

    else:
        return False

def op_multiplicativo():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador == '*':
        indice += 1
        return True

    elif tokens[indice].sIdentificador == '/':
        indice += 1
        return True

    elif tokens[indice].sIdentificador == 'and':
        indice += 1
        return True

    else:
        return False


######################
#modificação case

def seletor():

    global tokens, indice, pilhaEscopo, contadorIdentificadores
    
    if tokens[indice].classificacao == 'integer':
        indice += 1

    elif tokens[indice].classificacao == 'real':
        indice += 1

    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um tipo integer ou real")

def lista_de_seletor():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    seletor()

    if tokens[indice].sIdentificador == ':':
        indice += 1

        comando()

        lista_de_seletor2()
        
    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ':'")

    

def lista_de_seletor2():

    global tokens, indice, pilhaEscopo, contadorIdentificadores

    if tokens[indice].sIdentificador  == ";":
        indice += 1

        seletor()

        if tokens[indice].sIdentificador == ":":
    	    indice += 1
    
    	    comando()

        else:
    	    print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ':'")


if __name__ == '__main__':
    main()