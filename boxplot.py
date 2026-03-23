

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/python program's/Study_Pandas/bike_sales_india.csv")
df = pd.DataFrame(data)

plt.boxplot(df["Resale Price (INR)"])
plt.show()









