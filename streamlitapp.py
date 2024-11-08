# Import necessary libraries
import streamlit as st
import seaborn as sns 
import plotly.express as px
import pandas as pd

# --- Title and Introduction ---
st.title("Plotly and Streamlit Interactive Visualizations")

# Author information
st.markdown("<h5 style='color: teal;'>Created by: Anant Nagaraj Hegde </h6>", unsafe_allow_html=True)



tips = sns.load_dataset('tips')  # Loading the dataset
print(tips.head())  # This will show the first 5 rows of the tips dataset


fig1 = px.bar(tips, x="day", y="tip")
fig1.show()
st.plotly_chart(fig1)


# --- Task 2: Bar Chart ---
st.subheader("Bar Chart")
#Bar Chart: Average Tip by Day (With Color)
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white',  # Clean white background
)
fig2.show()
st.plotly_chart(fig2)


#4. Scatter Plot: Total Bill vs. Tip (Color-coded by Gender)
st.subheader("Scatter Plot")
fig4 = px.scatter(
tips, x='total_bill', y='tip', color='sex',
title='Total Bill vs Tip (Colored by Gender)',
labels={'total_bill': 'Total Bill ($)', 'tip': 'Tip ($)'},
template='plotly_dark', # Using a cool dark theme
size='size' # The size of points based on the size of the group
)
fig4.show()
st.plotly_chart(fig4)


#5. Box Plot: Distribution of Total Bill by Day (With Color by Time)
st.subheader("Box Plot")
fig5 = px.box(
tips, x='day', y='total_bill', color='time',
title='Total Bill Distribution by Day and Time',
labels={'total_bill': 'Total Bill ($)', 'day': 'Day'},
template='ggplot2', # Classic theme for a beautiful look
)
fig5.show()
st.plotly_chart(fig5)


#6. Histogram: Tip Distribution (With Color)
st.subheader("Histogram")
fig6 = px.histogram(
tips, x='tip', color='sex',
title='Distribution of Tips (Colored by Gender)',
labels={'tip': 'Tip ($)', 'sex': 'Gender'},
template='plotly_white', # Clean and bright look
)
fig6.show()
st.plotly_chart(fig6)

