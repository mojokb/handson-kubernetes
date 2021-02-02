import streamlit as st
import socket

st.title('hello world - ' + str(socket.gethostname()))
x = st.slider('x')  
st.write(x, 'squared is', x * x)

