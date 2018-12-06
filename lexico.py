import compiladorIO as cio
from token import token

def main():
    """
    Função principal do analisador léxico
    Controla as chamadas das funções utilizadas pelo analisador
    """

    programa = cio.lePrograma()
    print(programa)

    print('\n')

    mapaReservadas = cio.lePalavrasReservadas()
    print(mapaReservadas)

    automato(programa)

    #classificaoTokens = automato(programa)
    #cio.salvaTokens(classificaoTokens)

def automato(programa):
    """
    Função que representa o autômato
    Retorna lista de classificação de tokens, 
    cada elemento da lista representa um objeto token
    """

    numeros = ['0', '1','2','3','4','5','6','7','8','9'] #para fazer a checagem
    classificacao = '' #variavel para guardar a classifição
    sIdentificador = '' #variavel para guardar a string identificadora

    indiceParada = -1 #variavel para guardar o proximo indice a ser analisado

    nLinha = 1

    #começa uma lista vazia de objetos token
    #faz o loop do automato
    #loop finalizado -> instancia novo objeto token e add na lista de tokens
    #cria lista de classificação de tokens
    #loop na lista de tokens """token.getTokenInfo()""" adicionando na lista de classificação
    #retorna a lista de classificação

    tokens = []

    for ele in programa:

        print('\n')
        
        print(ele)
        tam = len(ele)

        print('tam ', tam)
        
        for i in range (0, tam): #estado inicial
            print('aque')
            
            if i <= indiceParada:
                print('i ', i)
                print(ele[i])
            
            else:
                print('here')
                
                if ele[i] == '\n':
                    nLinha += 1

                elif ele[i] in numeros: #recebeu numero
                    print('é numero')
                    
                    classificacao = 'inteiro'

                    for j in range (i+1, tam):
                        
                        print(ele[j])
                        if ele[j] in numeros:
                            print('continua inteiro')
                            
                            classificacao = 'inteiro'
                            indiceParada = j
                            
                        elif ele[j] == '.':
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

                        else:
                            print('fim de inteiro')

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
