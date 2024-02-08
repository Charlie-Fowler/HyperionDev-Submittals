
'''Start
    User Input time (minutes) variables for: swimming, cycling and running
    calculate total time (total time = Sum of swimming,cycling and running record)
    
    IF TIME WITHIN 0-100 MINUTES, AWARD PROVINCIAL COLOURS
    IF WITHIN 101-105 MINUTES, AWARD PROVINCIAL HALF COLOURS
    IF 106-110 MINUTES AWARD PROVINCIAN SCROLL
    ELSE (111+ MINUTES) NO AWARD

    END'''

print('''Welcome!
This programme will detemine you award based on your scores for the triatholon!
Please enter your scores in MINUTES
      ''')

#Request input from user with scores of each event
swimming_record = int(input('How long did it take you to finish the swimming event? '))
cycling_record = int(input('How long did it take you to complete the cycling event? '))
running_record = int(input('How long did it take you to finish the running event? '))

#Compile each record variable to work out total time
total_time = swimming_record + cycling_record + running_record
print(f'Your total time completing the triatholon was {total_time} minutes.')

#Allocate the award based on total time

if total_time <=100: #If time is below 100 minutes, P.Colours award
    print('''Congrats!
 You have been awarded the Provincial Colours!''')

elif total_time <= 105: #If time is between 101-105 . P.HalfColours award
    print('You have been awarded the Provincial Half Colours!')

elif total_time <= 110: #If time is between 106-110, Provincial Scroll award
    print('You have been awarded the Provincial Scroll!')

else: #Else, you wouldnt qualify, no award
    print('Unfortunately you have not won an award, maybe next time!')
