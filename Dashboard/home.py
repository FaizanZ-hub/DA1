import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd 
import plotly.graph_objects as go

st.markdown('<h1 style="color: brown; text-align : center;background-color:white; border:2px solid red"> Titanic Data Analysis </h1>', unsafe_allow_html=True) 
st.markdown('<p style="color: blue; text-align : center; margin-top: 20px"> The RMS Titanic was a British passenger liner that famously sank on its maiden voyage in April 1912 after hitting an iceberg. It was one of the largest and most luxurious ships of its time, designed to offer unparalleled comfort and amenities. The Titanic was equipped with advanced safety features, but it lacked enough lifeboats for all passengers. The disaster resulted in the deaths of over 1,500 people, making it one of the deadliest maritime tragedies in history. The story of the Titanic has inspired numerous books, films, and documentaries, highlighting themes of hubris, tragedy, and the human experience. </p>', unsafe_allow_html=True) 

st.image('assets\overview-Titanic.webp',use_column_width=True)