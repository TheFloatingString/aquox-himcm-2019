from src.model_water_bottle import City

import matplotlib.pyplot as plt
import numpy as np

city = City(population=1000000,
	temperature=20)
city.gdp_per_capita=100

all_results = []
all_results.append(city.output_variables())

number_of_days=10000

for i in range(number_of_days):
	city.simulate_one_day()
	all_results.append(city.output_variables())
	# print(city.output_variables())

all_results = np.array(all_results)

print(all_results.shape)

plt.scatter(range(number_of_days+1),all_results[:,1],s=1)
plt.title("CO2 produced")
plt.xlabel("Days elapsed")
plt.ylabel("CO2 (kg)")
plt.savefig("img/co2_produced.png")
plt.close()

plt.scatter(range(number_of_days+1),all_results[:,4],s=1)
plt.title("CO2 Water bottles bought")
plt.xlabel("Days elapsed")
plt.ylabel("Plastic ater bottles sold")
plt.savefig("img/water_bottles_bought.png")
plt.close()

plt.scatter(range(number_of_days+1),all_results[:,6],s=1)
plt.title("Temperature")
plt.xlabel("Days elapsed")
plt.ylabel("Temperature (C)")
plt.savefig("img/temperature.png")
plt.close()

plt.scatter(range(number_of_days+1),all_results[:,7],s=1)
plt.title("GDP per Capita")
plt.xlabel("Days elapsed")
plt.ylabel("GDP per capita")
plt.savefig("img/gdp_per_capita.png")
plt.close()

plt.scatter(range(number_of_days+1),all_results[:,5],s=1)
plt.scatter(range(number_of_days+1),all_results[:,8],s=1)
plt.title("Population")
plt.xlabel("Days elapsed")
plt.ylabel("Number of people")
plt.savefig("img/sick_people.png")
plt.close()

plt.scatter(range(number_of_days+1),all_results[:,9],s=1)
plt.title("Profit Made")
plt.xlabel("Days elapsed")
plt.ylabel("Profit ($) per day")
plt.savefig("img/per_day_profit_made.png")
plt.close()

plt.scatter(range(number_of_days+1),all_results[:,8],s=1)
plt.title("Sick People")
plt.xlabel("Days elapsed")
plt.ylabel("Number of people")
plt.savefig("img/sick_people.png")
plt.close()
