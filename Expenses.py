# PERSONAL EXPENSE ANALYTICS PROJECT

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
# LOAD DATASET

df = pd.read_csv("personal_expense_dataset.csv")

print("First 5 Records")
print(df.head())

# DATA CLEANING


print("\nChecking Missing Values")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Create Month and Year columns
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

print("\nData Cleaning Completed!")

# BASIC ANALYSIS

# Separate Income and Expense
income_df = df[df['Type'] == 'Income']
expense_df = df[df['Type'] == 'Expense']

# Total Income
total_income = income_df['Amount'].sum()

# Total Expense
total_expense = expense_df['Amount'].sum()

# Savings
savings = total_income - total_expense

print("\n========== FINANCIAL SUMMARY ==========")
print("Total Income :", total_income)
print("Total Expense :", total_expense)
print("Savings :", savings)

# CATEGORY-WISE ANALYSIS

category_expense = expense_df.groupby(
    'Category'
)['Amount'].sum()

print("\nCategory Wise Expense")
print(category_expense)

# VISUALIZATION - BAR CHART

plt.figure(figsize=(10,6))

category_expense.plot(kind='bar')

plt.title("Category Wise Expenses")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# VISUALIZATION - PIE CHART

plt.figure(figsize=(8,8))

category_expense.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Expense Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# MONTHLY EXPENSE TREND

monthly_expense = expense_df.groupby(
    expense_df['Date'].dt.strftime('%Y-%m')
)['Amount'].sum()

print("\nMonthly Expense Trend")
print(monthly_expense)

# Line Graph
plt.figure(figsize=(12,6))

monthly_expense.plot(
    kind='line',
    marker='o'
)

plt.title("Monthly Expense Trend")
plt.xlabel("Month")
plt.ylabel("Expense Amount")

plt.grid(True)
plt.tight_layout()
plt.show()

# PAYMENT METHOD ANALYSIS

payment_analysis = expense_df.groupby(
    'Payment_Method'
)['Amount'].sum()

print("\nPayment Method Analysis")
print(payment_analysis)

# Payment Method Chart
plt.figure(figsize=(8,5))

payment_analysis.plot(kind='bar')

plt.title("Payment Method Usage")
plt.xlabel("Payment Method")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show(block=True)

# TOP 10 HIGHEST EXPENSES

top_expenses = expense_df.sort_values(
    by='Amount',
    ascending=False
).head(10)

print("\nTop 10 Highest Expenses")

print(top_expenses[
    ['Date', 'Category', 'Amount', 'Merchant']
])

# DASHBOARD STYLE SUMMARY

summary = pd.DataFrame({
    'Metric': [
        'Total Income',
        'Total Expense',
        'Savings'
    ],
    'Amount': [
        total_income,
        total_expense,
        savings
    ]
})

print("\nDashboard Summary")
print(summary)

# Save Dashboard Report
summary.to_csv(
    "financial_summary.csv",
    index=False
)

# MACHINE LEARNING PREDICTION MODEL

print("\n========== PREDICTION MODEL ==========")

# Use only expense data
ml_df = expense_df.copy()

# Features
X = ml_df[['Month', 'Year']]

# Target
y = ml_df['Amount']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Linear Regression Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Model Accuracy
mae = mean_absolute_error(
    y_test,
    predictions
)

print("Mean Absolute Error :", mae)

# Predict Future Expense
future_data = pd.DataFrame({
    'Month': [12],
    'Year': [2026]
})

future_prediction = model.predict(
    future_data
)

print(
    "Predicted Expense for Dec 2026 :",
    future_prediction[0]
)

# SAVE CLEANED DATASET


df.to_csv(
    "cleaned_expense_dataset.csv",
    index=False
)

print("\nCleaned Dataset Saved!")

# PROJECT COMPLETED

print("\nPERSONAL EXPENSE ANALYTICS COMPLETED SUCCESSFULLY!")
# ==============================
# ADVANCED DASHBOARD
# ==============================

fig, axes = plt.subplots(2, 2, figsize=(15,10))

# 1. Category Expense Bar Chart
category_expense.plot(
    kind='bar',
    ax=axes[0,0]
)

axes[0,0].set_title("Category Wise Expense")
axes[0,0].set_xlabel("Category")
axes[0,0].set_ylabel("Amount")

