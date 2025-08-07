# Crie um programa com o seguinte menu:
# 1 - Mostrar uma mensagem de boas vindas
# 2 - Mostrar data do dia (pesquise como exibir essa informação com Python)
# 0 - Sair

from datetime import datetime
import os
def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_boas_vindas():
    limpar()
    print("Seja bem-vindo(a)!")

def mostrar_data():
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y")
    print(f"Data atual: {data_formatada}")

def main():
    while True:
        print("\nMenu:")
        print("1 - Mostrar mensagem de boas vindas")
        print("2 - Mostrar data do dia")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mostrar_boas_vindas()
        elif escolha == "2":
            mostrar_data()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()