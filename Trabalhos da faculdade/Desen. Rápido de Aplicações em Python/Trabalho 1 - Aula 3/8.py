#EXEMPLO 8 - Abrir um arquivo txt e escrever elementos de uma lista:
arq = open('exemplo8.txt', 'w+')

texto = ["Exemplo 1", "Exemplo 2", "Exemplo 3"]

for linha in texto:
    arq.write(linha)
    arq.write("\n")
arq.close()