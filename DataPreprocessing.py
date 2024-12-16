import pandas as pd
from datetime import datetime
import numpy as np
from scipy import stats

df = pd.read_csv('Data\sampled_file.csv')


df = df.drop(columns=['merch_zipcode'])
df = df.drop(columns=['first'])
df = df.drop(columns=['last'])
df = df.drop(columns=['street'])
df = df.drop(columns=['zip'])
df = df.drop(columns=['lat'])
df = df.drop(columns=['long'])
df = df.drop(columns=['merch_lat'])
df = df.drop(columns=['merch_long'])
df = df.drop(columns=['trans_num'])
df = df.drop(columns=['cc_num'])


def calculate_age(dob):
    dob = datetime.strptime(dob, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age
df['age'] = df['dob'].apply(calculate_age)
df = df.drop(columns=['dob'])

numerical_features = ['amt', 'city_pop', 'age']

z_scores = np.abs(stats.zscore(df[numerical_features]))
outliers = (z_scores > 3).any(axis=1)
df_cleaned = df[~outliers]

df.to_csv('preprocessed_dataset.csv', index=False)