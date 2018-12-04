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
    conteudoArquivo = arquivo.read()
    arquivo.close()
    conteudoArquivo = conteudoArquivo.split(' ')
    conteudoArquivo[-1] = conteudoArquivo[-1][:-1] #para apagar \n do último elemento

    return conteudoArquivo

def salvaTokes():
    pass