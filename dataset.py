import json
import pandas as pd


File = open('dados/vendas.json')
data = json.load(File)

# print(data)

df = pd.DataFrame.from_dict(data)

# print(df)

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

File.close()