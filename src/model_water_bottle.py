# https://sciencing.com/carbon-footprint-plastic-bottle-12307187.html
# https://www.bottledwater.org/news/weight-pet-bottled-water-containers-has-decreased-326-over-past-eight-years

import math
import numpy as np
import random

def profit(n_water_bottles, profit_per_water_bottle=0.50):
	return n_water_bottles*profit_per_water_bottle

def pollution_per_water_bottle(n_water_bottles, mass_water_bottle=0.0127, fraction_polluted=0.3):
	return n_water_bottles*mass_water_bottle*fraction_polluted

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
		self.water_bottles_bought_per_day=self.compute_n_water_bottles_bought_per_day()
		self.gdp_per_capita=100
		self.gdp_var_per_capita=0

	def kg_co2_per_water_bottle(self, n_water_bottles):
		return n_water_bottles*self.COEFF_CO2

	def compute_gdp_per_capita(self):
		gdp_per_capita=(self.population-self.sick_people)*(self.gdp_per_capita)/self.population*(1+.03/365)
		# print(self.sick_people)
		# print(gdp_per_capita)
		# print(self.per_day_profit_made)
		# print(self.per_day_profit_made/self.population)
		# print(self.var_per_day_profit_made/self.population)
		# print()
		gdp_per_capita+=(self.var_per_day_profit_made/self.population)
		self.gdp_var_per_capita = gdp_per_capita-self.gdp_per_capita
		self.gdp_per_capita=gdp_per_capita

	def profit(self, n_water_bottles, profit_per_water_bottle=0.5):
		self.gdp_var_per_capita = n_water_bottles*profit_per_water_bottle - self.per_day_profit_made
		return n_water_bottles*profit_per_water_bottle

	def compute_sick_people(self):
		sick_people = (self.population/self.water_bottles_bought_per_day)*self.population/10e4
		# print(f"population: {self.population}")
		# print(sick_people)
		sick_people += self.population*(math.fabs((self.temperature-20)/2)/1000)
		# print(sick_people)
		# print()
		return sick_people

	def compute_population(self):
		# print(self.population)
		# print(self.sick_people)
		self.population+=(self.population/25/365)*2.1
		# print(self.gdp_per_capita)
		# print(self.gdp_var_per_capita)
		self.population=self.population*(1+self.gdp_var_per_capita*0.0001)*(1-(self.sick_people/self.population)*0.01)

	def variation_based_on_temperature(self):
		return (1/40)*self.temperature+1

	def compute_n_water_bottles_bought_per_day(self):
		return self.population*self.variation_based_on_temperature()*1

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

	def compute_temperature_variation(self):
		self.temperature_variation += self.total_kg_co2_emitted*10e-18

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
						self.per_day_profit_made]
		return np.array(return_list)