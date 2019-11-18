class Airport:

	def __init__(self, deplaned_passengers_per_day):
		self.deplaned_passengers_per_day = deplaned_passengers_per_day
		self.passengers_with_buyer_power_to_change = 0.05
		self.passengers_who_change_airport = 0.001
		self.profit_per_passenger = 17
		self.deplaned_passengers_after_ban = self.deplaned_passengers_per_day*(1-0.05*0.001)
		self.profits_made=0

	def compute_profits_made(self):
		self.profits_made += self.deplaned_passengers_per_day*self.profit_per_passenger

	def compute_profits_made_after_ban(self):
		self.profits_made += self.deplaned_passengers_after_ban*self.profit_per_passenger
