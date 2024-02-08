#while.py
'''START
Request user input a number
while number is not -1
    store number
    repeat input
when number is -1
    end loop
    sum all inputs excluding -1 value / amount of inputs
    print average
'''

number = int(input('Please enter a number: '))
input_list = [] #Variable Storage

while number != -1: #while number is not -1 loop
    input_list.append(number) #add number onto variable list storage
    number = int(input('Please enter another number: '))

if number == -1: #Action when while condition is false
    total_inputs = len(input_list)
    average = sum(input_list) / total_inputs
    print(f'''Your inputted numbers were {input_list}.
    The average of your inputted numbers is {int(average)}''')
