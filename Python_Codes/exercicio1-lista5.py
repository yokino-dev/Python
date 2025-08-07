# 1. Escreva dois algoritmos que use while e for para imprimir os números de 1 a 10. No caso do for
# faça dois algoritmos: um usando a função range( ) e a outra usando lista.

# LINHA CRIADA PRO GIT RECONHECER ALGUMA ALTERAÇÃO NO CODIGO KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK


def usando_while():
    repeticao = 0
    while repeticao < 10:
        repeticao = repeticao + 1
        print(repeticao)
def usando_for_com_range():
    for i in range(1, 11):
        print(i)
def usando_for_com_lista():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in numeros:
        print(i)

def main():
    print("Bem vindo ao uso prático de estrutura de repetição em Python")
    while True:
        try:
            resposta = input("Qual estrutura gostaria de utilizar? while\n for_range\n for_lista \n sair: ").lower().strip()
            if resposta == "while":
                usando_while()
            elif resposta == "for_range":
                usando_for_com_range()
            elif resposta == "for_lista":
                usando_for_com_lista()
            elif resposta == "sair":
                print("Encerrando o programa...")
                break
            else:
                print("Digite algo válido: 'while', 'for_range', 'for_lista' ou 'sair'")
        except ValueError:
            print("Digite corretamente. Tente novamente.")

if __name__ == "__main__": 
    main()