# To calcuate a user's total holiday cost, which includes the plane cost, hotel cost and car-rental cost.
# 1st get user inputs for the flight city, no of nights to stay & no of days for hiring a car
# 2nd create three functions accordingly for flight, hotal and car rental costs
# Lastly calculate total holiday cost by summing up all costs above

city_flight = input('Please type your holiday destination city: ')
print(city_flight)
num_nights = int(input('Please type no of nights you will stay in the city: '))
print(num_nights)
rental_days = int(input('Please type no of days you will rent a car: '))
print(rental_days)

def plane_cost(city_flight):
    if city_flight == 'City1':
        return 200
    elif city_flight == 'City2':
        return 300
    else:
        return 400

def hotel_cost(num_nights):
    return num_nights * 150

def car_rental(rental_days):
    return rental_days * 50
    
def holiday_cost(plane_cost, hotel_cost, car_rental):
    return  plane_cost(city_flight) + car_rental(rental_days) + hotel_cost(num_nights)

# print("City: ", city_flight)
# print("No of nights: ", num_nights)
# print("No of car rental: ",  rental_days)
# print("Holiday cost: ", holiday_cost(plane_cost, hotel_cost, car_rental))