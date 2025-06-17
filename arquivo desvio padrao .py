import re
import statistics

# Ler o arquivo
with open('log.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Extrair os tempos de execução
tempos = []

for linha in linhas:
    match = re.search(r'Tempo de execução:\s*([\d.]+)', linha)
    if match:
        tempos.append(float(match.group(1)))

# Calcular média e desvio padrão
media = statistics.mean(tempos)
desvio = statistics.stdev(tempos)

print(f'Média do tempo de execução: {media:.2f}')
print(f'Desvio padrão do tempo de execução: {desvio:.2f}')
