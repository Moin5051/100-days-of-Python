print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Answer with either Left or Right in Each prompt.")


direction = input("Would you like to move Left or Right? ").lower()





if direction == "left":
    river = input("You have reached a River. Would you like to Wait or Swim? ").lower()

    if river == "wait":
        color = input("To reward your patience, You have been granted 3 doors, which one would you choose? Red, Blue, Yellow? ").lower()
        if color =="red":
            print("It is a room full of fire, you were burned. Game over")
        elif color == "blue":
            print("A hungry three headed beast is inside this room. You get eaten. Game Over")
        elif color == "yellow":
            print("You have found the treasure!!!! YAAAAYYY. You win")
        else:
            print("Wrong Selection Game over!!")
    else:
        print("There were croc in the river, You are dead. Game Over!!")


else:
    print("You fell in a hole!!!Game is over.")