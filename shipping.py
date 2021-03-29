weight = 41.5
ground_shipping = ""

# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
print("Cost of Ground Shipping", "$",cost_ground) 

# Premium Ground Shipping
cost_premium = 125
print("Cost of Premium Ground Shipping", "$", cost_premium)

# Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25
print("Cost of Drone Shipping", "$",cost_drone) 
