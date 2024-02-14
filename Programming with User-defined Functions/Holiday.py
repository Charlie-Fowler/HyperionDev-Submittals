'''
Calculate total holiday costs
request user input regarding:
    City_flight = destination
    num_nights = duration
    rental_days = rental car duration
then create the following four functions:
    hotel_cost: will take in num_nights and return cost
    plane_cost: will take city_flight and return cost
    car_rental: will take rental_days and return cost
    holiday cost will take the prior functions and return Total Cost

print out details of costs
'''
# generic welcome variable for easy useability
welcome = '''Welcome to your holiday cost calculator!
Please Note: all options must be entered in numerically'''
# generic error handling message for invalid inputs
invalid_message = '''\nSorry, we unfortunately dont have an option for that,
please try again.'''

destinations = ['1. Bali, Indonesia',
                '2. Perth, Australia',
                '3. Vancouver, Canada',
                '4. Lima, Peru',
                '5. Frankfurt, Germany']
# function database:
# plane cost function to calculate the cost which is location dependant.
def plane_cost(city_flight):
    if city_flight == 1:
        return 1250
    if city_flight == 2:
        return 950
    if city_flight == 3:
        return 900
    if city_flight == 4:
        return 500
    if city_flight == 5:
        return 200
    else:
        print(invalid_message)
# hotel cost function to calculate the cost with an added variable of star rating
def hotel_cost(num_nights):
    if star_rating == 5:
        return num_nights * 300
    if star_rating == 4:
        return num_nights * 200
    if star_rating == 3:
        return num_nights * 150
    if star_rating == 2:
        return num_nights * 100
    if star_rating == 1:
        return num_nights * 50
    
    else:
        print(f'''unfortunately we do not have any {star_rating} star hotels,
please try another rating between 1-5 stars''' )
# car rental function to calculate the cost of a car hire, 0 days is valid
def car_rental(rental_days):
    if type(rental_days) is int:
        if rental_days == 0:
            return 0
        else:
            return rental_days * 50
        
# holiday cost is the combined costings of the prior functions
def holiday_cost(city_flight, num_nights, rental_days):
    num_nights = hotel_cost(num_nights)
    rental_days = car_rental(rental_days)
    city_flight = plane_cost(city_flight)
    return num_nights + city_flight + rental_days

# request user inputs regarding their holiday:
# User to input city_flight destination:
try:
    # Show flight options and requesting a choice
    print("\nPlease review our destinations:\n")
    for option in destinations:
        print(option)
    city_flight = int(input('\nPlease select a destination by selecting 1,2,3,4 or 5.\n'))
    # request duration of holiday and star rating of hotel
    num_nights = int(input('\nHow many nights are you going to stay?\n'))
    star_rating = int(input('\nHow many stars would you like your hotel to be?\n'))
    # request duration of car rental
    rental_days = int(input("\nHow many days are you needing to hire a car for?\n"))
    # Accumulate the total cost of the holiday and display options

# display accumulated information in easy to read format
    print(f'''
Thank you for using out holiday calculation system,
The total cost of your holiday will be £{holiday_cost(city_flight, num_nights, rental_days)}.
Your flight is £{plane_cost(city_flight)}.
Your hotel cost is £{hotel_cost(num_nights)} for the duration of {num_nights} nights.
Your rental car is £{car_rental(rental_days)} for the duration of {rental_days} days.
''')
except ValueError:
    print(invalid_message)
