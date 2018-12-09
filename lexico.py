import compiladorIO as cio
from token import token
from automato import automato
import string

def main():
    """
    Função principal do analisador léxico
    Controla as chamadas das funções utilizadas pelo analisador
    """

    programa = cio.lePrograma()
    print(programa)

    print('\n')

    mapaReservadas, palavrasReservadas = cio.lePalavrasReservadas()
    print(mapaReservadas)

	

    automato(programa, mapaReservadas, palavrasReservadas)

    #classificaoTokens = automato(programa)
    #cio.salvaTokens(classificaoTokens)
	
	
def execucao(programa, mapaReservada, palavrasReservadas, automato):

	estadoAtual = q0
	estadoAnterior = None
	indiceCaractere = 0
	
	temTransicao = False
	transicao = {}
	
	dictEstados = {
		'q0' : q0, 'q1' : q1, 'q2' : q2, 'q3' : q3, 'q4' : q4, 'q5' : q5, 'q6' : q6, 'q7' : q7, 'q8' : q8, 'q9' : q9, 'q10' : q10, 'q11' : q11, 'q12' : q12,
		'q13' : q13, 'q14' : q14, 'q15' : q15, 'q16' : q16, 'q17' : q17, 'q18' : q18, 'q19' : q19, 'q20' : q20, 'q21' : q21}
		
	for linha in programa:
		
		while (indiceCaractere < len(linha)):
		
			if estadoAtual.nome == automato.estadoInicial:
				inicio = linha[i]
		
			#Percorrer as transições do estado atual
			for t in estadoAtual.transicoes.keys():
				#Esse caractere está nessa transicao?
				if linha[indiceCaractere] in estadoAtual.transicoes[t]:
					 temTransicao = True
					 transicao = t
				
			if temTransicao:	
				if estadoAtual in automato.estadosFinais:
					estadoAnterior = estadoAtual:
					
					#Atualiza o estado que essa transicao indica
					estadoAtual = dictEstados[transicao]
			else:
				if estadoAtual in automato.estadosFinais:
					sIdentificador = linha[inicio:i]
                    tkn = token(sIdentificador, estadoAtual.classificacao, str(nLinha))
                    tokens.append(tkn)
				else:
					sIdentificador = linha[inicio:i]
                    tkn = token(sIdentificador, estadoAnterior.classificacao, str(nLinha))
                    tokens.append(tkn)
				i -= 1
				estadoAtual = automato.estadoInicial
			
			i += 1
		
		contLinha += 1

def automato(programa, mapaReservadas, palavrasReservadas):
    """
    Função que representa o autômato
    Retorna lista de classificação de tokens, 
    cada elemento da lista representa um objeto token
    """

    minusculas = list(string.ascii_lowercase)
    maiusculas = list(string.ascii_uppercase)
    numeros = ['0', '1','2','3','4','5','6','7','8','9'] #para fazer a checagem

    caracteresValidos = minusculas+maiusculas+numeros+['_']

    classificacao = '' #variavel para guardar a classifição
    sIdentificador = '' #variavel para guardar a string identificadora

    indiceParada = -1 #variavel para guardar o proximo indice a ser analisado

    nLinha = 1 #armazena o numero da linha

    estaComentado = False

    #começa uma lista vazia de objetos token
    #faz o loop do automato
    #loop finalizado -> instancia novo objeto token e add na lista de tokens
    #cria lista de classificação de tokens
    #loop na lista de tokens """token.getTokenInfo()""" adicionando na lista de classificação
    #retorna a lista de classificação

    tokens = []

    for ele in programa: #percorre todo o programa linha por linha

        print('\n')
        
        print(ele)
        tam = len(ele)

        print('tam ', tam)
        
        for i in range (0, tam): #estado inicial
            print('aque')
            
            if i < indiceParada: #serve para ignorar os caracteres até o caracter no indiceParada
                print('i ', i)
                print(ele[i])
                #pass
            
            else:
                print('here')
                
                if ele[i] == '\n': #pula linha
                    print('pulei linha')
                    #precisa ser o primeiro if
                    nLinha += 1

                elif ele[i] == '\t': #tabulação, não faz nada
                    pass
                
                elif ele[i] == '{' or estaComentado: #abre comentario
                    print('comentado')

                    estaComentado = True
                    
                    for j in range (i+1, tam): #estado de loop até encontrar o fecha comentário
                        
                        if ele[j] == '}': #encontrou
                            print('fechou comentario')
                            
                            indiceParada = j
                            estaComentado = False
                            
                            break

                        elif ele[j] == '\n': #pula linha no comentário
                            print('pulou linha sem fechar comentario')
                            
                            nLinha += 1
                            indiceParada = -1 #reseta a variavel para começar a varrer a proxima linha
                            #break

                    if estaComentado: #se o loop encerrou e está comentado, pulou linha    
                        break










                
                
                    

                elif ele[i] in numeros: #recebeu numero
                    print('é numero')
                    
                    classificacao = 'inteiro'

                    for j in range (i+1, tam): #estado de loop recebendo numeros
                        
                        print(ele[j])
                        if ele[j] in numeros: #continua recebendo numeros
                            print('continua inteiro')
                            
                            classificacao = 'inteiro'
                            
                        elif ele[j] == '.': #recebeu um ponto -> float
                            print('é float')

                            classificacao = 'float'
                            
                            for z in range (j+1, tam):
                                print('tem casa decimal?')

                                if ele[z] in numeros:
                                    print('casa decimal')

                                    classificacao = 'float'

                                else:
                                    print('acabaram as casas decimais')
                                    
                                    indiceParada = z
                                    break
                            
                            print('fim de float')

                            sIdentificador = ele[i:z]
                            tkn = token(sIdentificador, classificacao, str(nLinha))
                            tokens.append(tkn) 
                            
                            break

                        else: #nao recebeu mais numero, sai desse estado e volta pro inicial
                            print('fim de inteiro')

                            indiceParada = j

                            sIdentificador = ele[i:j]
                            tkn = token(sIdentificador, classificacao, str(nLinha))
                            tokens.append(tkn)
                            
                            #print(tkn)
                            
                            break

                else:
                    pass

        indiceParada = -1 #retorna o valor do proximo indice a ser analisado pro valor inicial de comparação

    print('\n')
    
    for t in tokens:
        print(t.getTokenInfo())

if __name__ == '__main__':
    main()
