import pandas as pd


total_lines = sum(1 for line in open('credit_card_transactions.csv')) - 1
sample_size = 15000
interval = total_lines // sample_size

df = pd.read_csv('credit_card_transactions.csv', skiprows=lambda x: x % interval != 0)
df = df.iloc[:, 1:]
df.insert(0, 'line_number', range(1, len(df) + 1))

df.to_csv('sampled_file.csv', index=False)

