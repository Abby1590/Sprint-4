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

st.text("These insights imply that buyers looking for used vehicles are more likely to encounter gasoline-powered cars, while sellers of electric and hybrid vehicles may face a narrower pool of potential buyers. Further analysis could explore whether these differences impact pricing, vehicle condition, or the time vehicles spend on the market. Understanding these factors could help inform both sellers and buyers on market trends, pricing strategies, and demand dynamics for various fuel types.")

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

st.text("The scatter plot comparing vehicle model years to the date they were posted reveals several key insights regarding the used car market over time. The majority of the vehicles listed are relatively recent models, with a significant concentration of cars from the year 2000 onward, indicating a stronger market presence for newer models. Older vehicles, particularly those dating back before 1980, appear much less frequently, suggesting limited availability and potentially lower demand for older models.")

# Extra Graphs
# Create a histogram for 'days_listed'
fig = px.histogram(
    df, 
    x='days_listed', 
    nbins=30,  
    title='Distribution of Days Listed for Vehicles',
    labels={'days_listed': 'Days Listed'},
    color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA'], 
    width=900, 
    height=500
)

# Use a color gradient based on the count of listings in each bin
fig.update_traces(marker=dict(colorbar=dict(title='Count'), colorscale='Viridis'))

# Show the plot
st.plotly_chart(fig)

st.text("The histogram depicting the distribution of days vehicles are listed reveals insightful trends about the duration of listings. The majority of vehicles are sold or taken down relatively quickly, with the highest frequency occurring within the first 20 days. The data shows a sharp decline in the number of listings beyond 50 days, indicating that vehicles tend to sell faster in the early days after being posted.")


# Create a pie chart to show the distribution of vehicle conditions with distinct colors
fig = px.pie(
    df, 
    names='condition', 
    title='Proportion of Vehicle Conditions',
    color_discrete_sequence=px.colors.qualitative.Plotly,
    hole=0.4,
    labels={'condition': 'Condition'}
)

# Update trace to include percentage and label on each slice
fig.update_traces(textinfo='percent+label')

# Show the pie chart
st.plotly_chart(fig)

st.text("The distribution of vehicle conditions provides insights into the quality of the listings. The majority of the vehicles are categorized as being in excellent condition, making up nearly 48.1% of all listings. This suggests that sellers are keen to showcase their cars as being in top shape to attract buyers. Following this, 39.1% of the listings are in good condition, indicating that a significant portion of the cars is still of decent quality but not necessarily in pristine condition.")


# Listings over time
df['date_posted'] = pd.to_datetime(df['date_posted'])
fig = px.line(
    df.groupby('date_posted').size().reset_index(name='count'), 
    x='date_posted', 
    y='count', 
    title='Number of Listings Over Time',
    labels={'date_posted': 'Date Posted', 'count': 'Number of Listings'}
)
st.plotly_chart(fig)

st.text("The line chart depicting the number of listings over time reveals significant fluctuations throughout the analyzed period from May 2018 to May 2019. The general trend shows consistent spikes and dips in the number of listings, indicating that the vehicle listing activity varies day-to-day.The data suggests that there are multiple peaks where the number of listings reaches around 180 vehicles, followed by sharp declines to around 120 listings. This pattern could be indicative of seasonal trends or specific events that influence when people choose to list their vehicles. For instance, there could be increased listings around certain times of the year due to holidays, tax refunds, or other market factors driving vehicle sales.")


#Pricing compared to condition
fig = px.box(
    df, 
    x='condition', 
    y='price', 
    color='condition',
    title='Price Distribution by Vehicle Condition',
    labels={'condition': 'Vehicle Condition', 'price': 'Price'},
    color_discrete_sequence=px.colors.qualitative.Bold, 
    width=900, 
    height=500
)
st.plotly_chart(fig)

st.text(" The analysis indicates that vehicle condition significantly impacts pricing, with 'new' and 'excellent' condition listings commanding the highest prices, while 'fair' and 'salvage' vehicles are priced much lower. The presence of outliers in almost every category suggests variability in pricing strategies, potentially influenced by model, brand, or other factors like vehicle modifications.")

st.header("Final Conclusion:")

st.text("The exploratory data analysis of the vehicle dataset revealed several significant insights into the market trends and listings. The majority of vehicles listed were in 'good' or 'excellent' condition, which aligns with sellers aiming to present well-maintained cars. The scatter plots and box plots demonstrated that newer models generally commanded higher prices, while older models showed wider price variability, especially in the 'good' condition category. Listings were fairly consistent throughout the year, with slight increases in June and December, possibly due to seasonal demand shifts. Interestingly, most vehicles listed used gasoline, indicating its dominance in the market, while electric and hybrid vehicles made up a very small portion of the listings. Additionally, the distribution of 'days listed' showed that a significant number of cars were sold quickly, though some lingered on the market, especially those in poorer conditions or with higher mileage. Finally, a comparison between listings from 2018 and 2019 revealed a drop in postings in 2019, suggesting a potential shift in market dynamics or a reduction in overall supply. These insights can be valuable for both sellers and buyers in understanding market behavior, optimizing listing strategies, and making informed decisions.")