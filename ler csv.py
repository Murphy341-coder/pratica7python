import csv

# Ler o arquivo CSV
with open('pessoas.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(f"Nome: {linha['Nome']}, Cidade: {linha['Cidade']}")
