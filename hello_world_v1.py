import streamlit as st

st.write("Hello World, this is my new Streamlit application. It works again. ")

with st.form(key='my_form'):
 	text_input = st.text_input(label='Enter some text')
 	submit_button = st.form_submit_button(label='Submit')
