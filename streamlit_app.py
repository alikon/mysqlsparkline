import pandas as pd
import streamlit as st
from datetime import datetime
import altair as alt

def showChart(df, age):
  # sorting data frame by a column
  df.sort_values("id", axis=0, ascending=True,
                 inplace=True, na_position='first')
  newdf = df[(df.id > age)]

  chart_data = pd.DataFrame(
    newdf['openi'].tolist(),
    columns=['issues'])

  source = pd.DataFrame({
    'day': newdf['execution'].tolist(),
    'issues': newdf['openi'].tolist()
  })

  chart1 = alt.Chart(source).mark_line().encode(
      x='day:T',
      y='issues:Q'
  )

  chart = alt.Chart(source).mark_area(
    line={'color':'red'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='white', offset=0),
               alt.GradientStop(color='red', offset=1)],
        x1=1,
        x2=1,
        y1=1,
        y2=0
    )
  ).encode(
      alt.X('day:T'),
      alt.Y('issues:Q',scale=alt.Scale(type='log', domain=[0.001, 1000]),)
  )
  st.altair_chart(chart)

st.title("Datasort")



uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  age = st.slider('Start at ?', 0, 300, 0)
  st.write("From ", age, ' old')
  showChart(df, age)
  # st.write(df)
  # st.line_chart(chart_data)
  # st.bar_chart({"data": newdf['openi'].tolist()})
