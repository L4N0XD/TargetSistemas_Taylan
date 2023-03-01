import json

# leitura do arquivo JSON
with open("C:/Users/lanin/OneDrive/Área de Trabalho/Projetos/projetos python/dados.json") as json_file:
    dados = json.load(json_file)

# cria uma lista faturamento com valores != de Zero
faturamento = [dado['valor'] for dado in dados if dado['valor'] != 0]

#  calcula a média mensal
media = sum(faturamento) / len(faturamento)

print(f'Menor faturamento diário: R${min(faturamento):.2f}')
print(f'Maior faturamento diário: R${max(faturamento):.2f}')

dias_acima_media = sum(1 for valor in faturamento if valor > media)
print(f'{dias_acima_media} dias com faturamento acima da média mensal de R${media:.2f}')