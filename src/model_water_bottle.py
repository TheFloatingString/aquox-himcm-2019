# https://sciencing.com/carbon-footprint-plastic-bottle-12307187.html
# https://www.bottledwater.org/news/weight-pet-bottled-water-containers-has-decreased-326-over-past-eight-years

import math
import numpy as np
import random

def n_individuals_health_problems_from_bpa(n_population, coeff_problem=0.0001):
	return n_population*coeff_problem

class City:

	def __init__(self, population, temperature):
		self.temperature=temperature
		self.temperature_variation=0
		self.total_kg_co2_emitted=0
		self.per_day_kg_co2_emitted=0
		self.total_profit_made=0
		self.per_day_profit_made=0
		self.var_per_day_profit_made=0
		self.COEFF_CO2=0.0828
		self.population=population
		self.sick_people=0
		self.gdp_per_capita=100
		self.gdp_var_per_capita=0
		self.limit_coeff=1
		self.water_bottles_bought_per_day=self.compute_n_water_bottles_bought_per_day()
		self.total_water_bottles_bought=self.compute_n_water_bottles_bought_per_day()
		self.pollution = 0

	def pollution_per_water_bottle(self, mass_water_bottle=0.0127, fraction_polluted=1):
		self.pollution += self.water_bottles_bought_per_day*mass_water_bottle*fraction_polluted

	def set_limit_coeff(self, value):
		self.limit_coeff=value

	def kg_co2_per_water_bottle(self, n_water_bottles):
		return n_water_bottles*self.COEFF_CO2

	def compute_gdp_per_capita(self):
		gdp_per_capita = (self.gdp_per_capita)*(1.000062301904983)
		# gdp_per_capita=(self.population-self.sick_people)*(self.gdp_per_capita)/self.population*(1.000062301904983)
		gdp_per_capita+=(self.var_per_day_profit_made/self.population)
		if self.population < 0:
			gdp_per_capita = 0
		self.gdp_var_per_capita = gdp_per_capita-self.gdp_per_capita
		self.gdp_per_capita=gdp_per_capita

	def profit(self, n_water_bottles, profit_per_water_bottle=0.5):
		self.var_per_day_profit_made = n_water_bottles*profit_per_water_bottle - self.per_day_profit_made
		return n_water_bottles*profit_per_water_bottle

	def compute_sick_people(self):
		sick_people = 0
		# if self.water_bottles_bought_per_day > 0:
			# print(sick_people)
		sick_people += (self.water_bottles_bought_per_day/self.population)/10e4
		sick_people += self.population*(math.fabs((self.temperature-20)/2)/1000)
		# propagation of pathogens
		return sick_people

	def compute_population(self):
		self.population+=(self.population/35/365)*1.8
		self.population-=self.population*0.0084/365
		# print(self.population)
		self.population=self.population*(1+self.gdp_var_per_capita*0.001)*(1-(self.sick_people/self.population)*0.01)
		# print(self.sick_people)
		# print(self.population)

	def variation_based_on_temperature(self):
		return (1/40)*self.temperature+0.5

	def compute_n_water_bottles_bought_per_day(self):
		return self.population*self.variation_based_on_temperature()*self.limit_coeff

	def simulate_one_day(self):
		self.temperature += self.temperature_variation
		self.water_bottles_bought_per_day=self.compute_n_water_bottles_bought_per_day()
		self.per_day_kg_co2_emitted = self.kg_co2_per_water_bottle(self.water_bottles_bought_per_day)
		self.total_kg_co2_emitted += self.per_day_kg_co2_emitted
		self.per_day_profit_made = self.profit(self.water_bottles_bought_per_day)
		self.total_profit_made += self.per_day_profit_made
		self.sick_people = self.compute_sick_people()
		self.compute_temperature_variation()
		self.compute_gdp_per_capita()
		self.compute_population()
		self.total_water_bottles_bought += self.water_bottles_bought_per_day
		self.pollution_per_water_bottle()

	def compute_temperature_variation(self):
		self.temperature_variation += self.total_kg_co2_emitted*1.43e-22

	def output_variables(self):
		return_list = 	[self.per_day_kg_co2_emitted, 
						self.total_kg_co2_emitted, 
						self.per_day_profit_made, 
						self.total_profit_made,
						self.water_bottles_bought_per_day,
						self.population,
						self.temperature,
						self.gdp_per_capita,
						self.sick_people,
						self.total_profit_made,
						self.total_water_bottles_bought,
						self.pollution]
		return np.array(return_list)