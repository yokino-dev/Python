# Escreva um algoritmo que dada a lista nomes = ["Ana", "Bruno", "Carlos", "Diana"] imprima
# cada nome junto com sua posição (índice), no formato:

# 0 - Ana
# 1 - Bruno
# 2 - Carlos
# 3 - Diana

lista =  ["Ana", "Bruno", "Carlos","Diana"]

contador = 0
for nomes in lista:
    print (contador, nomes)
    contador += 1
