import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. Page Configuration ---
st.set_page_config(page_title="Global Terrorism Analytics", page_icon="🌍", layout="wide")

st.title("🌍 Global Terrorism Database Analysis")
st.markdown("An interactive dashboard exploring terrorist attacks from **1970 to 2017**.")

# --- 2. Load Data (Cached for Performance) ---
@st.cache_data
def load_data():
    # Load dataset (adjust filename if necessary)
    # df = pd.read_csv('./archive/globalterrorismdb_0718dist.csv', encoding='ISO-8859-1', low_memory=False)
    df = pd.read_csv('global_terror_LITE.zip', compression='zip', encoding='ISO-8859-1', low_memory=False)
    
    # Cleaning & Renaming

    df.rename(columns={
        'iyear': 'Year', 
        'imonth': 'Month', 
        'iday': 'Day',
        'country_txt': 'Country', 
        'region_txt': 'Region',
        'attacktype1_txt': 'AttackType', 
        'target1': 'Target',
        'nkill': 'Killed', 
        'nwound': 'Wounded',
        'gname': 'Group', 
        'targtype1_txt': 'TargetType',
        'weaptype1_txt': 'Weapon_type', 
        'latitude': 'Latitude', 
        'longitude': 'Longitude',
        'city': 'City'  
    }, inplace=True)
    
    # Create Casualties column
    df['Casualties'] = df['Killed'].fillna(0) + df['Wounded'].fillna(0)
    
    return df

# Show a loading spinner while data loads
with st.spinner('Loading massive dataset...'):
    df = load_data()

# --- 3. Sidebar Filters ---
st.sidebar.header("Filter Options")
selected_year = st.sidebar.slider("Select Year Range", 1970, 2017, (2000, 2017))
selected_region = st.sidebar.multiselect("Select Region", df['Region'].unique(), default=df['Region'].unique())

# Filter the dataframe based on user selection
filtered_df = df[(df['Year'] >= selected_year[0]) & 
                 (df['Year'] <= selected_year[1]) & 
                 (df['Region'].isin(selected_region))]

# --- 4. Key Metrics Row ---
# We use 4 columns now to fit the extra metric
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Attacks", f"{filtered_df.shape[0]:,}")
col2.metric("Total Casualties", f"{int(filtered_df['Casualties'].sum()):,}")

# Logic for Metric 3: Most Active Group (Excluding Unknown)
known_groups_df = filtered_df[filtered_df['Group'] != 'Unknown']
if not known_groups_df.empty:
    most_active_group = known_groups_df['Group'].mode()[0]
else:
    most_active_group = "None"

col3.metric("Most Active Group", most_active_group)

# Logic for Metric 4: Most Targeted Country
if not filtered_df.empty:
    most_targeted_country = filtered_df['Country'].mode()[0]
else:
    most_targeted_country = "None"

col4.metric("Most Targeted Country", most_targeted_country)

st.markdown("---")

# --- 5. Visualizations ---

# Row 1: Map and Trend
row1_col1, row1_col2 = st.columns([2, 1])

with row1_col1:
    st.subheader("📍 Geospatial Distribution")
    # Using Plotly for the map (Efficient & Interactive)
    # We limit points to avoid browser crash if range is too large
    map_data = filtered_df[filtered_df['Casualties'] > 0]  # Show only attacks with impact
    if len(map_data) > 5000:
        map_data = map_data.sample(5000) # Sample if too big
        st.warning("⚠️ Displaying a random sample of 5,000 attacks to maintain performance.")
    
    fig_map = px.scatter_geo(
        map_data, lat='Latitude', lon='Longitude',
        color='Region', size='Casualties',
        hover_name='Country', projection='natural earth',
        template='plotly_dark'
    )
    st.plotly_chart(fig_map, use_container_width=True)

with row1_col2:
    st.subheader("📈 Attacks Over Time")
    attacks_per_year = filtered_df['Year'].value_counts().sort_index()
    st.line_chart(attacks_per_year)

st.markdown("---")

# Row 2: Analysis Charts
row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("🔥 Top Attacking Groups")
    # Filter out Unknown
    top_groups = filtered_df[filtered_df['Group'] != 'Unknown']['Group'].value_counts().head(10)
    fig_groups = px.bar(x=top_groups.values, y=top_groups.index, orientation='h', 
                        labels={'x': 'Count', 'y': 'Group'}, color=top_groups.values)
    st.plotly_chart(fig_groups, use_container_width=True)

with row2_col2:
    st.subheader("🎯 Attack Targets")
    top_targets = filtered_df['TargetType'].value_counts().head(10)
    fig_targets = px.pie(values=top_targets.values, names=top_targets.index, hole=0.4)
    st.plotly_chart(fig_targets, use_container_width=True)

# --- 6. Footer ---

st.markdown("Data Source: Global Terrorism Database (GTD) | Final Project Winter 2025 | Aravind Kagganti Anjinamurthy")
