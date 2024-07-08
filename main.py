# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import streamlit as st
import pandas as pd
st.markdown("ventas en munro")

chart_data = pd.read_csv('ventas.csv')
st.line_chart(chart_data)




