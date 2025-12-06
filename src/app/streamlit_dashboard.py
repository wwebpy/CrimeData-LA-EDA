import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dark mode styling for plots
sns.set_theme(style="darkgrid")
plt.style.use("dark_background")

st.set_page_config(page_title="LA Crime Dashboard by Burak Tamer", layout="wide")

@st.cache_data
def load_data():
    data = pd.read_csv("../../data/processed/Crime_Data_cleaned.csv")
    data['DATE_OCC'] = pd.to_datetime(data['DATE_OCC'])
    return data

data = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
years = sorted(data['OCC_YEAR'].unique())
year_select = st.sidebar.multiselect("Select Year", years, default=years)
areas = sorted(data['AREA_NAME'].unique())
area_select = st.sidebar.multiselect("Select Area", areas, default=areas)
df = data[(data['OCC_YEAR'].isin(year_select)) & (data['AREA_NAME'].isin(area_select))]

# KPI Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", f"{df.shape[0]:,}")
col2.metric("Unique Crime Types", df['CRM_CD_DESC'].nunique())
col3.metric("Number of Areas", df['AREA_NAME'].nunique())

st.title("🚔 Los Angeles Crime Dashboard")
st.markdown("Interactive analysis of LAPD crime data (2020–Present)")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Crimes Overview",
    "Time Analysis",
    "Location",
    "Victim Profile"
])

# TAB 1: Top 20 Crimes and Weapons
with tab1:

    st.header("Top 20 Most Frequent Crime Types")

    top_crimes = df['CRM_CD_DESC'].value_counts().head(20)

    fig, ax = plt.subplots(figsize=(10,8))
    sns.barplot(x=top_crimes.values, y=top_crimes.index, ax=ax)
    ax.set_title("Top 20 Most Frequent Crime Types in LA")
    ax.set_xlabel("Number of Incidents")
    ax.set_ylabel("Crime Type")
    st.pyplot(fig)

    st.subheader("Top 15 Crimes involving Weapons")
    weapon_cases = df[df['WEAPON_USED_CD'] > 0]
    weapon_by_crime = weapon_cases['CRM_CD_DESC'].value_counts().head(15)
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(x=weapon_by_crime.values, y=weapon_by_crime.index, ax=ax)
    ax.set_title("Top 15 Crime Types with Weapon Usage")
    ax.set_xlabel("Number of Crimes (with weapons)")
    ax.set_ylabel("Crime Type")
    st.pyplot(fig)

# TAB 2: Time Analysis
with tab2:

    st.header("Crime Distribution over Time")

    # Crime by hour
    st.subheader("Crime Frequency by Hour of Day")

    crime_by_hour = df['OCC_HOUR'].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(12,6))
    sns.lineplot(x=crime_by_hour.index, y=crime_by_hour.values, marker="o", ax=ax)
    ax.set_title("Crime Frequency by Hour of Day")
    ax.set_xlabel("Hour (0–23)")
    ax.set_ylabel("Number of Crimes")
    ax.set_xticks(range(0,24))
    st.pyplot(fig)

    # Crime by weekday
    st.subheader("Crime Frequency by Weekday")

    crime_by_day = df['OCC_WEEKDAY'].value_counts().sort_index()
    weekday_labels = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

    fig, ax = plt.subplots(figsize=(10,5))
    sns.barplot(x=weekday_labels, y=crime_by_day.values, ax=ax)
    ax.set_title("Crime Frequency by Weekday")
    ax.set_xlabel("Weekday")
    ax.set_ylabel("Number of Crimes")
    st.pyplot(fig)

    # Heatmap
    st.subheader("Crime Intensity by Weekday and Hour")

    pivot = df.pivot_table(
        index='OCC_WEEKDAY',
        columns='OCC_HOUR',
        aggfunc='size',
        fill_value=0
    )

    fig, ax = plt.subplots(figsize=(14,6))
    sns.heatmap(pivot, cmap='viridis', ax=ax)
    ax.set_title("Crime Intensity by Hour and Weekday")
    ax.set_xlabel("Hour")
    ax.set_ylabel("Weekday (Mon–Sun as 0–6)")
    st.pyplot(fig)

# TAB 3: Location
with tab3:

    st.header("Location & Hotspots")

    st.subheader("Crime Hotspots in Los Angeles (Sample of 50,000 points)")

    sample = df.sample(50000)

    fig, ax = plt.subplots(figsize=(8,8))
    sns.scatterplot(
        x='LON', 
        y='LAT', 
        data=sample, 
        alpha=0.3, 
        s=10, 
        ax=ax
    )
    ax.set_title("Crime Hotspots in Los Angeles")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    st.pyplot(fig)

    # Crimes by LAPD Area
    st.subheader("Crime by LAPD Area")

    area_counts = df['AREA_NAME'].value_counts()

    fig, ax = plt.subplots(figsize=(10,7))
    sns.barplot(
        x=area_counts.values, 
        y=area_counts.index, 
        ax=ax
    )
    ax.set_title("Total Crime Count by LAPD Area")
    ax.set_xlabel("Number of Crimes")
    ax.set_ylabel("LAPD Area")
    st.pyplot(fig)

# TAB 4: Victim Profile
with tab4:

    st.header("Victim Demographics")

    # Age distribution
    st.subheader("Age Distribution of Victims")

    age_data = df[df['VICT_AGE'] > 0]

    fig, ax = plt.subplots(figsize=(12,6))
    sns.histplot(age_data['VICT_AGE'], bins=50, kde=False, ax=ax)
    ax.set_title("Distribution of Victim Age")
    ax.set_xlabel("Age")
    ax.set_ylabel("Number of Victims")
    st.pyplot(fig)

    st.text("Victim count by age:")
    st.write(age_data['VICT_AGE'].value_counts())

    # Age by Sex heatmap
    st.subheader("Victim Age Distribution by Sex")

    pivot_age = age_data.pivot_table(
        index='VICT_AGE',
        columns='VICT_SEX',
        aggfunc='size',
        fill_value=0
    )

    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(pivot_age, cmap='viridis', ax=ax)
    ax.set_title("Victim Age Distribution by Sex")
    ax.set_xlabel("Sex")
    ax.set_ylabel("Age")
    st.pyplot(fig)

    # Victim descent
    st.subheader("Victim Descent")

    descent_counts = df['VICT_DESCENT_FULL'].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(8,6))
    sns.barplot(
        x=descent_counts.values, 
        y=descent_counts.index, 
        ax=ax
    )
    ax.set_title("Victims by Descent (Top 10)")
    ax.set_xlabel("Number of Victims")
    ax.set_ylabel("Descent")
    st.pyplot(fig)