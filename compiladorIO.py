def lePrograma():
    """
    Função para leitura do programa
    Retorna lista com o conteúdo do programa, cada elemento da lista
    é uma linha do arquivo
    """
    
    arquivo = open('programaTeste', 'r')
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

    for ele in conteudoArquivo:
        aux = ele.split(" ")
        mapaReservadas[aux[0]] = aux[1] + ' ' + aux[2]

    return mapaReservadas

def salvaTokes():
    pass