import csv

# Dados das pessoas
pessoas = [
    {'Nome': 'Ana', 'Idade': 32, 'Cidade': 'Fortaleza'},
    {'Nome': 'Carlos', 'Idade': 28, 'Cidade': 'São Paulo'},
    {'Nome': 'Mariana', 'Idade': 24, 'Cidade': 'Recife'}
]

# Criar o arquivo CSV
with open('pessoas.csv', 'w', newline='', encoding='utf-8') as arquivo:
    campos = ['Nome', 'Idade', 'Cidade']
    escritor = csv.DictWriter(arquivo, fieldnames=campos)

    escritor.writeheader()
    for pessoa in pessoas:
        escritor.writerow(pessoa)

print('Arquivo CSV criado com sucesso!')
