from compiladorIO import leTokens

global tokens, indice

def main():
    
    global tokens, indice

    tokens = leTokens()
    indice = 0

    programa()

def programa():

    global tokens, indice

    if tokens[indice].sIdentificador == 'program':
        indice += 1
        
        if tokens[indice].classificacao == 'identificador':
            indice += 1

            if tokens[indice].sIdentificador == ';':
                indice += 1

                declaracao_de_variaveis()
                declaracoes_de_subprogramas()
                comando_composto()

                if tokens[indice].sIdentificador != '.':
                    
                    print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador '.'")

            else:
                print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ';'")

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado identificador após 'program'")    
    
    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'program'")

#####################################

def declaracao_de_variaveis():
    
    global tokens, indice

    if tokens[indice].sIdentificador == 'var':
        indice += 1

        lista_declaracoes_variaveis()
    
    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'var'")

def lista_declaracoes_variaveis():
    
    global tokens, indice

    lista_de_identificadores()

    if tokens[indice].sIdentificador == ':':
        indice += 1

        tipo()

        if tokens[indice].sIdentificador == ';':
            indice += 1

            lista_de_identificadores2()

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um delimitador ';'")

    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um delimitador ':'")

def lista_declaracoes_variaveis2():
    
    global tokens, indice

    if(lista_de_identificadores()):

        if tokens[indice].sIdentificador == ':':
            indice += 1

            tipo()

            if tokens[indice].sIdentificador == ';':
                indice += 1

                lista_de_identificadores2()

            else:
                print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um delimitador ';'")

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um delimitador ':'")

def lista_de_identificadores():
    
    global tokens, indice

    if tokens[indice].classificacao == 'identificador':
        indice += 1

        lista_de_identificadores2()

        return True

    else:
        return False

def lista_de_identificadores2():
    
    global tokens, indice
    
    lista_de_identificadores()

    if tokens[indice].sIdentificador == ',':
        indice += 1

        if tokens[indice].classificacao == 'identificador':
            indice += 1
            lista_de_identificadores2()

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um identificador após ','")
        
    else:
        #print('token:', tokens[indice].getTokenInfo())
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ','")

def tipo():

    global tokens, indice

    if tokens[indice].sIdentificador == 'integer':
        indice += 1

    elif tokens[indice].sIdentificador == 'real':
        indice += 1

    elif tokens[indice].sIdentificador == 'boolean':
        indice += 1

    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um tipo integer, real ou boolean")

#####################################
def declaracoes_de_subprogramas():
    
    global tokens, indice

    if(declaracao_de_subprograma()):

        if tokens[indice].sIdentificador == ';':
            indice += 1

            declaracoes_de_subprogramas()

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um delimitador ';'")

def declaracao_de_subprograma():

    global tokens, indice

    if tokens[indice].sIdentificador == 'procedure':
        indice += 1

        if tokens[indice].classificacao == 'identificador':
            indice += 1

            argumentos()

            if tokens[indice].sIdentificador == ';':
                indice += 1

                declaracao_de_variaveis()
                declaracoes_de_subprogramas()
                comando_composto()

            else:
                print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um delimitador ';'")
                indice += 1

        else: 
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'procedure'")
        
        return True

    else: 
        #print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um delimitador ';'")
        return False

def argumentos():
    
    global tokens, indice

    if tokens[indice].sIdentificador == '(':
        indice += 1

        lista_de_parametros()

        if tokens[indice].sIdentificador == ')':
            indice += 1

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ')'")

    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador '('")

def lista_de_parametros():
    
    global tokens, indice

    lista_de_identificadores()

    if tokens[indice].sIdentificador == ':':
        indice += 1
        
        tipo()
        lista_de_parametros2()

    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ':'")

def lista_de_parametros2():

    global tokens, indice

    if tokens[indice].sIdentificador == ';':
        indice += 1
        
        lista_de_identificadores()

        if tokens[indice].sIdentificador == ':':
            indice += 1

            tipo()
            lista_de_parametros2()

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ':'")

    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ';'")

def comando_composto():
    
    global tokens, indice

    if tokens[indice].sIdentificador == 'begin':
        indice += 1

        comandos_opcionais()

        if tokens[indice].sIdentificador == 'end':
            indice += 1
        
        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'end'")

    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'begin'")

def comandos_opcionais():

    global tokens, indice

    lista_de_comandos()

def lista_de_comandos():

    global tokens, indice

    if (comando()):
        lista_de_comandos2()

def lista_de_comandos2():

    global tokens, indice

    if tokens[indice].sIdentificador == ';':
        indice += 1

        comando()

        lista_de_comandos2()

def comando():

    global tokens, indice

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

    else:
        return False

def parte_else():

    global tokens, indice

    if tokens[indice].sIdentificador == 'else':
        indice += 1
        comando()

def variavel():

    global tokens, indice

    if tokens[indice].classificacao == 'identificador':
        indice += 1
        return True
    else:
        return False

def ativacao_de_procedimento():

    global tokens, indice

    if tokens[indice].classificacao == 'identificador':
        indice += 1

        ativacao_de_procedimento2()

        return True

    else:
        return False

def ativacao_de_procedimento2():

    global tokens, indice

    if tokens[indice].sIdentificador == '(':
        indice += 1

        lista_de_expressoes()

        if tokens[indice].sIdentificador == ')':
            indice += 1

        else:
            print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ')'")

def lista_de_expressoes():

    global tokens, indice

    expressao()
    lista_de_expressoes2()

def lista_de_expressoes2():

    global tokens, indice

    if tokens[indice].sIdentificador == ',':
        indice += 1

        expressao()
        lista_de_expressoes2()

def expressao():

    global tokens, indice

    expressao_simples()
    expressao2()

def expressao2():

    global tokens, indice

    if(op_relacional()):
        expressao_simples()

def expressao_simples():
    
    global tokens, indice

    if termo():
        expressao_simples2()

    elif sinal():
        expressao_simples2()

    else:
        print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um termo ou um sinal")

def expressao_simples2():

    global tokesn, indice

    if op_aditivo():
        termo()
        expressao_simples2()

def termo():

    global tokens, indice

    if fator():
        termo2()
        return True
    else:
        return False

def termo2():

    global tokens, indice

    if op_multiplicativo():
        fator()
        termo2()

def fator():

	global tokens, indice
	
	if tokens[indice].classificacao == "identificador":
		indice += 1
		fator2()
		return True
	
	elif tokens[indice].classificacao == "numero inteiro":
		indice += 1
		return True
	
	elif tokens[indice].classificacao == "numero real":
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

	global tokens, indice
	
	if tokens[indice].sIdentificador == "(":
		indice += 1
		
		lista_de_expressoes()
		
		if tokens[indice].sIdentificador == ")":
			indice += 1
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ')'")


def sinal():

    global tokens, indice

    if tokens[indice].sIdentificador == '+':
        indice += 1
        return True

    elif tokens[indice].sIdentificador == '-':
        indice += 1
        return True

    else:
        return False

def op_relacional():

    global tokens, indice

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

    global tokens, indice

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

    global tokens, indice

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

if __name__ == '__main__':
    main()