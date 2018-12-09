import string
from token import token

minusculas = list(string.ascii_lowercase)
maiusculas = list(string.ascii_uppercase)
letras = minusculas + maiusculas
numeros = ['0', '1','2','3','4','5','6','7','8','9'] #para fazer a checagem
caracteresValidos = minusculas+maiusculas+numeros+['_']

nLinha = 1 #armazena o numero da linha

classificacao = '' #variavel para guardar a classifição
sIdentificador = '' #variavel para guardar a string identificadora

indiceParada = -1 #variavel para guardar o proximo indice a ser analisado
estaComentado = False

def exe(programa, mapaReservadas, mapaOperadores):#, palavrasReservadas):
    """
    Função que representa o autômato
    Retorna lista de classificação de tokens, 
    cada elemento da lista representa um objeto token
    """

    global minusculas,maiusculas,letras,numeros,caracteresValidos,nLinha,classificacao,sIdentificador,indiceParada,estaComentado
    

    #começa uma lista vazia de objetos token
    #faz o loop do automato
    #loop finalizado -> instancia novo objeto token e add na lista de tokens
    #cria lista de classificação de tokens
    #loop na lista de tokens """token.getTokenInfo()""" adicionando na lista de classificação
    #retorna a lista de classificação

    tokens = []
    erro = False #variável para amazenar estado de erro... se tem erro encerra a análise léxica
    nLinhaAbreComentario = -1


    for ele in programa: #percorre todo o programa linha por linha

        print('\n')
        
        print(ele)
        tam = len(ele)

        print('tam ', tam)
        
        for i in range(0, tam): #estado inicial
            print('aque')
            print(i)
            print(indiceParada)
            if i < indiceParada: #serve para ignorar os caracteres até o caracter no indiceParada
                print('i ', i)
                print(ele[i])
                #pass
            
            else:
                print('here')
                print('ele[i]: ' + ele[i])
                if ele[i] == '\n': #pula linha
                    #precisa ser o primeiro if    
                    nLinha += 1

                elif ele[i] == '\t' or ele[i] == ' ': #tabulação ou espaço, não faz nada
                    pass
                    
                elif ele[i] == '{' or estaComentado: #abre comentario
                    if nLinhaAbreComentario == -1:
                        nLinhaAbreComentario = nLinha
                    
                    pulaLinha = comentario(ele, i, tam)
                    if pulaLinha:
                        break

                elif ele[i] in numeros: #recebeu numero
                    tkn = numero(ele, i, tam)
                    tokens.append(tkn)

                elif ele[i] in letras: #recebeu letra [a..Z]
                    print('letras')
                    tkn = letra(ele, i, tam, mapaReservadas)#, palavrasReservadas)
                    tokens.append(tkn)

                elif ele[i] in list(mapaOperadores.keys()):
                    print('operadores')
                    tkn = operador(ele, i, tam, mapaOperadores)
                    tokens.append(tkn)

                #elif ele[i] == '': #End Of File
                    #pass

                else: #caracteres não permitidos
                    sIdentificador = ele[i]
                    classificacao = 'ERRO: SÍMBOLO NÃO RECONHECIDO'
                    tkn = token(sIdentificador, classificacao, str(nLinha))
                    tokens.append(tkn)
                    erro = True #se tem erro encerra a análise léxica
                    break
            
        if erro:
            break #se tem erro encerra a análise léxica    

        indiceParada = -1 #retorna o valor do proximo indice a ser analisado pro valor inicial de comparação

    if estaComentado:
        sIdentificador = '{'
        classificacao = 'ERRO: COMENTÁRIO ABERTO NA LINHA ' +str(nLinhaAbreComentario)
        
        tkn = token(sIdentificador, classificacao, str(nLinha))
        tokens.append(tkn)
        erro = True #se tem erro encerra a análise léxica

    print('\n')

    classificacaoTokens = []
    for t in tokens:
        print(t.getTokenInfo())
        classificacaoTokens.append(t.getTokenInfo() + '\n')

    return classificacaoTokens

