#EXEMPLO 10 - Ler um arquivo com caracteres acentuados:

arq = open('exemplo10.txt', 'r', encoding = "utf-8")

print(arq.read())

arq.close()