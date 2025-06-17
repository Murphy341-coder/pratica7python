import json

# Dados da pessoa
pessoa = {
    'nome': 'Ana Karina',
    'idade': 32,
    'cidade': 'Fortaleza'
}

# Escrever no arquivo JSON
with open('pessoa.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

print('Arquivo JSON criado com sucesso!')

# Ler o arquivo JSON
with open('pessoa.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print('Dados lidos do JSON:')
print(f"Nome: {dados['nome']}")
print(f"Idade: {dados['idade']}")
print(f"Cidade: {dados['cidade']}")
