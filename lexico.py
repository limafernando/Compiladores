import compiladorIO as cio
from token import token
import automato
import string

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
    #print(palavrasReservadas)

    mapaOperadores = cio.leOperadoes()
    
    classificacaoTokens = automato.exe(programa, mapaReservadas, mapaOperadores)#, palavrasReservadas)
    
    cio.salvaTokens(classificacaoTokens)	
 
if __name__ == '__main__':
    main()
