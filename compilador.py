from lexico import main as lexico
from sintatico import main as sintatico

def main():

    nomeArq = 'programaTesteSemantico'

    lexico(nomeArq)
    print()
    sintatico()

if __name__ == "__main__":
    main()