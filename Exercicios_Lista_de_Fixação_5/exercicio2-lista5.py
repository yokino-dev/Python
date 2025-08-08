# Escreva um algoritmo que dada a lista nomes = ["Ana", "Bruno", "Carlos", "Diana"] imprima
# cada nome junto com sua posição (índice), no formato:

# 0 - Ana
# 1 - Bruno
# 2 - Carlos
# 3 - Diana

# Lista com quatro nomes armazenados em sequência
lista = ["Ana", "Bruno", "Carlos", "Diana"]

contador = 0  # Variável para contar a posição (índice) dos nomes na lista, começa em 0

# Loop for que percorre cada elemento da lista, atribuindo cada elemento à variável 'nomes'
for nomes in lista:
    print(contador, nomes)  # Imprime o valor do contador (posição) e o nome atual
    contador += 1  # Incrementa o contador em 1 para a próxima iteração, atualizando o índice
