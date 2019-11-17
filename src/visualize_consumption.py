import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/data_bottles.csv", delimiter=",")
print(df.values.shape)

def convert_gallons_to_liters(gallons):
	return gallons*3.78541

def total_consumtion(consumption, population, bottle_quantity=0.5, carbon_per_bottle=0.0828):
	carbon = ((consumption*population)/bottle_quantity)*carbon_per_bottle
	return carbon

consumption_list = list()
for index, row in df.iterrows():
	print(row["per capita water consumption gallons"])
	print(row["population(1000)"])
	consumption_list.append(
		total_consumtion(
			convert_gallons_to_liters(
				row["per capita water consumption gallons"]
				),
			row["population(1000)"]*1000
			)
		)

print(consumption_list)
print(df["year"].values)

plt.scatter(list(map(int, df["year"].values)), consumption_list)
plt.xticks(df["year"].values, rotation=80)
plt.xlabel("Year")
plt.ylabel("Carbon emitted per year (kg)")
plt.ylim(0,)
plt.title("Carbon Emitted in the US due to Water Bottle Usage")
plt.savefig("img/consumption.png")