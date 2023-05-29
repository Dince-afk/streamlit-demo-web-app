import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("Practice App")

df = pd.read_csv("data.csv", index_col="Name")
# st.write(df)
# st.table(df.head(10))
# df_widget = st.dataframe(df)
# df_widget.add_rows(df.head())

# use dataframe methods in order to change it 
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

# create charts
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.line_chart(df.groupby("Generation")[["HP", "Attack", "Defense"]].mean())

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
st.write(plt.scatter(df["HP"], df["Attack"]))
st.write(df[["HP", "Attack"]].plot.scatter("HP", "Attack"))

st.slider("Label")