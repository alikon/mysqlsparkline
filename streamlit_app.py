import pandas as pd
import streamlit as st
from datetime import datetime
import altair as alt

st.title("Datasort")

age = st.slider('Start at ?', 0, 300, 25)
st.write("From ", age, ' old')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
 # st.write(df)

data =df['execution'].tolist()
openi=df['openi'].tolist()
id=df['id'].tolist()

# sorting data frame by a column
df.sort_values("id", axis=0, ascending=True,
                 inplace=True, na_position='first')

newdf = df[(df.id > age)]
  
# display
df.head(10)

chart_data = pd.DataFrame(
    newdf['openi'].tolist(),
    columns=['issues'])

source = pd.DataFrame({
  'day': newdf['execution'].tolist(),
  'issues': newdf['openi'].tolist()
})

chart = alt.Chart(source).mark_line().encode(
    x='issues',
    y='day'
)
st.altair_chart(chart)
# st.line_chart(chart_data)

# st.bar_chart({"data": newdf['openi'].tolist()})
