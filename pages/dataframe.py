import streamlit as st
import pandas as pd
from dataset import df

st.title("Dataset de Vendas :shopping_cart:")

with st.expander("Visualizar Colunas"):
    colunas = st.multiselect(
        "Selecione as colunas",
        df.columns.tolist(),
        default=df.columns.tolist()
    )

st.sidebar.title("Filtros")

with st.sidebar.expander("Categoria do Produto"):
    categorias = st.multiselect(
        "Selecione as categorias",
        df['Categoria do Produto'].unique(),
        df['Categoria do Produto'].unique()
    )

with st.sidebar.expander("Preço do Produto"):
    preco = st.slider(
        "Selecione o Preço",
        min_value=df['Preço'].min(),
        max_value=df['Preço'].max(),
        value=(df['Preço'].min(), df['Preço'].max())
    )

with st.sidebar.expander("Data da Compra"):
    data = st.date_input(
        "Selecione a Data",
        value=(df['Data da Compra'].min(), df['Data da Compra'].max()),
        min_value=df['Data da Compra'].min(),
        max_value=df['Data da Compra'].max()
    )

filtro = (
    (df['Categoria do Produto'].isin(categorias)) &
    (df['Preço'].between(preco[0], preco[1])) &
    (df['Data da Compra'].between(pd.to_datetime(data[0]), pd.to_datetime(data[1])))
)

df_filtrado = df[filtro]
df_filtrado = df_filtrado[colunas]

st.dataframe(df_filtrado)

st.dataframe(df.loc[filtro])