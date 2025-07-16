print("Welcome to the Simple Tip Calculator!!")
bill = float(input("What is the total bill amount? $"))
tip = int(input("What is the tip percenatge you would like to give? Choose from: 10 12 15 20. *Only input numbers:  "))
people = int(input("How many people are splitting this bill? "))

final_tip = (tip/100)+1
result= round((bill/people)*final_tip,2)
print(f"Each person needs to pay: ${result}")