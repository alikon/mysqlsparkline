import pandas as pd
import streamlit as st
from datetime import datetime
import altair as alt

def showIssues(df):
  source = pd.DataFrame({
    'day': df['execution'].tolist(),
    'issues': df['openi'].tolist()
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

def showPulls(df):
  source = pd.DataFrame({
    'day': df['execution'].tolist(),
    'pulls': df['openp'].tolist()
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
      alt.Y('pulls:Q',scale=alt.Scale(type='log', domain=[100, 350]),)
  )
  st.altair_chart(chart)
############################## start ##################################
st.title("Joomla Github statistics")
#uploaded_file = st.file_uploader("Choose a file")
df = pd.read_csv("./data/dataset.csv")
if df is not None:
  # df = pd.read_csv(uploaded_file)
  df['execution'] = pd.to_datetime(df['execution'])
  slider = st.sidebar.slider('Select date', min_value=datetime.date(df['execution'].min()), value=datetime.date(df['execution'].min()) ,max_value=datetime.date(df['execution'].max()))
  ts = pd.DatetimeIndex([slider])[0]
  # sorting data frame by a column
  df.sort_values("id", axis=0, ascending=True,
                 inplace=True, na_position='first')
  # filter values
  newdf = df[(df.execution > ts)]
  # show chart
  tab1, tab2 = st.tabs(["📈 Issues", "🗃 Pull Requests"])
  with tab1:
    showIssues(newdf)
  with tab2:
    showPulls(newdf)
  with st.expander("See data"):
    st.write(df)
