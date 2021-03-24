# Descriptions

lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""

# Prices

lovely_loveseat_price = 254.00
stylish_settee_price = 180.50
luxurious_lamp_price = 52.15

#Tax

sales_tax = .088

# Customer 1
# Customer 1 total
customer_one_total = 0
#Customer one Itemization
customer_one_itemization = ""
customer_one_total += lovely_loveseat_price
print("Customer One Items")
print(lovely_loveseat_price, lovely_loveseat_description) 
customer_one_total += luxurious_lamp_price
print(luxurious_lamp_price, luxurious_lamp_description) 

# Customer one Tax
customer_one_tax = customer_one_total * sales_tax
print("Sales Tax", customer_one_tax)
#running total
print("Total", customer_one_total) 
