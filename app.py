import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 


    # Botón para construir gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: precio vs. kilometraje')
    
    # Crear el gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price", 
                     title="Precio vs. Kilometraje",
                     labels={"odometer": "Kilometraje", "price": "Precio"},
                     opacity=0.5)  # Puedes ajustar la opacidad si hay muchos puntos
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)