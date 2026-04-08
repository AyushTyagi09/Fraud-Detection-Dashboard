import pandas as pd
import random
from datetime import datetime, timedelta

rows = []

locations = ["Bangalore", "Delhi", "Mumbai", "Chennai", "Hyderabad"]
start_time = datetime(2024, 4, 1, 10, 0, 0)

for i in range(1, 501):
    transaction_id = i
    user_id = random.randint(100, 120)
    amount = random.randint(500, 100000)
    location = random.choice(locations)
    timestamp = start_time + timedelta(seconds=random.randint(0, 10000))

    rows.append([transaction_id, user_id, amount, location, timestamp])

df = pd.DataFrame(rows, columns=[
    "transaction_id", "user_id", "amount", "location", "timestamp"
])

df.to_csv("transactions.csv", index=False)

print("Done! CSV created")