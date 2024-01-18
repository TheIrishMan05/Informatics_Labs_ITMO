import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Лаба5 - доп2.csv")
df.head()
fig, ax = plt.subplots(figsize=(12, 8))
df.groupby(['<DATE>'.replace(",", '')]).boxplot(column=["<OPEN>", "<HIGH>", "<LOW>", "<CLOSE>"], ax=ax, color="purple")
plt.show()