# Faça um programa que peça ao usuário para digitar números inteiros e vá somando esses números
# até que o usuário digite zero. Ao final, mostre a soma total.

import time  # Importa o módulo para manipular tempo (pausas)
import os    # Importa o módulo para interagir com o sistema operacional

# Função para limpar a tela do terminal
def limpar():
    if os.name == 'nt':        # Se o sistema for Windows
        os.system('cls')       # Comando para limpar a tela no Windows
    else:
        os.system('clear')     # Comando para limpar a tela em Linux/Mac

limpar()  # Limpa a tela antes de começar

# Mensagem de boas-vindas explicando o funcionamento do programa
print("Bem vindo ao Contador, em breve poderá escolher um número que será somado constantemente até desejar parar e no final \n mostrará o resultado da soma total")

time.sleep(7)  # Pausa o programa por 7 segundos para o usuário ler a mensagem

limpar()  # Limpa a tela para começar a execução do contador

soma = 0  # Inicializa a variável soma com zero

while True:  # Loop infinito para o usuário continuar somando números até desejar parar
    try:
        print("Digite 0 para sair")  # Informa como sair do programa
        numero = int(input("Escolha um número para somar \n"))  # Pede um número ao usuário e converte para inteiro

        # Atenção: aqui há um pequeno erro. numero é inteiro, então a comparação deve ser com 0 (int), não '0' (string)
        if numero == 0:  # Se o número digitado for zero, sai do loop
            break

        else:
            soma += numero  # Soma o número digitado ao total acumulado
            print(f"O valor da soma atual é: {soma}")  # Mostra a soma atualizada
            continue  # Continua para a próxima repetição do loop

    except ValueError:  # Caso o usuário digite algo que não possa ser convertido para inteiro
        print("Digite um valor válido")  # Mostra mensagem de erro
        continue  # Continua o loop pedindo o número novamente



