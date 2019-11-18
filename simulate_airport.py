from src.model_airport import Airport 

airport = Airport(deplaned_passengers_per_day=57793313/365)
for i in range(365):
	airport.compute_profits_made()
print(airport.profits_made)

airport = Airport(deplaned_passengers_per_day=57793313/365)
for i in range(365):
	airport.compute_profits_made_after_ban()
print(airport.profits_made)