import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configure Streamlit page
st.set_page_config(page_title="Farming Expense Pattern Analyzer", layout="wide")

# Title and intro
st.title("🚜 Farming Expense Pattern Analyzer")
st.markdown("Analyze your farming expenses by category and time!")

# Load and cache data
@st.cache_data
def load_data():
    df = pd.read_csv("expenses.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")
categories = st.sidebar.multiselect(
    "Select Categories:",
    options=df["Category"].unique(),
    default=list(df["Category"].unique())
)
date_range = st.sidebar.date_input(
    "Select Date Range:",
    value=[df["Date"].min(), df["Date"].max()]
)

# Filter data based on sidebar selections
filtered_df = df[
    (df["Category"].isin(categories)) &
    (df["Date"] >= pd.to_datetime(date_range[0])) &
    (df["Date"] <= pd.to_datetime(date_range[1]))
]

# Main content
st.subheader("📋 Filtered Expense Data")
st.dataframe(filtered_df, use_container_width=True)

# Total expense metric
total_expense = filtered_df["Amount"].sum()
st.metric("💰 Total Expenses", f"₹{total_expense:,.2f}")

# Bar chart for category-wise expense
st.subheader("📊 Category-wise Expense Breakdown")
category_data = filtered_df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
st.bar_chart(category_data)

# Pie chart
st.subheader("🧁 Category-wise Expense Pie Chart")
if not category_data.empty:
    fig1, ax1 = plt.subplots()
    ax1.pie(category_data, labels=category_data.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Draw as circle
    st.pyplot(fig1)
else:
    st.warning("No category data to display in pie chart.")

# Monthly trend chart
st.subheader("📈 Monthly Expense Trend")
monthly_data = filtered_df.resample('M', on='Date')["Amount"].sum()
st.line_chart(monthly_data)

# Footer
st.success("✅ Analysis complete. Adjust filters in the sidebar to explore further!")
