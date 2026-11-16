import json

file = open('dados/vendas.json', 'r')
data = json.load(file)

print(data)

file.close()
