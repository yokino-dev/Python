# 1. Escreva dois algoritmos que use while e for para imprimir os números de 1 a 10. No caso do for
# faça dois algoritmos: um usando a função range( ) e a outra usando lista.

# LINHA CRIADA PRO GIT RECONHECER ALGUMA ALTERAÇÃO NO CODIGO KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK


# Função que usa o laço while para imprimir números de 1 a 10
def usando_while():
    repeticao = 0  # Inicializa a variável de controle da repetição
    while repeticao < 10:  # Enquanto repeticao for menor que 10, execute o bloco
        repeticao = repeticao + 1  # Incrementa repeticao em 1 a cada iteração
        print(repeticao)  # Imprime o valor atual de repeticao

# Função que usa o laço for com a função range() para imprimir números de 1 a 10
def usando_for_com_range():
    # range(1, 11) gera números de 1 até 10 (11 não incluso)
    for i in range(1, 11):
        print(i)  # Imprime o valor atual da variável i

# Função que usa o laço for com uma lista explícita para imprimir números de 1 a 10
def usando_for_com_lista():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista com os números de 1 a 10
    for i in numeros:  # Itera cada elemento da lista
        print(i)  # Imprime o número atual

# Função principal que apresenta o menu e lê a escolha do usuário
def main():
    print("Bem vindo ao uso prático de estrutura de repetição em Python")  # Mensagem de boas-vindas
    while True:  # Loop infinito para o menu funcionar até o usuário sair
        try:
            # Pede ao usuário que escolha qual estrutura usar, converte resposta para minúsculas e remove espaços
            resposta = input("Qual estrutura gostaria de utilizar? while\n for_range\n for_lista \n sair: ").lower().strip()
            
            if resposta == "while":  # Se o usuário escolher "while"
                usando_while()  # Executa a função que usa while
            
            elif resposta == "for_range":  # Se escolher "for_range"
                usando_for_com_range()  # Executa a função que usa for com range
            
            elif resposta == "for_lista":  # Se escolher "for_lista"
                usando_for_com_lista()  # Executa a função que usa for com lista
            
            elif resposta == "sair":  # Se escolher sair
                print("Encerrando o programa...")  # Mensagem de saída
                break  # Sai do loop infinito, encerrando o programa
            
            else:  # Se a entrada for diferente das opções válidas
                print("Digite algo válido: 'while', 'for_range', 'for_lista' ou 'sair'")  # Mensagem de erro

        except ValueError:  # Caso ocorra erro de valor (não deve acontecer aqui, mas está prevenindo)
            print("Digite corretamente. Tente novamente.")  # Mensagem para tentar novamente

# Bloco que garante que o main será executado apenas se este arquivo for executado diretamente (não importado)
if __name__ == "__main__": 
    main()
