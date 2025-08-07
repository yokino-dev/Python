# Faça um programa que peça ao usuário para digitar números inteiros e vá somando esses números
# até que o usuário digite zero. Ao final, mostre a soma total.

import time
import os
def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
limpar()
print ("Bem vindo ao Contador, em breve poderá escolher um número que será somado constantemente até desejar parar e no final \n mostrará o resultado da soma total")
time.sleep (7)
limpar()
soma = 0
while True:
    try:
        print ("Digite 0 para sair")
        numero = int(input("Escolha um número para somar \n"))
        if numero == '0':
            break
        else:
            soma += numero
            print(f"O valor da soma atual é: {soma}")
            continue
    except ValueError:
        print("Digite um valor válido")
        continue


