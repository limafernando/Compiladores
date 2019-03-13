from lexico import main as lexico
from sintatico import main as sintatico

def main():

    nomeArq = 'teste'

    lexico(nomeArq)
    
    #print de acompanhamento de programa
    #print()
    
    sintatico()

if __name__ == "__main__":
    main()