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
    resp = st.checkbox('No estoy de acuerdo')
    if resp:
        st.write('Incorrecto')
        
    with col2:
        st.subheader("Esta es la segunda columna")
        modo = st.radio("Que Modalidad es la principal en tu interfaz", ('Visual','auditiva','tactil'))
    if modo=='Visual':
        st.write("la vista es fundamental para tu interfaz") 
    if modo == "auditiva":
        st.write("La audicion es fundamental para tu interfaz")
    if modo == "tactil":
        st.write("El tacto es fundamental para tu interfaz")
        
    st.subheader("Uso de Botones")
        if st.button('Presiona el botón'):
            st.write('Gracias por presionar')
        else:
            st.write('No has presionado aún')
