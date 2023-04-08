import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("Hello world!")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)

  # Add some matplotlib code !
  fig, ax = plt.subplots()
  df.hist(
    bins=8,
    column="openp",
    grid=False,
    figsize=(8, 8),
    color="#86bf91",
    zorder=2,
    rwidth=0.9,
    ax=ax,
  )
  st.write(fig)


   
year = [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
unemployment_rate = [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
  
plt.plot(year, unemployment_rate, color='red', marker='o')
plt.title('unemployment rate vs year', fontsize=14)
plt.xlabel('year', fontsize=14)
plt.ylabel('unemployment rate', fontsize=14)
plt.grid(True)
plt.show()