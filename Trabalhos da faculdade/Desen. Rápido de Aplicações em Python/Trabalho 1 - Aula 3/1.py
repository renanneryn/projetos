# EXEMPLO 1 - Abrir e ler o arquivo "arquivo_jogadoresNFL.txt"

# Abrindo o arquivo no modo leitura
with open("arquivo_jogadoresNFL.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Exibindo o conteúdo do arquivo
print(conteudo)
