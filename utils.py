import pandas as pd

from dataset import df
import streamlit as st
import time


# Formata números grandes: 5871490 -> "R$ 5.87 milhões"
def format_number(value, prefix=''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'


# 1 - Receita por estado (com lat/lon para o mapa)
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
df_rec_estado = (
    df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']]
    .merge(df_rec_estado, left_on='Local da compra', right_index=True)
    .sort_values('Preço', ascending=False)
)

# 2 - Receita mensal ('ME' = fim do mês; o 'M' antigo foi descontinuado no pandas novo)
df_rec_mensal = (
    df.set_index('Data da Compra')
    .groupby(pd.Grouper(freq='ME'))['Preço']
    .sum()
    .reset_index()
)
df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name()

# 3 - Receita por categoria
df_rec_categoria = (
    df.groupby('Categoria do Produto')[['Preço']]
    .sum()
    .sort_values('Preço', ascending=False)
)

# 4 - Vendedores: receita (sum) e quantidade de vendas (count)
df_vendedores = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))

# Função para converter arquivos CSV em DataFrame
# Função para converter o DataFrame em arquivo CSV (para download)
@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def mensagem_sucesso_download():
    success = st.success("Download concluído com sucesso!")
    time.sleep(3)
    success.empty()
