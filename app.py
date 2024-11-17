import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# 1. Add a header
st.header("Exploratory Data Analysis of Vehicles Dataset")

# 2. Add a Plotly Express histogram
fig = px.histogram(
    df,
    x='fuel',
    color='fuel',
    title='Distribution of Fuel Types',
    labels={'fuel': 'Fuel Type'},
    color_discrete_sequence=px.colors.qualitative.Set3,
    width=800,
    height=500
)
st.plotly_chart(fig)

# 3. Add a Plotly Express scatter plot
st.header("Model Year vs. Date Posted Analysis")
if st.checkbox("Show only cars in 'excellent' condition"):
    filtered_df = df[df['condition'] == 'excellent']
else:
    filtered_df = df

fig = px.scatter(
    filtered_df,
    x='date_posted',
    y='model_year',
    color='condition',
    opacity=0.7,
    title='Model Year vs Date Posted by Condition',
    labels={'model_year': 'Model Year', 'date_posted': 'Date Posted'},
    width=900,
    height=500
)
st.plotly_chart(fig)
