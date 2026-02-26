import streamlit as st
from PIL import image

st.title("Hola de nuevo mundo jaja")
st.header("En este espacio comienza el nuevo orden mundial")
st.write("Facilmente el bhuo puede gobernar el mundo")
image = image.open('buhoo.jpg')
st.image(image, caption='EL BUHO')

