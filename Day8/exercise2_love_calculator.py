print("Welcome to a Basic yet inaccurate Love Calculator. This calculator wont deifne your actual love life. Let's continue!! ")
nameA = input("What is your name? ")
nameB = input("What is the name of your Significant other?")
def calculate_love(nameA,nameBM):
   
   combined = (nameA + nameB).lower()
   True_score = 0
   Love_score = 0

   for letters in "true":
      True_score += combined.count(letters)
   for letter in "love":
      Love_score += combined.count(letter)
  
   final_score = int(str(True_score)+str(Love_score))

   print(f"Your Love score based on an absurd logic is: {final_score}")

calculate_love(nameA,nameB)

    
