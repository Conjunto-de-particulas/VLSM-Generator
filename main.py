import streamlit as st
import pandas as pd
import metodos

st.title('Subnetting VLSM')


dip = st.text_input('Direccion IP', '')
mr = st.text_input('Mascara de red', '')
numSubRedes = st.text_input('Numero de subredes', '')

try:
    numSubRedes = int(numSubRedes)
except Exception as e:
    numSubRedes = 0

subRedes = metodos.generarSubredes(numSubRedes)
dfSubRedes = pd.DataFrame(subRedes)

edited_df = st.data_editor(dfSubRedes, num_rows="dynamic")




