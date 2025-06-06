import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load Data ---
df = pd.read_csv("copenhagen_traffic_raw.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        /* Set background of app */
        .stApp {
            background-color: #f5f7fa;
        }

        /* Custom metric box */
        .metric-box {
            background-color: #e3f2fd;
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
            margin: 0.5rem 0;
        }

        /* Header text color */
        h1, h2, h3 {
            color: #1f4e79 !important;
        }

        /* Sidebar background */
        [data-testid="stSidebar"] {
            background-color: #e8f0fe;
        }

        /* Footer styling */
        footer {
            text-align: center;
            font-size: 0.8rem;
            color: #777;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.image("copenhagen.jpg")
st.sidebar.title("🔧 Dashboard Filters")

area = st.sidebar.selectbox("Select Area", df['area'].unique())
weather = st.sidebar.selectbox("Select Weather", df['weather'].unique())
view = st.sidebar.radio("View", ["Overview", "Raw Data"])

# --- Filter Data ---
filtered = df[(df['area'] == area) & (df['weather'] == weather)]

# --- Main Content ---
st.title("🚦Copenhagen Traffic Dashboard")
st.markdown(f"<h3>📍 Area: <em>{area}</em> | 🌦 Weather: <em>{weather}</em></h3>", unsafe_allow_html=True)

if view == "Overview":
    st.subheader("📊 Traffic Stats")
    col1, col2, col3 = st.columns(3)
    col1.markdown(f"""
        <div class='metric-box'>
            <h4>🚗 Avg Vehicles</h4>
            <p><b>{filtered['vehicle_count'].mean():.0f}</b></p>
        </div>
    """, unsafe_allow_html=True)
    col2.markdown(f"""
        <div class='metric-box'>
            <h4>🚲 Avg Bikes</h4>
            <p><b>{filtered['bike_count'].mean():.0f}</b></p>
        </div>
    """, unsafe_allow_html=True)
    col3.markdown(f"""
        <div class='metric-box'>
            <h4>🚌 Avg Buses</h4>
            <p><b>{filtered['bus_count'].mean():.0f}</b></p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("📈 Hourly Traffic Trends")
    st.line_chart(filtered.set_index('timestamp')[['vehicle_count', 'bike_count', 'bus_count']])

    st.subheader("🌦 Weather Distribution (All Data)")
    weather_counts = df['weather'].value_counts().reset_index()
    weather_counts.columns = ['weather', 'count']
    st.bar_chart(weather_counts.set_index('weather'))

else:
    st.subheader("📋 Raw Data Preview")
    st.dataframe(filtered, use_container_width=True)
    
    # Show raw data
with st.expander("📄 Raw Data"):
    st.dataframe(df)

# Summary Statistics
st.subheader("📊 Descriptive Statistics (All Data)")
st.dataframe(df.describe())

# Quick Metrics
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)
col1.metric("Avg Vehicle Count", f"{df['vehicle_count'].mean():.0f}")
col2.metric("Avg Bike Count", f"{df['bike_count'].mean():.0f}")
col3.metric("Avg Bus Count", f"{df['bus_count'].mean():.0f}")


# Mean count by Area
st.subheader("🏙️ Average Traffic Count by Area (All Data)")
area_means = df.groupby("area")[["vehicle_count", "bike_count", "bus_count"]].mean()
st.bar_chart(area_means)

# Boxplots
st.subheader("📦 Distribution by Category (All Data)")
fig, ax = plt.subplots(1, 3, figsize=(15, 4))
sns.boxplot(data=df, y="vehicle_count", ax=ax[0])
sns.boxplot(data=df, y="bike_count", ax=ax[1])
sns.boxplot(data=df, y="bus_count", ax=ax[2])
ax[0].set_title("Vehicle Count"); ax[1].set_title("Bike Count"); ax[2].set_title("Bus Count")
st.pyplot(fig)

# Weather pie chart
st.subheader("🌦️ Weather Distribution (All Data)")
weather_counts = df['weather'].value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
st.pyplot(fig2)

# --- Footer ---
st.markdown("---")
st.markdown("""
<footer>
Made with ❤️ by Eng. <a href="https://github.com/xuux12/" target="_blank">Ali Mohammed</a> in Esbjerg using Streamlit | Data: Copenhagen Traffic (7 days hourly)
</footer>
""", unsafe_allow_html=True)









