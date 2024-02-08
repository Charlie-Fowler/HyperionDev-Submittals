#request name,age, house number and streetname from user
#print all the input out

userName = str(input("What is your first and last name? "))
userAge = int(input("What is your age? "))
userHouseNum = int(input("What is your house number? "))
userStName = str(input("What is your street name? "))

print("This is {}. They are {} years old and lives at {} {}".format(userName,userAge,userHouseNum,userStName))
