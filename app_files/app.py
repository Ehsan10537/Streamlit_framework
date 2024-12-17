
# NOTE: To run a streamlit app (in this case app.py), you have to run the following command in terminal: streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Streamlite folks")

## Display a simple text
st.write("This is a simple text")

## Create a simple DataFrame
df = pd.DataFrame({
    "first column":[1, 2, 3, 4],
    "second column":[10, 20, 30, 40]
})

## Display the DataFrame
st.write("Here is the DataFrame")
st.write(df)

## Create a line chart
chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a', 'b', 'c'])
st.write("The chart data:")
st.write(chart_data)
st.write("The line chart")
st.line_chart(chart_data)
print(chart_data)
