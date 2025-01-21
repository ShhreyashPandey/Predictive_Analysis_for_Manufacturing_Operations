import pandas as pd
import numpy as np

np.random.seed(42)

def generate_data(rows=1000):
    data = {"Machine_ID": np.arange(1,rows + 1),
        "Temperature": np.random.uniform(50, 200, rows),  # Temperature in degrees
        "Run_Time": np.random.uniform(50, 200, rows),     # Run time in hours
        "Downtime_Flag": np.random.choice([0, 1], rows, p=[0.6, 0.4])  # 60% uptime, 40% downtime
    }
    df = pd.DataFrame(data)
    return df

df = generate_data()
df.to_csv("data.csv", index=False)
print("Synthetic data generated and saved")