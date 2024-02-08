# This example program is meant to demonstrate errors

print("Welcome to the error program") 
# syntax Error No Parentheses
print("\n") 
# syntax error no parenthesis, incorrect indentation

# variables declaring the user's age, casting the str to an int,
# ^and printing result
age_Str = "24"
 # syntax error incorrect indentation #runtime error incorrect value to cast,
 # remove 'years old' #Runtime error, incorrect use of operator change == to =
age = int(age_Str) 
# syntax error incorrect indentation
print("I'm " + str(age) + " years old.") 
# syntax error incorrect indentation 
# ^runtime error, no casting on age in print function, add str()

# Variables declaring additional years and printing the total years of age
years_from_now = 3 
# syntax error incorrect indentation #Runtime error, Remove "" needs to be int
total_years = age + years_from_now
# syntax error incorrect indentation

print("The total number of years:" + str(total_years)) 
# logical, incorrect use of quotations, remove "" 
# runtime error, amend answer_years to total_years 
# syntax error, no parentheses for print function
# ^runtime error, no casting on total_years in print function, add str()

# variable to calc the total amount of months from the total amount of years
total_months = (total_years * 12) + 6 
# logical Error - 6 months to be added 
# runtime error, amend total to total_years
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") 
# syntax error, no parentheses for print function 
# runtime error, no casting on total_months in print function, add str()
