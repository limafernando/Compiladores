from token import token

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

def leTokens():
    arquivo = open('tokens', 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    tokens = []

    for l in linhas:
        
        aux = l.split(' ')

        if len(aux) == 3:

            identificador = aux[0]
            classificacao = aux[1]
            nLinha = aux[2]
            nLinha = nLinha[0:nLinha.find('\n')] #tira o \n

        else:

            identificador = aux[0]
            classificacao = aux[1]+' '+aux[2]
            nLinha = aux[3]
            nLinha = nLinha[0:nLinha.find('\n')] #tira o \n

        #print(nLinha)

        tkn = token(identificador, classificacao, nLinha)
        tokens.append(tkn)

    return tokens