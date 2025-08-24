age = int(input("What is your current age? "))

def life_in_weeks(age):
    total_life = 90*52
    current_life = age*52
    life_left = total_life - current_life

    print(f"You have {life_left} weeks left to live. Assuming your life is 90 Years")

life_in_weeks(age)