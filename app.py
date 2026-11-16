import streamlit as st
import plotly.express as px

from dataset import df

st.set_page_config(layout="wide")
st.title("Análise de Vendas :shopping_cart:")

aba1, aba2, aba3 = st.tabs(["Dataset", "Receita", "Vendedores"])

with aba1:
    st.subheader("Dataset")
    st.dataframe(df)

with aba2:
    st.subheader("Receita")
    receita_total = df['Preço'].sum()
    st.metric("Receita Total", f"R$ {receita_total:,.2f}")

    receita_por_produto = df.groupby('Produto')['Preço'].sum().reset_index()
    fig = px.bar(receita_por_produto, x='Produto', y='Preço', title='Receita por produto')
    st.plotly_chart(fig)

with aba3:
    st.subheader("Vendedores")
    receita_por_vendedor = df.groupby('Vendedor')['Preço'].sum().reset_index()
    fig = px.bar(receita_por_vendedor, x='Vendedor', y='Preço', title='Receita por vendedor')
    st.plotly_chart(fig)