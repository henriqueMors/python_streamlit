import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

# 1 - Mapa: receita por estado
grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat = 'lat',
    lon = 'lon',
    scope = 'south america',
    size = 'Preço',
    template = 'seaborn',
    hover_name = 'Local da compra',
    hover_data = {'lat': False, 'lon': False},
    title = 'Receita por Estado'
)

# 2 - Linha: receita mensal (uma linha por ano)
grafico_rec_mensal = px.line(
    df_rec_mensal,
    x = 'Mes',
    y = 'Preço',
    markers = True,
    color = 'Ano',
    line_dash = 'Ano',
    title = 'Receita Mensal'
)
grafico_rec_mensal.update_layout(yaxis_title = 'Receita')

# 3 - Barras: top 5 estados
grafico_rec_estado = px.bar(
    df_rec_estado.head(5),
    x = 'Local da compra',
    y = 'Preço',
    text_auto = True,
    title = 'Top Receita por Estado'
)

# 4 - Barras: top 5 categorias
grafico_rec_categoria = px.bar(
    df_rec_categoria.head(5).reset_index(),
    x = 'Categoria do Produto',
    y = 'Preço',
    text_auto = True,
    title = 'Top Receita por Categoria'
)

# 5 - Barras: top 5 vendedores
grafico_rec_vendedor = px.bar(
    df_vendedores[['sum']].sort_values('sum', ascending=False).head(5).reset_index(),
    x = 'sum',
    y = df_vendedores[['sum']].sort_values('sum', ascending=False).head(5).reset_index()['Vendedor'],
    text_auto = True,
    title = 'Top Receita por Vendedor'
)

# 6 - Barras: Top 5 vendedores (quantidade de vendas)
grafico_rec_vendedor_count = px.bar(
    df_vendedores[['count']].sort_values('count', ascending=False).head(5).reset_index(),
    x = 'count',
    y = df_vendedores[['count']].sort_values('count', ascending=False).head(5).reset_index()['Vendedor'],
    text_auto = True,
    title = 'Top Vendedores (Quantidade de Vendas)'
)