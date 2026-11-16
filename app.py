import streamlit as st
import plotly.express as px

from dataset import df

st.title("Análise de Vendas :shopping_cart:")
st.set_page_config(layout="wide")

aba1, aba2, aba3 = st.tabs(["Dataset", "Receita", "Vendedores"])