# ==========================================
# STREAMLIT DASHBOARD
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Personal Expense Dashboard",
    layout="wide"
)

st.title(" PERSONAL EXPENSE ANALYTICS DASHBOARD")

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("cleaned_expense_dataset.csv")

# Convert Date
df['Date'] = pd.to_datetime(df['Date'])

# ==========================================
# FILTER DATA
# ==========================================

income_df = df[df['Type'] == 'Income']
expense_df = df[df['Type'] == 'Expense']

# ==========================================
# FINANCIAL SUMMARY
# ==========================================

total_income = income_df['Amount'].sum()
total_expense = expense_df['Amount'].sum()
savings = total_income - total_expense

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
# CATEGORY ANALYSIS
# ==========================================

category_expense = expense_df.groupby(
    'Category'
)['Amount'].sum()

st.subheader(" Category Wise Expense")

fig, ax = plt.subplots(figsize=(10,5))

category_expense.plot(
    kind='bar',
    ax=ax
)

ax.set_title("Category Wise Expenses")

st.pyplot(fig)

# ==========================================
# PIE CHART
# ==========================================

st.subheader(" Expense Distribution")

fig, ax = plt.subplots(figsize=(7,7))

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

monthly_expense = expense_df.groupby(
    expense_df['Date'].dt.strftime('%Y-%m')
)['Amount'].sum()

st.subheader(" Monthly Expense Trend")

fig, ax = plt.subplots(figsize=(12,5))

monthly_expense.plot(
    kind='line',
    marker='o',
    ax=ax
)

ax.grid(True)

st.pyplot(fig)

# ==========================================
# PAYMENT METHOD ANALYSIS
# ==========================================

payment_analysis = expense_df.groupby(
    'Payment_Method'
)['Amount'].sum()

st.subheader(" Payment Method Analysis")

fig, ax = plt.subplots(figsize=(8,5))

payment_analysis.plot(
    kind='bar',
    ax=ax
)

st.pyplot(fig)

# ==========================================
# TOP 10 EXPENSES
# ==========================================

top_expenses = expense_df.sort_values(
    by='Amount',
    ascending=False
).head(10)

st.subheader(" Top 10 Highest Expenses")

st.dataframe(
    top_expenses[
        ['Date', 'Category', 'Amount', 'Merchant']
    ]
)

# ==========================================
# MACHINE LEARNING PREDICTION
# ==========================================

X = expense_df[['Month', 'Year']]
y = expense_df['Amount']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

future_data = pd.DataFrame({
    'Month': [12],
    'Year': [2026]
})

future_prediction = model.predict(
    future_data
)

st.subheader(" Future Expense Prediction")

st.success(
    f"Predicted Expense for Dec 2026 : ₹ {future_prediction[0]:,.2f}"
)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.success(
    " DASHBOARD CREATED SUCCESSFULLY!"
)