import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from chart import chart_map_estado, chart_rec_mensal, chart_rec_estado, chart_rec_categoria, chart_rec_vendedores, chart_vendas_vendedores


st.set_page_config(layout='wide', page_title="Gráficos", page_icon="📊")
st.title("Dashboard de Vendas 🛒")

st.sidebar.title('Filtro de Vendedores')

filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique()
)

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]

aba1, aba2, aba3 = st.tabs(['Receita', 'Vendedores', 'Dataset'])
with aba3:
    st.dataframe(df)
with aba1:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))
        st.plotly_chart(chart_map_estado, use_container_width=True)
        st.plotly_chart(chart_rec_estado, use_container_width=True)
    with coluna2:
        st.metric('Quantidade Vendas', format_number(df.shape[0]))
        st.plotly_chart(chart_rec_mensal, use_container_widht=True)
        st.plotly_chart(chart_rec_categoria, use_container_widht=True)

with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(chart_rec_vendedores)
    with coluna2:
        st.plotly_chart(chart_vendas_vendedores)

