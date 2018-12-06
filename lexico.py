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

    numeros = ['1','2','3','4','5','6','7','8','9'] #para fazer a checagem
    classificacao = '' #variavel para guardar a classifição

    indiceParada = -1 #variavel para guardar o proximo indice a ser analisado

    #começa uma lista vazia de objetos token
    #faz o loop do automato
    #loop finalizado -> instancia novo objeto token e add na lista de tokens
    #cria lista de classificação de tokens
    #loop na lista de tokens """token.getTokenInfo()""" adicionando na lista de classificação
    #retorna a lista de classificação

    tokens = []

    for ele in programa:
        
        tam = len(ele)
        
        for i in range (0, tam): #estado inicial
            
            if i <= indiceParada:
                pass
            
            else:
                print('here')
                if ele[i] in numeros: #recebeu numero
                    print('here')
                    classificacao = 'inteiro'

                    for j in range (i+1, tam):
                        
                        if ele[j] in numeros:
                            classificacao = 'inteiro'
                            indiceParada = j
                        
                        elif ele[j] == '.':
                            classificacao = 'float'
                            print('float')

                            for z in range (j+1, tam):
                                
                                if ele[z] in numeros:
                                    classificacao = 'float'

                                else:
                                    indiceParada = z
                                    break

                            tkn = token('af', classificacao, '1')
                            tokens.append(tkn) 
                            
                            break

                        else:
                            tkn = token('af', classificacao, '1')
                            tokens.append(tkn)
                            print(tkn)
                            
                            break

                else:
                    pass
    print('\n')
    
    for t in tokens:
        print(t.getTokenInfo())

if __name__ == '__main__':
    main()
