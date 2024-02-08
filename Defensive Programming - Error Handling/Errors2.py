# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program,
# ^look at the error messages, and find and fix the errors.

animal = "Lion" 
# syntax error no quotations on string "Lion"
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal} {animal_type}. It has {number_of_teeth} teeth" 
# syntax error, no format for f-string type
# logical error, incorrect print output
# amend'This is a {animal}. It is a {number_of_teeth} and it has {animal_type}
# teeth' to 'This is a {animal} {animal_type}. It has {number_of_teeth} teeth'

print(full_spec)
 #syntax error, no parentheses with print function
