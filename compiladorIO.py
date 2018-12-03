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

def salvaTokes():
    pass