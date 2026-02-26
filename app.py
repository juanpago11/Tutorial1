import streamlit as st
from PIL import Image

st.title("Es encontrado el especimen Rudyus Pititus blogus")
st.header("Comienza el nuevo orden mundial")
st.write("El bhuo puede gobernar el mundo")
image = Image.open('buhoo.jpg')
st.image(image, caption='EL BUHO')

texto = st.text_input('escribe algo', 'este es mi texto')
st.write('EL texto es la prote', texto)

st.subheader("Ahora usemos 2 columnas")

coll, col2 = st.columns(2)

with coll:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimpodales mejoran la UX")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
      st.write('Correcto')
               
    
