import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data(1990)')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
population_filter = st.slider('Minimal Median House Price :', 0, 500001,200000)  # min, max, default

# create a multi select
capital_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a radio button
income_level = st.radio(
    'Filter by Income Level',
    ('Low', 'Medium', 'High')
)

# filter DataFrame by income level
if income_level == 'Low':
    df_filtered = df[df['income'] <= 2.5]
elif income_level == 'Medium':
    df_filtered = df[(df['income'] > 2.5) & (df['income'] < 4.5)]
elif income_level == 'High' :
    df_filtered = df[df['income'] > 4.5]

# show DataFrame
st.write(df_filtered)


# show on map
st.map(df)

# show the plot
fig, ax = plt.subplots(figsize=(20, 5))
df['median_house_value'].hist(bins=30, ax=ax)
st.pyplot(fig)