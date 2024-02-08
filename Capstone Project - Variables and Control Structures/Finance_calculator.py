#FINANCE_CALCULATORS

'''START
User enters required calculator: investment or bond
the choice submitted by user dictates the calculation
IF investment is selected, ask user to input:
    amount, interest rate, duration (years) and choose simple or compound.
    after input, print answer based on calculation
    END
IF bond is selected, ask user to input:
    Value of house, interest rate and the number of months they plan to take to repay.
    print calculated repayments
    END
    !IF NO CORRECT VALUE IF ENTERED E.G INVESTMENT OR BOND. PRINT MESSAGE AND STOP!
'''
import math

#START
print('''Hi there! 
Welcome to the finance calculator, please follow the steps below to calculate your investment or bond:

      Investment - To calculate the amount of interest you'll earn on your investment.
      Bond - To calculate the amount you'll have to pay on a home loan.
''')

calculator_decision = input("Enter either 'Investment' or 'Bond' from the menu above to proceed: ") #ASK USER TO CHOOSE CALCULATORS
print(f'You have selected the {calculator_decision}:') 

if calculator_decision.upper() == 'INVESTMENT': #PROCEED WITH FOLLOWING CALCULATIONS IF INVESTMENT, USER PROMPTED FOR FOLLOWING INFORMATION REQUIRED
    monies = int(input("Please enter the amount you wish to deposit: "))
    interest_rate = float(input("Please enter an interest rate: "))
    invest_duration = int(input(f"How many years would you like to invest £{monies} for? "))
    interest = input("Please choose if you would like to work out the 'simple' or 'compound' interest: ") #INFO REQUIRED NEEDING INPUTTING//CHOOSE INTEREST TYPE
    print(f'Thank you, you have chosen {interest} interest.')

    if interest.upper() == 'SIMPLE': #SIMPLE INTEREST CALCULATION
        simple_result = monies * (1 + (interest_rate / 100) * invest_duration)
        profit = simple_result - monies #COMPARABLE FIGURE, HIGHLIGHTS GAINS, DISPLAY FIGURE AFTER INVESTMENT AND THE GAINS ON CAPITAL
        print(f'In {invest_duration} years, you will have £{int(simple_result)}! This is a gain of £{int(profit)} on your initial investment with simple interest!')

    elif interest.upper() == 'COMPOUND': #COMPOUND INTEREST CALCULATION
        compound_result = monies * math.pow((1 + (interest_rate / 100)),invest_duration)
        profit = compound_result - monies #COMPARABLE FIGURE, HIGHLIGHTS GAINS, DISPLAY FIGURE AFTER INVESTMENT AND THE GAINS ON CAPITAL
        print(f'In {invest_duration} years, you will have £{int(compound_result)}! This is a gain of £{int(profit)} on your initial investment with simple interest!')

    else:
        print("ERROR! Invalid input, please start again! ") #IF NEITHER COMPOUND OR SIMPLE IS INPUTTED

elif calculator_decision.upper() == 'BOND': #PROCEED WITH FOLLOWING CALCULATIONS IF BOND, USER PROMPTED FOR FOLLOWING INFORMATION REQUIRED
    home_value = int(input('Please enter the current value of your home: '))
    interest = float(input('Please enter your interest rate: '))
    duration = int(input("How many months do you plan to repay the bond? "))
    repayment_result = ((interest / 100) * home_value) / (1 - (1 + (interest / 100)) ** (-duration)) #HOME BOND CALCULATION
    print(f'You will have to pay {int(repayment_result)} in order to pay your bond in time!') #GIVES USER INFORMATION BASED ON THEIR INPUTS.

else:
    print("ERROR! Invalid input, please start again! ")

#END