# 2. Expense Distribution Pie Chart
category_expense.plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=axes[0,1]
)

axes[0,1].set_title("Expense Distribution")
axes[0,1].set_ylabel("")

# 3. Monthly Expense Trend
monthly_expense.plot(
    kind='line',
    marker='o',
    ax=axes[1,0]
)

axes[1,0].set_title("Monthly Expense Trend")
axes[1,0].set_xlabel("Month")
axes[1,0].set_ylabel("Expense")

# 4. Payment Method Analysis
payment_analysis.plot(
    kind='bar',
    ax=axes[1,1]
)

axes[1,1].set_title("Payment Method Usage")
axes[1,1].set_xlabel("Payment Method")
axes[1,1].set_ylabel("Amount")

# Dashboard Layout
plt.suptitle(
    "PERSONAL EXPENSE ANALYTICS DASHBOARD",
    fontsize=18,
    fontweight='bold'
)

plt.tight_layout()

plt.show()
# ==========================================
# STREAMLIT DASHBOARD
# ==========================================

import streamlit as st

# Page Config
st.set_page_config(
    page_title="Personal Expense Analytics",
    layout="wide"
)

# Title
st.title(" PERSONAL EXPENSE ANALYTICS DASHBOARD")

st.markdown("---")

# ==========================================
# FINANCIAL SUMMARY
# ==========================================

st.subheader(" Financial Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Income",
    f"₹ {total_income:,.2f}"
)

col2.metric(
    "Total Expense",
    f"₹ {total_expense:,.2f}"
)

col3.metric(
    "Savings",
    f"₹ {savings:,.2f}"
)

st.markdown("---")

# ==========================================
# DATASET PREVIEW
# ==========================================

st.subheader(" Dataset Preview")

st.dataframe(df.head())

# ==========================================
# CATEGORY WISE EXPENSE
# ==========================================

st.subheader(" Category Wise Expense")

fig, ax = plt.subplots(figsize=(10,5))

category_expense.plot(
    kind='bar',
    ax=ax
)

ax.set_title("Category Wise Expenses")
ax.set_xlabel("Category")
ax.set_ylabel("Amount")

plt.xticks(rotation=0)

st.pyplot(fig)

# ==========================================
# PIE CHART
# ==========================================

st.subheader(" Expense Distribution")

fig, ax = plt.subplots(figsize=(8,8))

category_expense.plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=ax
)

ax.set_ylabel("")

st.pyplot(fig)

# ==========================================
# MONTHLY EXPENSE TREND
# ==========================================

st.subheader(" Monthly Expense Trend")

fig, ax = plt.subplots(figsize=(12,5))

monthly_expense.plot(
    kind='line',
    marker='o',
    ax=ax
)

ax.set_title("Monthly Expense Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Expense Amount")

ax.grid(True)

plt.xticks(rotation=45)

st.pyplot(fig)

# ==========================================
# PAYMENT METHOD ANALYSIS
# ==========================================

st.subheader(" Payment Method Analysis")

fig, ax = plt.subplots(figsize=(8,5))

payment_analysis.plot(
    kind='bar',
    ax=ax
)

ax.set_title("Payment Method Usage")
ax.set_xlabel("Payment Method")
ax.set_ylabel("Amount")

plt.xticks(rotation=0)

st.pyplot(fig)

# ==========================================
# TOP 10 EXPENSES
# ==========================================

st.subheader(" Top 10 Highest Expenses")

st.dataframe(
    top_expenses[
        ['Date', 'Category', 'Amount', 'Merchant']
    ]
)

# ==========================================
# PREDICTION MODEL
# ==========================================

st.subheader(" Expense Prediction")

st.write(
    f"Predicted Expense for December 2026 : ₹ {future_prediction[0]:,.2f}"
)

# Future Prediction Graph
future_months = pd.DataFrame({
    'Month': [1,2,3,4,5,6,7,8,9,10,11,12],
    'Year': [2026]*12
})

future_values = model.predict(future_months)

prediction_df = pd.DataFrame({
    'Month': future_months['Month'],
    'Predicted Expense': future_values
})

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(
    prediction_df['Month'],
    prediction_df['Predicted Expense'],
    marker='o'
)

ax.set_title("Future Expense Prediction")
ax.set_xlabel("Month")
ax.set_ylabel("Predicted Expense")

ax.grid(True)

st.pyplot(fig)