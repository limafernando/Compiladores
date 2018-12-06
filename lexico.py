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

    #classificaoTokens = automato(programa)
    #cio.salvaTokens(classificaoTokens)

def automato(programa):
    """
    Função que representa o autômato
    Retorna lista de classificação de tokens, 
    cada elemento da lista representa um objeto token
    """
    
    #começa uma lista vazia de objetos token
    #faz o loop do automato
    #loop finalizado -> instancia novo objeto token e add na lista de tokens
    #cria lista de classificação de tokens
    #loop na lista de tokens """token.getTokenInfo()""" adicionando na lista de classificação
    #retorna a lista de classificação

if __name__ == '__main__':
    main()
