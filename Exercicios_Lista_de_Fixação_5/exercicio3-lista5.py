# Escreva um programa que dada a lista notas = [4.5, 6.0, 8.3, 5.9, 9.0, 3.2, 7.5] imprima quantos
# alunos foram aprovados (nota ≥ 6.0) e quantos reprovaram.

import os

notas = [4.5, 6,0, 8.3, 5.9, 9.0, 3.2, 7.5]
nomes = ["Lucas", "Mariana", "Pedro", "Beatriz", "Rafael", "Camila", "Thiago", "Isabela"]
def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
def relacao_aprovados():
    for i in range(len(notas)):                        # len(notas) retorna quantos elementos existem na lista 'notas'
        if notas[i] >= 6.0:
            print (nomes[i],notas[i])                 # Usamos isso para percorrer todos os índices das listas 'notas' e 'nomes'
                                                    # range cria uma sequência de números inteiros, que você pode usar para repetir um código várias vezes.
def relacao_reprovados():
    for i in range(len(notas)):
        if notas[i] < 6.0:
            print (nomes[i],notas[i])

def relacao_geral():
    for i in range(len(notas)):
        print (nomes[i],notas[i])

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Mostrar aprovados")
        print("2 - Mostrar reprovados")
        print("3 - Mostrar relação geral")
        print("4 - Sair")
        escolha = input("Opção: ")

        if escolha == "1":
            limpar()
            relacao_aprovados()
        elif escolha == "2":
            limpar()
            relacao_reprovados()
        elif escolha == "3":
            limpar()
            relacao_geral()
        elif escolha == "4":
            limpar()
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()