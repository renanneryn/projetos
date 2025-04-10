#EXEMPLO 7 - Ler todas as linhas de um arquivo com o for e separar as palavras de cada linha com o método split():

arq = open('exemplo7.txt', 'r')
for linha in arq:
    print(linha.split())
arq.close()