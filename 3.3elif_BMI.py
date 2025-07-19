print("This is a Simple BMI Calculator!!")
weight = int(input("What is your weight in KG's? "))
height = float(input("What is your height in meters? "))

bmi = weight / (height**2)

if bmi>=25:
    print("Overweight")
elif bmi>= 18.5:
    print("Normal Weight")
else:
    print("Underweight")
