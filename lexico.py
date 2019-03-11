import compiladorIO as cio
from token import token
import automato
import string

def main(nomeArq):
    """
    Função principal do analisador léxico
    Controla as chamadas das funções utilizadas pelo analisador
    """

    programa = cio.lePrograma(nomeArq)
    
    #print de acompanhamento de programa
    #print(programa)

    #print de acompanhamento de programa
    #print('\n')

    mapaReservadas = cio.lePalavrasReservadas()
    #print de acompanhamento de programa
    #print(mapaReservadas)

    mapaOperadores = cio.leOperadoes()
    
    classificacaoTokens = automato.exe(programa, mapaReservadas, mapaOperadores)#, palavrasReservadas)

    cio.salvaTokens(classificacaoTokens)


if __name__ == '__main__':
    main(nomeArq)