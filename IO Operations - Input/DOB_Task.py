''' Open .txt in read only
    interate through each line of the .txt and return particular sets of data
    print data through sub categorys such as DOB and Name
'''

name = []
dob = []
# lists to store data chunks

file = open(r'DOB.txt', 'r', encoding='utf-8')
# open file
personal_details = file.readlines()
# convert file into str.variable

for row in personal_details:
    # read each line in the variable
    data_chunk = row.split()
    # break up variable to retrieve particular data
    name.append(data_chunk[:2])
    # retrieve first 2 index's and store together
    dob.append(data_chunk[2:])
    # retrieve following information after index 2
    # then store together

print("\n\033[1mName\033[0m") # print header of 'name' in BOLD
for i in name:
    print(f"{' '.join(i)}")
# iterate through the list and join them per iteration for comprehension

print("\n\033[1mBirthday\033[0m") # print header of 'birthday' in BOLD
for i in dob:
    print(f"{' '.join(i)}")
# iterate through the list and join them per iteration for comprehension.
