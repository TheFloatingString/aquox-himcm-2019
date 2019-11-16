import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/obesity_in_concord.csv", delimiter=',')
print(df.values)
plt.scatter(df.values[:,0], df.values[:,1])
# plt.plot([2013,0],[2013,100])


plt.title("Obesity Rates in Concord among Adults")
plt.xlabel("Year")
plt.ylabel("% adults")

plt.savefig("img/obesity_in_concord.png")