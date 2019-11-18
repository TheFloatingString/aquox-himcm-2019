from src.model_water_bottle import City

import matplotlib.pyplot as plt
import numpy as np

simulation_data = list()

simulation_data.append({"name": "Concord", "population": 17668, "temperature": 14.9, "number_of_days_before":365*3, "number_of_days_after":365*3})
simulation_data.append({"name": "Concord", "population": 17668, "temperature": 14.9, "number_of_days_before":365*6, "number_of_days_after":0})
simulation_data.append({"name": "San Francisco", "population": 816294, "temperature": 17.7, "number_of_days_before":365*3, "number_of_days_after":365*3})
simulation_data.append({"name": "San Francisco", "population": 816294, "temperature": 17.7, "number_of_days_before":365*6, "number_of_days_after":0})

all_data = []

for row in simulation_data:

	city = City(population=row["population"],
		temperature=row["temperature"])
	city.gdp_per_capita=59531/365

	all_results = []
	all_results.append(city.output_variables())

	number_of_days_before=row["number_of_days_before"]
	number_of_days_after=row["number_of_days_after"]


	for i in range(number_of_days_before):
		city.simulate_one_day()
		all_results.append(np.array(city.output_variables()))

	city.set_limit_coeff(0.0001)

	for i in range(number_of_days_after):
		city.simulate_one_day()
		all_results.append(np.array(city.output_variables()))

	all_results = np.array(all_results)

	all_data.append(all_results)
	# all_data.append(all_results[-1])

	print(all_results.shape)

	number_of_days = number_of_days_before + number_of_days_after

	# plt.plot(range(number_of_days+1),all_results[:,0])
	# plt.title("Concord: CO2 produced")
	# plt.xlabel("Days elapsed")
	# plt.ylabel("CO2 (kg)")
	# plt.legend()
# plt.savefig("img/concord_co2_produced.png")
	# plt.close()

	# plt.plot(range(number_of_days+1),all_results[:,4])
	# plt.title("Concord: Water bottles bought")
	# plt.xlabel("Days elapsed")
	# plt.ylabel("Plastic water bottles sold")
	# plt.legend()
# plt.savefig("img/concord_water_bottles_bought.png")
	# plt.close()

	# plt.plot(range(number_of_days+1),all_results[:,6])
	# plt.title("Concord: Temperature")
	# plt.xlabel("Days elapsed")
	# plt.ylabel("Temperature (C)")
	# plt.legend()
# plt.savefig("img/concord_temperature.png")
	# plt.close()

	# plt.plot(range(number_of_days+1),all_results[:,7])
	# plt.title("Concord: GDP per Capita")
	# plt.xlabel("Days elapsed")
	# plt.ylabel("GDP per capita")
	# plt.legend()
# plt.savefig("img/concord_gdp_per_capita.png")
	# plt.close()

	# plt.plot(range(number_of_days+1),all_results[:,5])
	# plt.title("Concord: Population")
	# plt.xlabel("Days elapsed")
	# plt.ylabel("Number of people")
	# plt.legend()
	# plt.savefig("img/concord_population.png")
	# plt.close()

	# plt.plot(range(number_of_days+1),all_results[:,9])
	# plt.title("Concord: Profit Made")
	# plt.xlabel("Days elapsed")
	# plt.ylabel("Profit ($) per day")
	# plt.legend()
# plt.savefig("img/concord_per_day_profit_made.png")
	# plt.close()

	# plt.plot(range(number_of_days+1),all_results[:,8])
	# plt.title("Concord: Sick People")
	# plt.xlabel("Days elapsed")
	# plt.ylabel("Number of people")
	# plt.legend()
# plt.savefig("img/concord_sick_people.png")
	# plt.close()

	# input("Continue? (PRESS ENTER) ")
#
# all_data = np.array(all_data)
# 
# print(all_data.shape)
# print(all_data.reshape(4,12,2191))

# print(len(all_data))
# print(all_data[1].shape)
# print(len(all_data[0]))

# plt.plot(all_data[0][0])
# plt.show()

plt.plot(range(number_of_days+1),all_data[0][:,0], alpha=0.4, c="blue", label="With ban (+1095 days)")
plt.plot(range(number_of_days+1),all_data[1][:,0], alpha=0.4, c="red", label="No ban")
plt.title("Concord: CO2 produced")
plt.xlabel("Days elapsed")
plt.ylabel("CO2 (kg)")
plt.legend()
plt.savefig("img/concord_co2_produced.png")
plt.close()

plt.plot(range(number_of_days+1),all_data[0][:,4], alpha=0.4, c="blue", label="With ban (+1095 days)")
plt.plot(range(number_of_days+1),all_data[1][:,4], alpha=0.4, c="red", label="No ban")
plt.title("Concord: Water bottles bought")
plt.xlabel("Days elapsed")
plt.ylabel("Plastic water bottles sold")
plt.legend()
plt.savefig("img/concord_water_bottles_bought.png")
plt.close()

plt.plot(range(number_of_days+1),all_data[0][:,6], alpha=0.4, c="blue", label="With ban (+1095 days)")
plt.plot(range(number_of_days+1),all_data[1][:,6], alpha=0.4, c="red", label="No ban")
plt.title("Concord: Temperature")
plt.xlabel("Days elapsed")
plt.ylabel("Temperature (C)")
plt.legend()
plt.savefig("img/concord_temperature.png")
plt.close()

