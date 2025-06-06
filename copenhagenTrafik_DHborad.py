
import streamlit as st

# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#loading data
df = pd.read_csv('copenhagen_traffic_raw.csv')

#sidebar
st.sidebar.header('C Copenhagen Traffic Dashboard')
st.sidebar.image('copenhagen.jpg')
st.sidebar.write('Are You Sure You,re In Copenhagen')
st.markdown("# 🚦You Are in Copenhagen Traffic")


st.sidebar.write('By Eng [Ali Mohammed](https://github.com/xuux12/)')

#Body 

#Rows a 
a1, a2 = st.columns(2)

a1.metric('Total Cars', round(df['vehicle_count'].max(), 0))
a2.metric('Cars Avg Speed', f"{round(df['avg_speed_kmph'].mean(), 1)} km/h")

 # Code before...

fig, ax = plt.subplots()
sns.barplot(data=df, x='intersection', y='avg_speed_kmph', hue='congestion_level', ax=ax)
ax.set_ylabel("Average Speed (km/h)")
ax.set_title("Average Speed by Intersection")

st.pyplot(fig)

fig, ax = plt.subplots()
df['congestion_level'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax, startangle=90)
ax.set_ylabel("")
ax.set_title("Traffic Congestion Distribution")

st.pyplot(fig)




import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and parse timestamp
df = pd.read_csv("copenhagen_traffic_raw.csv", parse_dates=["timestamp"])

# Create day_of_week column
df["day_of_week"] = df["timestamp"].dt.day_name()

# Define day order for proper sorting
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Get only the days that are actually in the dataset
available_days = [day for day in day_order if day in df["day_of_week"].unique()]

# Streamlit multiselect filter
selected_days = st.multiselect("Filter by Day of the Week", available_days, default=available_days)

# Filter the DataFrame
filtered_df = df[df["day_of_week"].isin(selected_days)]

# Show filtered data
st.write("### Filtered Data", filtered_df.head())

# Plot: Average Speed per Day of Week
if not filtered_df.empty:
    fig, ax = plt.subplots()
    sns.boxplot(data=filtered_df, x="day_of_week", y="avg_speed_kmph", order=day_order)
    ax.set_title("Average Speed by Day of Week")
    ax.set_xlabel("Day")
    ax.set_ylabel("Speed (km/h)")
    st.pyplot(fig)
else:
    st.warning("No data available for the selected days.")
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and parse timestamp
df = pd.read_csv("copenhagen_traffic_raw.csv", parse_dates=["timestamp"])

# Create day_of_week column
df["day_of_week"] = df["timestamp"].dt.day_name()

# Define day order for proper sorting
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Get only the days that are actually in the dataset
available_days = [day for day in day_order if day in df["day_of_week"].unique()]

# Streamlit multiselect filter
selected_days = st.multiselect("Filter by Day of the Week", available_days, default=available_days)

# Filter the DataFrame
filtered_df = df[df["day_of_week"].isin(selected_days)]

# Show filtered data
st.write("### Filtered Data", filtered_df.head())

# Plot: Average Speed per Day of Week
if not filtered_df.empty:
    fig, ax = plt.subplots()
    sns.boxplot(data=filtered_df, x="day_of_week", y="avg_speed_kmph", order=day_order)
    ax.set_title("Average Speed by Day of Week")
    ax.set_xlabel("Day")
    ax.set_ylabel("Speed (km/h)")
    st.pyplot(fig)
else:
    st.warning("No data available for the selected days.")








