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

chart_data = pd.DataFrame(
    openi,
    columns=['issues'])

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")

st.write("Start time:", start_time)

st.line_chart(chart_data)

st.bar_chart({"data": openi})
