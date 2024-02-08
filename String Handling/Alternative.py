'''
ask user to input string
turn each alternative character turns upper case and each other character turns lower case
output print

turn each alternative word into uppercase then upper case
output print
'''
# request input from user
user_sentence = input('Please enter a sentence:')
# retrieve lenght of string
size = len(user_sentence)
# create empty variable
user_output = ''
# amend each character character for each index
for i in range(size):
    # if even, upper. if odd, lower
    if i % 2 == 0:
        # add to string
        user_output += user_sentence[i].upper()
    else:
        user_output += user_sentence[i].lower()
# output
print(user_output)

# request user input for sentence
user_sentence = input('Please enter another sentence:')
# seperate the string
word_convert = user_sentence.split()
# length of list
size = len(word_convert)

# amend each character character for each index
for i in range(size):
# if i == odd, upper
    if i % 2 == 1:
        word_convert[i] = word_convert[i].upper()
# else i != even, lower case
    else:
        word_convert[i] = word_convert[i].lower()
# join list seperated with space
word_convert = ' '.join(word_convert)
# output
print(word_convert)
