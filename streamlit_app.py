import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from datetime import datetime

st.title("Hello world!")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)

data =df['execution'].tolist()
openi=df['openi'].tolist()
id=df['id'].tolist()

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 1, 30),
    format="DD/MM/YY - hh:mm")

st.write("Start time:", start_time)
age = st.slider('Start at ?', 0, 300, 25)
st.write("From ", age, ' old')


chart_data = pd.DataFrame(
    openi,
    columns=['issues'])

st.line_chart(chart_data)

st.bar_chart({"data": openi})
