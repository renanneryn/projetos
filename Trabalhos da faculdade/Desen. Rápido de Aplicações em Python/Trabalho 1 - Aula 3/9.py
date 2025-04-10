#EXEMPLO 9 - É possível ler cada linha diretamente do arquivo sem readline() e/ou readlines():

arq = open("exemplo9.txt", "r")
for linha in arq:
    print(linha)
arq.close()