# Step 1: Create Database
CREATE DATABASE fraud_db;
USE fraud_db;

# Step 2: Create Table
CREATE TABLE transactions (
    transaction_id INT,
    user_id INT,
    amount INT,
    location VARCHAR(50),
    timestamp DATETIME
);

# STEP 3: Import CSV

# Step 4: Verify Data
SELECT COUNT(*) FROM transactions;

# STEP 5: Create Fraud Table
CREATE TABLE fraud_results AS
SELECT *,
    CASE 
        WHEN amount > 50000 THEN 1
        ELSE 0
    END AS is_suspicious
FROM transactions;

# Verify Final Data
SELECT COUNT(*) FROM fraud_results;
