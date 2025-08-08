# Crie um programa com o seguinte menu:
# 1 - Mostrar uma mensagem de boas vindas
# 2 - Mostrar data do dia (pesquise como exibir essa informação com Python)
# 0 - Sair

from datetime import datetime  # Importa a classe datetime para trabalhar com data e hora
import os  # Importa o módulo para interagir com o sistema operacional

# Função para limpar a tela do terminal
def limpar():
    if os.name == 'nt':  # Verifica se o sistema operacional é Windows
        os.system('cls')  # Comando para limpar a tela no Windows
    else:
        os.system('clear')  # Comando para limpar a tela em sistemas Unix/Linux/Mac

# Função que limpa a tela e mostra uma mensagem de boas-vindas
def mostrar_boas_vindas():
    limpar()  # Limpa a tela antes de mostrar a mensagem
    print("Seja bem-vindo(a)!")  # Exibe a mensagem de boas-vindas

# Função que mostra a data atual formatada no formato dia/mês/ano
def mostrar_data():
    agora = datetime.now()  # Pega a data e hora atual do sistema
    data_formatada = agora.strftime("%d/%m/%Y")  # Formata a data para o formato desejado
    print(f"Data atual: {data_formatada}")  # Exibe a data formatada

# Função principal que exibe o menu e executa as opções escolhidas pelo usuário
def main():
    while True:  # Loop infinito para o menu funcionar até o usuário escolher sair
        print("\nMenu:")
        print("1 - Mostrar mensagem de boas vindas")
        print("2 - Mostrar data do dia")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")  # Lê a opção do usuário

        if escolha == "1":  # Se o usuário escolher a opção 1
            mostrar_boas_vindas()  # Chama a função que mostra a mensagem de boas-vindas
        elif escolha == "2":  # Se escolher a opção 2
            mostrar_data()  # Chama a função que mostra a data atual
        elif escolha == "0":  # Se escolher a opção 0
            print("Saindo...")  # Mensagem de saída
            break  # Sai do loop, encerrando o programa
        else:  # Caso o usuário digite uma opção inválida
            print("Opção inválida. Tente novamente.")  # Mensagem de erro

# Bloco que garante que a função main() será executada apenas se este arquivo for executado diretamente
if __name__ == "__main__":
    main()
