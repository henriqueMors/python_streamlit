from utils import format_number, df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

st.metric("Receita Total", format_number(df['Preço'].sum(), 'R$'))
st.metric("Quantidade de Vendas", format_number(df.shape[0]))