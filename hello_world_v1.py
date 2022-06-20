import streamlit as st
import pandas as pd

# Creating Data Frame 1
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df1 = pd.DataFrame(data)



st.write("Hello World, this is my new Streamlit application. It works again. ")

element = st.dataframe(df1)


with st.form(key='my_form'):
  calories = int(st.number_input(label='Enter calories'))
  duration = int(st.number_input(label='Enter duration'))
  
  data = {
    "calories": [calories],
    "duration": [duration]
  }
  
  df2 = pd.DataFrame(data)
  element.add_rows(df2)
  
  submit_button = st.form_submit_button(label='Submit')
