# PERSONAL EXPENSE ANALYTICS PROJECT DOCUMENTATION


# 1. Introduction

The Personal Expense Analytics Project is a Data Analytics and Machine Learning project developed using Python. The purpose of this project is to analyze personal financial transactions, visualize spending patterns, and predict future expenses.

This project helps users understand:

* Total income and expenses
* Savings
* Category-wise spending
* Monthly expense trends
* Payment method usage
* Future expense prediction

The project also includes an interactive dashboard developed using Streamlit.

---

# 2. Objectives

The main objectives of this project are:

* To clean and preprocess expense data
* To analyze income and expense transactions
* To visualize expense patterns using graphs
* To build a Machine Learning model for prediction
* To create an interactive dashboard for users

---

# 3. Technologies Used

| Technology   | Purpose               |
| ------------ | --------------------- |
| Python       | Programming Language  |
| Pandas       | Data Analysis         |
| NumPy        | Numerical Operations  |
| Matplotlib   | Data Visualization    |
| Scikit-learn | Machine Learning      |
| Streamlit    | Dashboard Development |

---

# 4. Dataset Description

The dataset used in this project is:

personal_expense_dataset.csv

## Dataset Columns

| Column Name    | Description         |
| -------------- | ------------------- |
| Date           | Transaction Date    |
| Type           | Income or Expense   |
| Category       | Expense Category    |
| Amount         | Transaction Amount  |
| Merchant       | Merchant Name       |
| Payment_Method | Payment Method Used |

---

# 5. Data Preprocessing

The following preprocessing steps were performed:

## 5.1 Handling Missing Values

The dataset was checked for missing values using:

df.isnull().sum()


## 5.2 Removing Duplicate Records

Duplicate rows were removed using:

df.drop_duplicates()

## 5.3 Date Conversion

The Date column was converted into datetime format:

df['Date'] = pd.to_datetime(df['Date'])

## 5.4 Feature Engineering

New columns were created:

* Month
* Year

---

# 6. Financial Analysis

The project performs the following analyses:

## 6.1 Total Income Calculation

Calculates total income from all income transactions.

## 6.2 Total Expense Calculation

Calculates total expenses from all expense transactions.

## 6.3 Savings Calculation

Savings are calculated as:

\text{Savings} = \text{Total Income} - \text{Total Expense}

---

# 7. Data Visualization

The project includes multiple visualizations:

## 7.1 Category Wise Expense Analysis

A bar chart is used to display expenses across different categories.

## 7.2 Expense Distribution Pie Chart

A pie chart shows the percentage distribution of expenses.

## 7.3 Monthly Expense Trend

A line graph visualizes monthly expense trends over time.

## 7.4 Payment Method Analysis

A bar chart shows the usage of different payment methods.

## 7.5 Advanced Dashboard

A combined dashboard includes:

* Bar Chart
* Pie Chart
* Line Graph
* Payment Analysis

---

# 8. Machine Learning Model

## 8.1 Algorithm Used

The project uses:

### Linear Regression

for future expense prediction.

---

## 8.2 Features Used

Input features:

* Month
* Year

Target variable:

* Amount

---

## 8.3 Train-Test Split

The dataset was divided into:

* 80% Training Data
* 20% Testing Data

---

## 8.4 Model Evaluation

The model performance was evaluated using:

### Mean Absolute Error (MAE)

MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|

---

# 9. Future Expense Prediction

The trained model predicts future expenses for upcoming months and years.

Example:

* Predicted Expense for December 2026

---

# 10. Streamlit Dashboard

An interactive dashboard was developed using Streamlit.

## Dashboard Features

* Financial Summary Cards
* Dataset Preview
* Interactive Charts
* Expense Analysis
* Future Prediction Graph

## Running the Dashboard

streamlit run dashboard.py

---

# 11. Project Structure

PERSONAL_EXPENSE_ANALYTICS/
│
├── dataset/
│   └── personal_expense_dataset.csv
│
├── screenshots/
│   ├── financial_summary.png
│   ├── category_expense.png
│   ├── monthly_trend.png
│   ├── payment_analysis.png
│   ├── dashboard.png
│   └── prediction.png
│
├── main.py
├── dashboard.py
├── cleaned_expense_dataset.csv
├── financial_summary.csv
├── README.md
└── documentation.md

---

# 12. Output Generated

The project generates:

* Cleaned Dataset
* Financial Summary Report
* Expense Visualizations
* Dashboard Visualizations
* Future Expense Predictions

---

# 13. Advantages of the Project

* Easy financial tracking
* Better expense understanding
* Expense trend analysis
* Future expense forecasting
* Interactive dashboard visualization

---

# 14. Future Enhancements

Future improvements can include:

* Budget alert system
* Login authentication
* Real-time expense tracking
* Advanced Machine Learning models
* Cloud deployment

---

# 15. Conclusion

The Personal Expense Analytics Project successfully demonstrates:

* Data Cleaning
* Data Analysis
* Data Visualization
* Machine Learning
* Dashboard Development

This project helps users analyze their financial activities efficiently and predict future expenses using Data Analytics and Machine Learning techniques.
