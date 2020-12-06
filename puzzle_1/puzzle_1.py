import numpy as np
import pandas as pd

df = pd.read_csv('./input.csv')
df = df.iloc[:,0].tolist()
print(df)

for i in range(len(df)):
	for j in range(i+1, len(df)):
		if df[i] + df[j] == 2020:
			print("prod:", df[i] * df[j])
			print("sum:", df[i] + df[j])
			break

# part 2
for i in range(len(df)):
	for j in range(i+1, len(df)):
		for k in range(j+1, len(df)):
			if df[i] + df[j] + df[k] == 2020:
				print("prod2:", df[i] * df[j] * df[k])
				print("sum2:", df[i] + df[j] + df[k])
				break
