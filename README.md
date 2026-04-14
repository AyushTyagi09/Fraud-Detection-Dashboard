# 🚀 End-to-End Fraud Detection Data Pipeline (SQL + Power BI)

## 📌 Overview
This project demonstrates an end-to-end data pipeline for detecting suspicious financial transactions using Python, SQL, and Power BI.

The pipeline ingests raw transaction data, performs data cleaning and feature engineering, applies fraud detection logic using SQL, and visualizes insights through an interactive Power BI dashboard.

---

## 🔄 Data Pipeline Flow
Raw Data (CSV) → Python ETL → SQL Processing → Fraud Detection Logic → Power BI Dashboard

---

## ⚙️ Tech Stack
- Python (Pandas)
- SQL (SQLite)
- Power BI
- Git & GitHub

---

## 📂 Project Structure
Fraud-Detection-Dashboard/
│
├── Data/
│ ├── raw/
│ │ └── transactions.csv
│ ├── processed/
│ │ └── clean_transactions.csv
│ └── transactions.db
│
├── Scripts/
│ ├── ingest.py
│ ├── transform.py
│ └── load.py
│
├── SQL/
│ ├── schema.sql
│ └── queries.sql
│
├── PowerBI/
│ └── fraud_dashboard.pbix
│
├── Screenshots/
│ ├── dashboard.png
│ └── sql_output.png
│
├── README.md


---

## 🔧 Features
- Data ingestion from CSV using Python
- Data cleaning and preprocessing
- Feature engineering:
  - Transaction hour extraction
  - High-value transaction flag
- Fraud detection logic using SQL (`CASE WHEN`)
- Interactive dashboard using Power BI
- End-to-end pipeline design

---

## 🧠 Fraud Detection Logic
Transactions are flagged as suspicious based on amount:

```sql
CASE 
    WHEN amount > 50000 THEN 1
    ELSE 0
END AS is_suspicious
```


## 📊 Dashboard Highlights

- Total Transactions
- Total Transaction Amount
- Suspicious vs Normal Transactions
- Transactions by Location


## 📈 Key Insights
- Processed 500+ transactions
- ~48% transactions flagged as suspicious
- Chennai and Delhi have highest transaction volume
- Total transaction volume ≈ ₹25M


## 🚀 How to Run the Project

1. Clone the Repository
git clone https://github.com/AyushTyagi09/Fraud-Detection-Dashboard.git
cd Fraud-Detection-Dashboard

2. Run Python ETL Pipeline
python Scripts/ingest.py
python Scripts/transform.py
python Scripts/load.py

3. Run SQL Queries
-> Open SQL/schema.sql
-> Execute in SQLite / DB Browser

4. Open Dashboard
-> Open PowerBI/fraud_dashboard.pbix in Power BI Desktop


## 📸 Screenshots
### Dashboard
![Dashboard](Screenshots/dashboard.png)

### SQL Output
![SQL Output](Screenshots/sql_output.png)

## 🎯 Project Objective

To demonstrate practical skills in:

- Data Engineering (ETL pipeline)
- SQL-based data transformation
- Data Visualization
- End-to-end project development


## 🙌 Author

Ayush Tyagi