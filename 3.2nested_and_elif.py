print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age<=12:
        print("You need to pay 5$")
    elif 12<age<18:
        print("Please pay 8$")
    else:
        print("Your ticket price is 15$")
else:
    print("Sorry you have to grow taller before you can ride.")
