from graficos import grafico_map_estado, grafico_rec_mensal, grafico_rec_estado, grafico_rec_categoria, grafico_rec_vendedor, grafico_rec_vendedor_count

import streamlit as st
import plotly.express as px

from dataset import df
from utils import format_number, df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

st.set_page_config(layout="wide")
st.title("Análise de Vendas :shopping_cart:")

st.sidebar.title("Filtro de vendedores")
filtro_vendedor = st.sidebar.multiselect(
    "Selecione os vendedores", 
    df_vendedores['Vendedor'].unique()
)

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]
    df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
    df_rec_estado = (
        df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']]
        .merge(df_rec_estado, left_on='Local da compra', right_index=True)
        .sort_values('Preço', ascending=False)
    )
    df_rec_mensal = (
        df.set_index('Data da Compra')
        .groupby(pd.Grouper(freq='ME'))['Preço']
        .sum()
        .reset_index()
    )
    df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
    df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name()
    df_rec_categoria = (
        df.groupby('Categoria do Produto')[['Preço']]
        .sum()
        .sort_values('Preço', ascending=False)
    )
    df_vendedores = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))

aba1, aba2, aba3 = st.tabs(["Dataset", "Receita", "Vendedores"])

with aba1:
    st.subheader("Dataset")
    st.dataframe(df)

with aba2:
    st.subheader("Receita")
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric("Receita Total", format_number(df['Preço'].sum(), 'R$'))
        st.plotly_chart(grafico_map_estado, width='stretch')
        st.plotly_chart(grafico_rec_estado, width='stretch')
    with coluna2:
        st.metric("Quantidade de Vendas", format_number(df.shape[0]))
        st.plotly_chart(grafico_rec_mensal, width='stretch')
        st.plotly_chart(grafico_rec_categoria, width='stretch')

    receita_por_produto = df.groupby('Produto')['Preço'].sum().reset_index()
    fig = px.bar(receita_por_produto, x='Produto', y='Preço', title='Receita por produto')
    st.plotly_chart(fig)

with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.subheader("Vendedores")
        st.plotly_chart(grafico_rec_vendedor, width='stretch')
    with coluna2:
        st.subheader("Vendedores")
        st.plotly_chart(grafico_rec_vendedor_count, width='stretch')