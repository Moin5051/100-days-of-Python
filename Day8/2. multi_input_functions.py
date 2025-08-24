# Functions with input

def greet_with_name(name, food):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"I see that your favorite food is {food}")


greet_with_name("Jack Bauer","Apple")
greet_with_name(food="Cheesecake" , name="Makaveli") 

# Usually the inputs need to be in the same order at the time of calling as they are when declaring. 
# However, if you are using positional arguments basically specifying the name of the parameter and argument, you can use any order you want to 