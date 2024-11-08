# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ["banana","orange","apple","avocade"]
# TODO: Add a fruit to the end of the list
fruits.append("mango")

# TODO: Insert a fruit at the beginning of the list
fruits.insert(0,"strawberry")
# TODO: Remove a fruit from the list
fruits.remove("apple")
# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1,2,3,4,5]
# TODO: Create a new list with each number squared
squared_numbers = [1*1,2*2,3*3,4*4,5*5]
# TODO: Find the sum and average of the original numbers
sum = 1+2+3+4+5
average = sum/ 5
# TODO: Print the results
print(average)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries = {"Mozanmbique":"Maputo","Zimbabwe":"Harare","China":"Beijing"}
# TODO: Add a new country-capital pair
countries["Kenya"] = "Nairobi"
# TODO: Update the capital of an existing country
countries.update({"Mozambique":"Maputo","Zambia":"Lusaka"})
# TODO: Remove a country-capital pair
countries.pop("Zimbabwe")
# TODO: Print the modified dictionary
print(countries)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {"mango":"orange","avocado":"green","strawberry":"red","banana":"yellow"}
# TODO: Print all the fruits (keys)
b = fruit_colors.keys()
print(b)
# TODO: Print all the colors (values)
x = fruit_colors.values()
print(x)

# TODO: Print each fruit and its color
for fruit,colors in fruit_colors.items():
    print(fruit,colors)

# TODO: Check if a fruit is in the dictionary and print its color
print("mango" in fruit_colors, "orange")
print("avocado" in fruit_colors, "green")
print("strawberry" in fruit_colors, "red")
print("banana" in fruit_colors, "yellow")