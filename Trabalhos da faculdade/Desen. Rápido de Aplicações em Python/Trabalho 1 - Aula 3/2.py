# EXEMPLO 2 - Criar e ler um arquivo sem usar 'with'

# Criando e escrevendo no arquivo (sem 'with')
arquivo = open("exemplo2.txt", "w", encoding="utf-8")
arquivo.write("Arquivo criado sem utilizar 'with'.\n")
arquivo.write("Tem que fechar manualmente.\n")
arquivo.close()  # Fechando manualmente

# Lendo o conteúdo (também sem 'with')
arquivo = open("exemplo2.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
arquivo.close()

# Exibindo o conteúdo
print(conteudo)