programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
# Dictionaries are kept in {} braces with Key : Value pairs

# adding a value in a dictionary:

programming_dictionary["Loop"] = "The action of doing over and over again." # key valur pair at the end of the current dictionary.

# Usually we can start with an empty dictionary and then add Key:Value pairs to it.
# We can also wipe an existing dictionary by the same method.
empty_dictionary = {}


#Edit an item in the dictionary :
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

#Loop through in a dictionary:
# using a for loop when you run it in a dict, it will get only hold of the keys in the dictionary.
# To get the values, you will have to write the print statement again here for the values only.

for keys in programming_dictionary:
    print(keys)
    print(programming_dictionary[keys])