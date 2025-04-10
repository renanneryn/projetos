#EXEMPLO 6 - Ler todas as linhas de um arquivo com laço de repetição for:
arq = open('exemplo6.txt', 'r')
for linha in arq:
    print(linha)
arq.close()