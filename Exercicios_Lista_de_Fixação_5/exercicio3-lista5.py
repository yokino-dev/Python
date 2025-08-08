# Escreva um programa que dada a lista notas = [4.5, 6.0, 8.3, 5.9, 9.0, 3.2, 7.5] imprima quantos
# alunos foram aprovados (nota ≥ 6.0) e quantos reprovaram.

import os  # Importa o módulo para interagir com o sistema operacional (limpar tela)

# Lista com as notas dos alunos
notas = [4.5, 6.0, 8.3, 5.9, 9.0, 3.2, 7.5]
# Lista com os nomes dos alunos, posição correspondente às notas acima
nomes = ["Lucas", "Mariana", "Pedro", "Beatriz", "Rafael", "Camila", "Thiago", "Isabela"]

# Função para limpar a tela do terminal
def limpar():
    if os.name == 'nt':  # Verifica se o sistema operacional é Windows (nt = Windows)
        os.system('cls')  # Comando para limpar tela no Windows
    else:
        os.system('clear')  # Comando para limpar tela em sistemas Unix/Linux/Mac

# Função que mostra a relação dos alunos aprovados (nota maior ou igual a 6.0)
def relacao_aprovados():
    # Percorre todos os índices das listas (de 0 até tamanho das notas - 1)
    for i in range(len(notas)):  
        # Verifica se a nota atual é maior ou igual a 6.0
        if notas[i] >= 6.0:
            print(nomes[i], notas[i])  # Imprime o nome e a nota do aluno aprovado

# Função que mostra a relação dos alunos reprovados (nota menor que 6.0)
def relacao_reprovados():
    for i in range(len(notas)):
        if notas[i] < 6.0:
            print(nomes[i], notas[i])  # Imprime o nome e a nota do aluno reprovado

# Função que mostra a relação geral de todos os alunos e suas notas
def relacao_geral():
    for i in range(len(notas)):
        print(nomes[i], notas[i])  # Imprime o nome e a nota do aluno, independentemente do resultado

# Função principal que apresenta um menu para o usuário escolher o que deseja fazer
def main():
    while True:  # Loop infinito até o usuário escolher sair
        print("\nEscolha uma opção:")
        print("1 - Mostrar aprovados")
        print("2 - Mostrar reprovados")
        print("3 - Mostrar relação geral")
        print("4 - Sair")
        escolha = input("Opção: ")  # Lê a opção do usuário

        if escolha == "1":
            limpar()  # Limpa a tela antes de mostrar os aprovados
            relacao_aprovados()
        elif escolha == "2":
            limpar()  # Limpa a tela antes de mostrar os reprovados
            relacao_reprovados()
        elif escolha == "3":
            limpar()  # Limpa a tela antes de mostrar a relação geral
            relacao_geral()
        elif escolha == "4":
            limpar()
            print("Saindo...")  # Mensagem de saída
            break  # Encerra o loop e finaliza o programa
        else:
            print("Opção inválida, tente novamente.")  # Mensagem de erro para opção inválida

# Verifica se este arquivo está sendo executado diretamente (e não importado)
if __name__ == "__main__":
    main()  # Executa a função principal
