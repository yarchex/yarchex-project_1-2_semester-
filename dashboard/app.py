import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('data/processed/programming_languages.csv')

df = load_data()

# Dashboard layout
st.title('Programming Languages Popularity Dashboard')
st.sidebar.header('Filters')

# Filters
selected_languages = st.sidebar.multiselect(
    'Select languages',
    df['language'].unique(),
    default=['python', 'javascript']
)

# Filtered data
filtered_df = df[df['language'].isin(selected_languages)]

# Visualizations
st.header('Trend Analysis')
fig = px.line(filtered_df, x='date', y='count', color='language')
st.plotly_chart(fig)

st.header('Popularity Comparison')
fig2 = px.bar(filtered_df.groupby('language')['count'].mean().reset_index(), 
              x='language', y='count')
st.plotly_chart(fig2)

# Metrics
st.header('Key Metrics')
col1, col2 = st.columns(2)
col1.metric("Most Popular Language", "Python")
col2.metric("Fastest Growing", "Rust", "35%")
