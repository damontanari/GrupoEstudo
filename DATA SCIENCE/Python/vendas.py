import pandas as pd

# Importando a base de dados em csv | Alterar caminho se necessário
df = pd.read_csv("C:/Users/daniel.montanari/Desktop/GrupoEstudo/GrupoEstudo/DATA SCIENCE/Planilhas/vendas.csv")
df.head()

# Verificando a quantidade de colunas do dataframe
qtd_colunas = len(list(df.columns))
print(qtd_colunas)

# Verificando a quantidade de linhas do dataframe
qtd_linhas = len(df)
print(qtd_linhas)
