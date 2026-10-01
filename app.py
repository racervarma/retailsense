"""RetailSense Analytics Dashboard."""

import sqlite3

import pandas as pd
import plotly.express as px
import streamlit as st

from utils import calculate_revenue

st.set_page_config(page_title="RetailSense Analytics Dashboard", layout="wide")

DB_PATH = "outputs/retailsense.db"


@st.cache_data
def load_data(db_path=DB_PATH):
    """Load, join, and enrich the retail tables from the SQLite database."""
    conn = sqlite3.connect(db_path)
    try:
        orders = pd.read_sql("SELECT * FROM orders", conn)
        customers = pd.read_sql("SELECT * FROM customers", conn)
        products = pd.read_sql("SELECT * FROM products", conn)
    finally:
        conn.close()

    full_df = orders.merge(customers, on="customer_id", how="inner")
    full_df = full_df.merge(products, on="product_id", how="inner")

    full_df["revenue"] = full_df.apply(
        lambda row: calculate_revenue(row["price"], row["quantity"], row["discount_pct"]),
        axis=1,
    )
    return full_df


full_df = load_data()

# --- Sidebar filters ---
st.sidebar.header("Filters")

selected_category = st.sidebar.selectbox(
    "Category",
    ["All", "Electronics", "Clothing", "Food", "Books"],
)

min_rating = st.sidebar.slider(
    "Minimum Product Rating",
    min_value=1.0,
    max_value=5.0,
    value=1.0,
    step=0.1,
)

# --- Apply filters ---
filtered_df = full_df
if selected_category != "All":
    filtered_df = filtered_df[filtered_df["category"] == selected_category]
filtered_df = filtered_df[filtered_df["rating"] >= min_rating]

# --- Main area ---
st.title("🛒 RetailSense Analytics Dashboard")

st.subheader("Overview Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹{filtered_df['revenue'].sum():,.0f}")
col2.metric("Total Orders", f"{filtered_df['order_id'].nunique():,}")
col3.metric("Average Product Rating", f"{filtered_df['rating'].mean():.1f}")

st.subheader("Filtered Data View")
st.dataframe(filtered_df.head(50), width="stretch")

st.subheader("Business Insights")
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    revenue_by_age = (
        filtered_df.groupby("age_group", observed=True)["revenue"].sum().reset_index()
    )
    age_fig = px.bar(
        revenue_by_age,
        x="age_group",
        y="revenue",
        title="Revenue by Age Group",
    )
    age_fig.update_layout(xaxis_title="Age Group", yaxis_title="Total Revenue")
    st.plotly_chart(age_fig, width="stretch")

with chart_col2:
    price_fig = px.box(
        filtered_df,
        x="category",
        y="price",
        title="Price Distribution by Category",
    )
    price_fig.update_layout(xaxis_title="Category", yaxis_title="Price")
    st.plotly_chart(price_fig, width="stretch")

st.subheader("Upload Custom Data")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    custom_df = pd.read_csv(uploaded_file)
    st.write(f"**Rows:** {len(custom_df)} | **Columns:** {len(custom_df.columns)}")
    st.write("**First 10 Rows**")
    st.dataframe(custom_df.head(10), width="stretch")
    st.write("**Summary Statistics**")
    st.dataframe(custom_df.describe(), width="stretch")
