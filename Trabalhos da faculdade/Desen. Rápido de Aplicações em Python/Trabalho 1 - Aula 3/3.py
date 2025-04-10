# EXEMPLO 3 - Criar, adicionar e ler arquivo com 'with'

with open("exemplo3.txt", "w",) as arq:
    arq.write("Texto inicial.\n")
    arq.write("Texto 2\n")

#lendo
with open("exemplo3.txt", "r",) as arq:
    print(arq.read())

with open("exemplo3.txt", "a",) as arq:
    arq.write('texto3')


