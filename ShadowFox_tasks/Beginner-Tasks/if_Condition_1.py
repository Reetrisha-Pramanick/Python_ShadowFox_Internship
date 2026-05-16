height = float(input("enter the height in meters: "))
weight = float(input("enter the weight in kilograms: "))
BMI = weight/(height*height)
if BMI >= 30:
    print("Obesity")
elif BMI >= 25:
    print("Overweight")
elif BMI >= 18.5:
    print("Normal")
else:
    print("Underweight")