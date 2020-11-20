import streamlit as st

import numpy as np
import pandas as pd
import joblib
import datetime


st.set_page_config(
            page_title="Super batch recap", # => Quick reference - Streamlit
            page_icon="🚀",
            layout="centered")

'# Welcome to super batch web page'

our_html = f'''
    <p>Testche</p>
    <img src="https://picsum.photos/200/300">
'''

st.write(our_html, unsafe_allow_html=True)

'-----'

"# Let's try to incorporate our pipeline into Streamlit"

# precisamos carregar o joblib
pipeline = joblib.load('model.joblib')


# precisamos de um input (dados que vamos utilizar para fazer a previsão)
# - latitude e longitude da partida
pic_lat = st.number_input('What is the pickup latitude?')
pic_lng = st.number_input('What is the pickup longitude?')

# - latitude e longitude da chegada
drop_lat = st.number_input('What is the dropoff latitude?')
drop_lng = st.number_input('What is the dropoff longitude?')

# - n de passageiros
n_pass = st.number_input('What is the number of passengers?', min_value=1, max_value=8, step=1)

# - data da partida
date = st.date_input("What is the pickup date?")
date = str(date)

time = st.time_input("What is the pickup time?")
time = str(time)

dt = f"{date} {time} UTC"
dt

# transforma enderecos obtidos em lat e lng (exercicio completar)


# gerar um df com os inputs
# X = pd.DataFrame({
#     'key': ['2020-11-20 17:47:00 UTC'],
#     'pickup_datetime': ['2020-11-20 17:47:00 UTC'],
#     'pickup_longitude': [-74.1093172],
#     'pickup_latitude': [40.7592369],
#     'dropoff_longitude': [-74.2251911],
#     'dropoff_latitude': [40.6454265],
#     'passenger_count': [4]
# })


X = pd.DataFrame({
    'key': [dt],
    'pickup_datetime': [dt],
    'pickup_longitude': [pic_lng],
    'pickup_latitude': [pic_lat],
    'dropoff_longitude': [drop_lng],
    'dropoff_latitude': [drop_lat],
    'passenger_count': [n_pass]
})

X

# passar o input para o joblib para fazer a previsão
results = pipeline.predict(X)

# mostrar os resultados na tela
result = round(results[0], 2)
f'The prediction for the given inputs is {result}'



