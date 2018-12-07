import compiladorIO as cio
from token import token
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
