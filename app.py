import streamlit as st
import pandas as pd
import plotly.express as px
#python -m streamlit run app.py

st.set_page_config(layout="wide")

df = pd.read_csv('vgsales.csv')

#SIDEBAR

st.sidebar.title('Game Time')
st.sidebar.image('gaming_logo.png')

publishers = df['Publisher'].unique().tolist()

publishers_escolhidos = st.sidebar.multiselect('Publisher', publishers, publishers)

df = df[df['Publisher'].apply(lambda x: x in publishers_escolhidos)]

#BODY

with st.container():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st.container(border=True, height='stretch'):
            st.metric('Total em Vendas Globais', f'${df['Global_Sales'].sum():.0f}')

    with col2:
        with st.container(border=True, height='stretch'):
            st.metric('Total de Paises', len(paises_escolhidos))

    with col3:
        with st.container(border=True, height='stretch'):
            st.metric('Total de Empresas', df['Company'].nunique())

    with col4:
        with st.container(border=True, height='stretch'):
            st.metric('Provedores de Crédito', df['CC Provider'].nunique())