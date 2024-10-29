import streamlit as st
import pandas as pd
import numpy as np


st.write("Bonjour ceci est un test")
file = st.file_uploader("Pick a file")
color = st.color_picker
date = st.date_input("Pick a date")

chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
)

st.line_chart(chart_data, x="col1", y="col2", color="col3")


x = st.slider("Select a value")
st.write(x, "squared is", x * x)
