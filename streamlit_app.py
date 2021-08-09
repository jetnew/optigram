import streamlit as st
import matplotlib.pyplot as plt

from texts import *

st.title(txt_title)

st.header(header1)
st.markdown(section1)

st.header(header2)
st.markdown(section2)

st.header(header3)
st.markdown(section3)

st.header(header4)

st.markdown(4)

st.header(header5)
st.text("Average Household Size")
household_size = [3.3, 3.3, 4.3, 2.9]
st.bar_chart(household_size)

st.markdown(section5)