plt.plot(range(number_of_days+1),all_data[0][:,7], alpha=0.4, c="blue", label="With ban (+1095 days)")
plt.plot(range(number_of_days+1),all_data[1][:,7], alpha=0.4, c="red", label="No ban")
plt.title("Concord: GDP per Capita")
plt.xlabel("Days elapsed")
plt.ylabel("GDP per capita")
plt.legend()
plt.savefig("img/concord_gdp_per_capita.png")
plt.close()

plt.plot(range(number_of_days+1),all_data[0][:,5], alpha=0.4, c="blue", label="With ban (+1095 days)")
plt.plot(range(number_of_days+1),all_data[1][:,5], alpha=0.4, c="red", label="No ban")
plt.title("Concord: Population")
plt.xlabel("Days elapsed")
plt.ylabel("Number of people")
plt.legend()
plt.savefig("img/concord_population.png")
plt.close()

plt.plot(range(number_of_days+1),all_data[0][:,9], alpha=0.4, c="blue", label="With ban (+1095 days)")
plt.plot(range(number_of_days+1),all_data[1][:,9], alpha=0.4, c="red", label="No ban")
plt.title("Concord: Profit Made")
plt.xlabel("Days elapsed")
plt.ylabel("Total profit ($)")
plt.legend()
plt.savefig("img/concord_per_day_profit_made.png")
plt.close()

plt.plot(range(number_of_days+1),all_data[0][:,8], alpha=0.4, c="blue", label="With ban (+1095 days)")
plt.plot(range(number_of_days+1),all_data[1][:,8], alpha=0.4, c="red", label="No ban")
plt.title("Concord: Sick People")
plt.xlabel("Days elapsed")
plt.ylabel("Number of people")
plt.legend()
plt.savefig("img/concord_sick_people.png")
plt.close()



plt.plot(range(number_of_days+1),all_data[2][:,0], alpha=0.4, c="blue", label="With ban (+1095 days)")
plt.plot(range(number_of_days+1),all_data[3][:,0], alpha=0.4, c="red", label="No ban")
plt.title("San Francisco: CO2 produced")
plt.xlabel("Days elapsed")
plt.ylabel("CO2 (kg)")
plt.legend()
plt.savefig("img/sf_co2_produced.png")
plt.close()

plt.plot(range(number_of_days+1),all_data[2][:,4], alpha=0.4, c="blue", label="With ban (+1095 days)")
plt.plot(range(number_of_days+1),all_data[3][:,4], alpha=0.4, c="red", label="No ban")
plt.title("San Francisco: Water bottles bought")
plt.xlabel("Days elapsed")
plt.ylabel("Plastic water bottles sold")
plt.legend()
plt.savefig("img/sf_water_bottles_bought.png")
plt.close()

plt.plot(range(number_of_days+1),all_data[2][:,6], alpha=0.4, c="blue", label="With ban (+1095 days)")
plt.plot(range(number_of_days+1),all_data[3][:,6], alpha=0.4, c="red", label="No ban")
plt.title("San Francisco: Temperature")
plt.xlabel("Days elapsed")
plt.ylabel("Temperature (C)")
plt.legend()
plt.savefig("img/sf_temperature.png")
plt.close()

plt.plot(range(number_of_days+1),all_data[2][:,7], alpha=0.4, c="blue", label="With ban (+1095 days)")
plt.plot(range(number_of_days+1),all_data[3][:,7], alpha=0.4, c="red", label="No ban")
plt.title("San Francisco: GDP per Capita")
plt.xlabel("Days elapsed")
plt.ylabel("GDP per capita")
plt.legend()
plt.savefig("img/sf_gdp_per_capita.png")
plt.close()

plt.plot(range(number_of_days+1),all_data[2][:,5], alpha=0.4, c="blue", label="With ban (+1095 days)")
plt.plot(range(number_of_days+1),all_data[3][:,5], alpha=0.4, c="red", label="No ban")
plt.title("San Francisco: Population")
plt.xlabel("Days elapsed")
plt.ylabel("Number of people")
plt.legend()
plt.savefig("img/sf_population.png")
plt.close()

plt.plot(range(number_of_days+1),all_data[2][:,9], alpha=0.4, c="blue", label="With ban (+1095 days)")
plt.plot(range(number_of_days+1),all_data[3][:,9], alpha=0.4, c="red", label="No ban")
plt.title("San Francisco: Profit Made")
plt.xlabel("Days elapsed")
plt.ylabel("Total profit ($)")
plt.legend()
plt.savefig("img/sf_per_day_profit_made.png")
plt.close()

plt.plot(range(number_of_days+1),all_data[2][:,8], alpha=0.4, c="blue", label="With ban (+1095 days)")
plt.plot(range(number_of_days+1),all_data[3][:,8], alpha=0.4, c="red", label="No ban")
plt.title("San Francisco: Sick People")
plt.xlabel("Days elapsed")
plt.ylabel("Number of people")
plt.legend()
plt.savefig("img/sf_sick_people.png")
plt.close()