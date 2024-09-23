import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data(1990)')
df = pd.read_csv('housing.csv')

price_filter = st.slider('Minimal Median House Price :', 0, 500001,200000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a radio button
income_level = st.sidebar.radio(
    'Filter by Income Level',
    ('Low', 'Medium', 'High')
)

# filter DataFrame by income level
if income_level == 'Low':
    df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium':
    df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
elif income_level == 'High' :
    df = df[df['median_income'] > 4.5]

# filter by median price
df = df[df.median_house_value >= price_filter]

# filter by location type
df = df[df.ocean_proximity.isin(location_filter)]


# show on map
st.map(df)

# show the plot
fig, ax = plt.subplots(figsize=(20, 20))
df['median_house_value'].hist(bins=30, ax=ax)
st.pyplot(fig)
