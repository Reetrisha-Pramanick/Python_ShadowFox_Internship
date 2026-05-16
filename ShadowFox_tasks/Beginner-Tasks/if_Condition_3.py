India = ["Mumbai", "Chennai", "Hydrabad", "Bangalore", "Delhi", "Kolkata"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
city1 = input("Enter your 1st city: ").title()
city2 = input("Enter your 2nd city: ").title()
if city1 in India and city2 in India:
    print("Both cities are in India")
elif city1 in UAE and city2 in UAE:
    print("Both cities are UAE")
elif city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")
else:
    print("They dont belong to the same country")