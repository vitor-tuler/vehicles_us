import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv') # lendo os dados

mediana_hodometro = car_data['odometer'].median()
car_data['odometer'].fillna(mediana_hodometro, inplace=True)

mediana_ano = car_data['model_year'].median()
car_data['model_year'].fillna(mediana_ano, inplace=True)

mediana_cilindros = car_data['cylinders'].median()
car_data['cylinders'].fillna(mediana_cilindros, inplace=True)
car_data['cylinders'] = car_data['cylinders'].astype(int)

car_data['paint_color'].fillna('Unknown', inplace=True)

st.header('Dashboard de anuncios de vendas de carros')

st.subheader('Visualizações Interativas')
build_histogram = st.checkbox('Mostrar Histograma de Hodômetro')

if build_histogram: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Mostrar Grafico de dispersao (Preco vs. Hodometro)')

if build_scatter:
    st.write('Grafico de dispersao: Relacao entre preco e hodometro')
    
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    st.plotly_chart(fig_scatter, use_container_width=True)