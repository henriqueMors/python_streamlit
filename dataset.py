import json
import pandas as pd

file = open('dados/vendas.json', 'r')
data = json.load(file)

#print(data)

df = pd.DataFrame(data)
print(df)

file.close()