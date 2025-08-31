#Instead of a String value assigned to a key, we can replace it with a List. IT can also be a dict inside a dict

# You can nest a List in a Dictionary like this:

#my_dictionary = {
    #key1: [List],
    #key2: Value,}



travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
#Printing the value in the list inside a dict.
print(travel_log["France"][1])


#nesting:
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

#Print Stuttgart from Travel_log:

print(travel_log["Germany"]["cities_visited"][2])