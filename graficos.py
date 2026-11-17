import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat='lat',
    lon='lon',
    scope='south america',
    size='Preço',
    template='seaborn',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False},
    title='Receita por estado'
)