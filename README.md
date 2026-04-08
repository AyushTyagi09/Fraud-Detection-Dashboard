# 🚀 Fraud Detection Dashboard (SQL + Power BI)

## 📌 Overview
This project demonstrates an end-to-end data analytics pipeline for detecting fraudulent transactions using SQL and visualizing insights with Power BI.

The system processes transaction data, applies fraud detection logic, and presents key insights through an interactive dashboard.

---

## 🛠️ Tech Stack
- **MySQL (SQL)** – Data storage and fraud detection logic  
- **Power BI** – Data visualization and dashboard creation  
- **Python (Optional)** – Synthetic data generation  

---

## 📊 Key Features
- Rule-based fraud detection using SQL  
- Interactive Power BI dashboard connected to database  
- Real-time data refresh capability  
- Visual insights including:
  - Fraud vs Normal transactions
  - Transactions by location
  - Total transaction metrics  

---

## 🧠 Fraud Detection Logic
Fraudulent transactions are identified using a simple business rule:
IF amount > 50000 THEN Fraud (1)
ELSE Normal (0)


This logic is implemented using SQL CASE statements.

---
## 📁 Project Structure
Fraud-Detection-Dashboard/
│── data/
│ └── transactions.csv
│
│── sql/
│ └── fraud_queries.sql
│
│── powerbi/
│ └── Fraud_Detection_Dashboard.pbix
│
│── scripts/
│ └── generate_data.py
│
│── screenshots/
│ ├── dashboard_final.png
│ ├── sql_output.png
│
│── README.md


---

## 📸 Screenshots

### 🔹 Dashboard Overview
![Dashboard](screenshots/dashboard_final.png)

### 🔹 SQL Output (Fraud Detection)
![SQL](screenshots/sql_output.png)

---

## ⚙️ How to Run the Project

### 1️⃣ Setup Database
- Create database `fraud_db` in MySQL
- Import `transactions.csv` into `transactions` table

### 2️⃣ Run SQL Queries
- Execute `fraud_queries.sql`
- This will generate `fraud_results` table with fraud flag

### 3️⃣ Open Power BI
- Open `.pbix` file
- Connect to MySQL (`fraud_db`)
- Refresh data

---

## 📈 Insights
- Total Transactions: 500
- Fraud Transactions: 240 (48%)
- Normal Transactions: 260 (52%)
- Highest transactions observed in Chennai and Delhi

---

## 🚀 Future Improvements
- Machine Learning-based fraud detection  
- Real-time streaming data pipeline  
- Advanced anomaly detection techniques  

---

## 👨‍💻 Author
**Ayush Tyagi**  
B.Tech IT Student | Aspiring Data Engineer  