def comentario(ele, i, tam):
    global nLinha, estaComentado, indiceParada
    
    print('comentado')

    estaComentado = True
                    
    for j in range (i, tam): #estado de loop até encontrar o fecha comentário
        print(ele[j])              
        if ele[j] == '}': #encontrou
            print('fechou comentario')
                           
            indiceParada = j+1
            estaComentado = False
                            
            break

        elif ele[j] == '\n': #pula linha no comentário
            print('pulou linha sem fechar comentario')
                            
            nLinha += 1
            indiceParada = -1 #reseta a variavel para começar a varrer a proxima linha
            #break

        '''elif ele[j] == '': #EOF
            print('EOF')
            indiceParada = j
            break   '''                    

    if estaComentado:
        return True

def numero(ele, i, tam):
    global nLinha, numeros, classificacao, indiceParada

    print('é numero')    
    classificacao = 'numero inteiro'
    
    for j in range (i+1, tam): #estado de loop recebendo numeros
                        
        print(ele[j])
        if ele[j] in numeros: #continua recebendo numeros
            print('continua numero inteiro')
                            
            classificacao = 'numero inteiro'
                            
        elif ele[j] == '.': #recebeu um ponto -> numero real
            print('é numero real')

            classificacao = 'numero real'
                            
            for z in range (j+1, tam):
                print('tem casa decimal?')

                if ele[z] in numeros:
                    print('casa decimal')

                    classificacao = 'numero real'

                else:
                    print('acabaram as casas decimais')
                                    
                    indiceParada = z
                    break
                            
            print('fim de numero real')

            sIdentificador = ele[i:z]
            tkn = token(sIdentificador, classificacao, str(nLinha))
            #tokens.append(tkn) 
                            
            break

        else: #nao recebeu mais numero, sai desse estado e volta pro inicial
            print('fim de numero inteiro')

            indiceParada = j

            sIdentificador = ele[i:j]
            tkn = token(sIdentificador, classificacao, str(nLinha))
            #tokens.append(tkn)
                            
            #print(tkn)
                            
            break

    return tkn

def letra(ele, i, tam, mapaReservadas):#, palavrasReservadas):
    global nLinha, caracteresValidos, classificacao, indiceParada

    for j in range(i+1, tam):
        if ele[j] in caracteresValidos:
            pass
        else:
            indiceParada = j
            break

    sIdentificador = ele[i:indiceParada]

    try:
        classificacao = mapaReservadas[sIdentificador]
    except:
        classificacao = 'identificador'

    tkn = token(sIdentificador, classificacao, str(nLinha))

    return tkn
    
def operador(ele, i, tam, mapaOperadores):
    global nLinha, classificacao, indiceParada

    classificado = False
    j = i+1
    
    if ele[i] == ':':
        if ele[j] == '=':
            op = ele[i]+ele[j]
            sIdentificador = op
            classificacao = mapaOperadores[op]
            classificado = True
            indiceParada = j+1 #pula o segundo
    
    elif ele[i] == '<':
        print('menor que')
        if ele[j] == '=':
            op = ele[i]+ele[j]
            sIdentificador = op
            classificacao = mapaOperadores[op]
            classificado = True
            indiceParada = j+1 #pula o segundo
        
        elif ele[j] == '>':
            print('diferente')
            op = ele[i]+ele[j]
            sIdentificador = op
            classificacao = mapaOperadores[op]
            classificado = True
            indiceParada = j+1 #pula o segundo
    
    elif ele[i] == '>':
        if ele[j] == '=':
            op = ele[i]+ele[j]
            sIdentificador = op
            classificacao = mapaOperadores[op]
            classificado = True
            indiceParada = j+1 #pula o segundo
    
    if not classificado:
        sIdentificador = ele[i]
        classificacao = mapaOperadores[ele[i]]

    tkn = token(sIdentificador, classificacao, str(nLinha))

    return tkn