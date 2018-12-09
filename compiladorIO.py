def lePrograma():
    """
    Função para leitura do programa
    Retorna lista com o conteúdo do programa, cada elemento da lista
    é uma linha do arquivo
    """
    
    arquivo = open('programaTeste', 'r')
    #arquivo = open('teste', 'r')
    conteudoArquivo = arquivo.readlines()
    arquivo.close()
    
    return conteudoArquivo

def lePalavrasReservadas():
    """
    Função para carregamento de palavras reservadas
    Retorna lista com de palavras reservadas, cada elemento da lista
    é uma palavra reservada
    """
    
    arquivo = open('palavrasReservadas', 'r')
    conteudoArquivo = arquivo.readlines()
    arquivo.close()

    mapaReservadas = {}
    #palavrasReservadas = []

    for ele in conteudoArquivo:
        aux = ele.split(" ")
        mapaReservadas[aux[0]] = aux[1] + ' ' + aux[2]
        #palavrasReservadas.append(aux[0])

    return mapaReservadas#, palavrasReservadas

def leOperadoes():
    """
    Função para carregamento de operadores
    Retorna lista de operadores, cada elemento da lista
    é um operador
    """
    
    arquivo = open('operadores', 'r')
    conteudoArquivo = arquivo.readlines()
    arquivo.close()

    mapaOperadores = {}

    for ele in conteudoArquivo:
        ele = ele[:-1]
        aux = ele.split(" ")
        try:
            mapaOperadores[aux[0]] = aux[1]+' '+aux[2]
        except:
            mapaOperadores[aux[0]] = aux[1]

    return mapaOperadores

def salvaTokens(classificacaoTokens):
    arquivo = open('tokens', 'w')
    arquivo.writelines(classificacaoTokens)
    arquivo.close()