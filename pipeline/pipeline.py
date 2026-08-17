import sys
import pandas as pd 
print("arguments:", sys.argv)

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

day = int(sys.argv[1])
print(f"Running pipeline for day {day}")

print(df.head())
df.to_parquet(f"output_day_{day}.parquet")