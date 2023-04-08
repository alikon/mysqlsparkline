import pandas as pd
import streamlit as st
from datetime import datetime
import altair as alt

def showIssues(df, age):
  # sorting data frame by a column
  df.sort_values("id", axis=0, ascending=True,
                 inplace=True, na_position='first')
  newdf = df[(df.id > age)]

  source = pd.DataFrame({
    'day': newdf['execution'].tolist(),
    'issues': newdf['openi'].tolist()
  })

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
      alt.Y('issues:Q',scale=alt.Scale(type='log', domain=[600, 1000]),)
  )
  st.altair_chart(chart)

def showPulls(df, age):
  # sorting data frame by a column
  df.sort_values("id", axis=0, ascending=True,
                 inplace=True, na_position='first')
  newdf = df[(df.id > age)]

  source = pd.DataFrame({
    'day': newdf['execution'].tolist(),
    'pulls': newdf['openp'].tolist()
  })

  chart = alt.Chart(source).mark_area(
    line={'color':'green'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='white', offset=0),
               alt.GradientStop(color='green', offset=1)],
        x1=1,
        x2=1,
        y1=1,
        y2=0
    )
  ).encode(
      alt.X('day:T'),
      alt.Y('pulls:Q',scale=alt.Scale(type='log', domain=[100, 500]),)
  )
  st.altair_chart(chart)

st.title("Datasort")



#uploaded_file = st.file_uploader("Choose a file")
df = pd.read_csv("./data/dataset.csv")
if df is not None:
  # df = pd.read_csv(uploaded_file)
  df['execution'] = pd.to_datetime(df['execution'])
  slider = st.slider('Select date', min_value=df['execution'].min(), value=df['execution'].max() ,max_value=df['execution'].max())
  st.sidebar.write(slider)
  start_dt = st.sidebar.date_input('Start date', value=df['execution'].min())
  end_dt = st.sidebar.date_input('End date', value=df['execution'].max())
  age = st.slider('Start at ?', 0, 300, 0)
  st.write("From ", age, ' old')
  tab1, tab2 = st.tabs(["📈 Issues", "🗃 Pull Requests"])
  with tab1:
    showIssues(df, age)
  with tab2:
    showPulls(df, age)
  # st.write(df)
  # st.line_chart(chart_data)
  # st.bar_chart({"data": newdf['openi'].tolist()})
