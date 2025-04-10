# EXEMPLO 5 - Ler todas as linhas de um arquivo em uma list com o readlines().
arq = open('exemplo5.txt', 'r')
print(arq.readlines())
arq.close()