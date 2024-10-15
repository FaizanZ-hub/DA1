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

#Create a pie chart for gender distribution
st.subheader('Gender Distribution')
gender_count = filtered_data['sex'].value_counts()
fig = px.pie(names=gender_count.index, values=gender_count.values,
             title='Gender Distribution')
st.plotly_chart(fig)

#Create a histogram for age distribution
st.subheader("Age Distribution")
fig=px.histogram(filtered_data,x='age',nbins=20,title='Age Distribution',
                 labels={'age':'Age','count':'count'})
st.plotly_chart(fig)

#box blot of age distribution by passenger class
#st.subheader("Age distribution by passenger class")
#fig = px.box(filtered_data,x='pclass', y='age', title='Age Distribution by Passenger Class',
#             labels={'pclass': 'Passenger Class', 'age': 'Age'})

#Barchart for survival count
#st.subheader("Survival Count")
#fig = px.bar(filtered_data,x='Survived', y='Count', title='Titanic Survival Counts',
#             labels={'Survived': 'Survival Status', 'Count': 'Number of Passengers'})



#violin plot of age distribution by survival status 
#Scatter plot of age vs fare
#box plot of age distribution by passenger class
#bar chart of survival counts