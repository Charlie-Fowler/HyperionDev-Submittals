# create a programme with a runtime error

print('Welcome to the doggy age calculator!\n')

dog_humanyrs = int(input('Please enter your dogs age in human years as a number:'))
# the runtime error will occur here, this is because if the user inputs a
# non integer, it will crash because of the pre-casting.
# this can be resolved by defensive programming

if type(dog_humanyrs) == int:
    dog_age = dog_humanyrs * 7
    print(f'\nYour dog is actually {dog_age} doggy years old!')

else:
    print('You have not entered a valid number!')

'''
HOW TO REPAIR
print('Welcome to the doggy age calculator!')
while True:
    try:
        dog_humanyrs=int(input('Please enter your dogs age in years as a number: '))
        dog_age = dog_humanyrs * 7
        print(f'Your dogs is actually {dog_age} doggy years old!')
        break
        
    except ValueError:
        print('\nYou have not entered a number! Please restart!')
