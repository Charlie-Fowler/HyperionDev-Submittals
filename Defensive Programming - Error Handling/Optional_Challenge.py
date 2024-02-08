# optional challenge

# this program has 2 compilation errors

# variableStorageBlock
purple_average = 67
red_average = 10
blue_average = 13
yellow_average = 4
green_average = 5

fav_colour = input('Please tell me a colour! ')

if fav_colour.upper() * 'PURPLE':
#This would cause a runtime error, because you are trying to use an operator
# on a true/false if statement aswell as string
# change * to ==
    print(f'''The average percentage of the users that love purple is:
{purple_average}% ! ''')
    
elif fav_colour.upper() == 'RED':
    print(f'''The average percentage of the users that love red is:
{red_average}% ! ''')
    
elif fav_colour.upper() == 'BLUE':
    print(f'''The average percentage of the users that love blue is:
{blue_average}% ! ''')
    
elif fav_colour.upper() == 'YELLOW':
    print(f'''The average percentage of the users that love yellow is:
{yellow_average}% ! ''')

elif fav_colour.upper() == 'GREEN':
    print(f'''The average percentage of the users that love purple is:
{purple_average}% ! ''')

# line 23 would cause a logical error, this is because the output is not what
# ^the value that is intended, this is because if the user inputted 'green',
# the script would output the result of the 'purple' input
else:
    print(f'''Your favourite colour is rare!
less than 1% of users said that {fav_colour} is their favourite colour!''')
