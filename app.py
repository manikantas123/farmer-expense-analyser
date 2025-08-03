import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Farming Expense Analyzer", layout="wide")

st.title("🌾 Farming Expense Pattern Analyzer")

# Step 1: Upload or Load Sample Data
uploaded_file = st.file_uploader("📤 Upload your Farming Expenses CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully.")
else:
    df = pd.read_csv("data/expenses.csv")
    st.info("ℹ️ Using sample data from 'data/expenses.csv'")

# Step 2: Convert date to proper format and extract month
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%B')

# Step 3: Total Expense Summary
total = df['Amount'].sum()
st.metric("💰 Total Expense", f"₹ {total}")

# Step 4: Category-wise Expense Chart
st.subheader("📊 Expenses by Category")
category_data = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
st.bar_chart(category_data)

# Step 5: Month-wise Trend Chart
st.subheader("📈 Monthly Expense Trend")
monthly_data = df.groupby("Month")["Amount"].sum()
st.line_chart(monthly_data)

# Step 6: Show High-Cost Items
st.subheader("🚨 High Expense Alerts (Above ₹3000)")
high_cost = df[df["Amount"] > 3000]
if not high_cost.empty:
    st.warning("Found high-value expenses:")
    st.dataframe(high_cost)
else:
    st.success("No high-cost entries found ✅")
