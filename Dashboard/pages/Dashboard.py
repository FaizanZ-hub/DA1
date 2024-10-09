import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd 
import plotly.graph_objects as go

#load the titanic dataset
df = sns.load_dataset('titanic')

#set the title of the page
st.title('Titanic Data Analysis')


st.sidebar.header("Filter Options")

#gender filter
gender = st.sidebar.multiselect("gender",
                                options=df['sex'].unique(),
                                default=df['sex'].unique())


#class filter
pclass = st.sidebar.multiselect('Class',
                                options=sorted(df['pclass'].unique()),
                                default=sorted(df['pclass'].unique()))

#age filter
min_age,max_age = st.sidebar.slider('Age',
                                    min_value=int(df['age'].min()),
                                    max_value=int(df['age'].max()),
                                    value = (int(df['age'].min()),int(df['age'].max())))

#filter the dataset based on the user selection
filtered_data = df[
    (df['sex'].isin(gender)) &
    (df['pclass'].isin(pclass)) &
    (df['age'] >= min_age) &
    (df['age'] <=max_age) 
]

st.dataframe(filtered_data)