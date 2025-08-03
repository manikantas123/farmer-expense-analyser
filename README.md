# 🚜 Farming Expense Pattern Analyzer

A simple, interactive Streamlit dashboard that helps farmers analyze and visualize their farming expenses. This tool is designed to assist in identifying spending patterns, improving budgeting decisions, and promoting data-driven farming.

---

## 🌟 Features

- 📁 Upload your farming expenses CSV file
- 🗂️ Automatically detects categories like Seeds, Fertilizers, Labour, etc.
- 🧮 Calculates total, average, and per-category expenses
- 🥧 Displays a pie chart for expense distribution
- 📊 Shows bar and line charts to track trends over time
- 📋 Interactive table of raw expense data

---

## 📂 Sample CSV Format

Ensure your CSV file contains the following columns:

| Date       | Category    | Amount | Description     |
|------------|-------------|--------|-----------------|
| 2025-01-05 | Fertilizers | 2000   | Urea purchase   |
| 2025-01-10 | Seeds       | 1000   | Paddy seeds     |
| 2025-01-15 | Labour      | 1500   | Harvesting work |

- **Date**: Format should be YYYY-MM-DD  
- **Category**: Expense type (Seeds, Fertilizers, Labour, etc.)  
- **Amount**: Numeric value of expense  
- **Description**: Optional notes for the entry  

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/farming-expense-analyzer.git
cd farming-expense-analyzer
