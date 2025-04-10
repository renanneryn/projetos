# EXEMPLO 4 - Ler a linha de um arquivo com o readline().

# Lendo as linhas do arquivo TXT
arq = open("exemplo4.txt", "r")
print(arq.readline())
print(arq.readline())
print(arq.readline())
print(arq.readline())
print(arq.readline())
print(arq.readline())
arq.close()

# Lendo os 3 primeiros digitos 
arq = open("exemplo4.txt", "r")
print(arq.readline(3))
arq.close()

