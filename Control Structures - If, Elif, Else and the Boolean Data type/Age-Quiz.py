#age-quiz.py
#User inputs age
#if user under 13 print "You qualify to kiddie discount"
#else if user is 21 print "Congrats on your 21st!"
#else if User is or over 40 print "You're over the hill"
#else if is or over 65 print "Enjoy your retirement!"
#else if over 100 print "Sorry, Youre dead"
#else if any other age print "age is but a number"

age = int(input("What is your age? "))

if age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
elif age > 100:
    print("Sorry, you're dead.")
elif age >= 60:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
else:
    print("Age is but a number.")
