import random 
# list of options for trip
destinations = ["Sacramento", 'Las Vegas', 'Salt Lake City', 'Toronto' ]
restaurants = ['Jack in the Box', 'KFC', 'Subway', 'Pizza Hut']
ways_of_transportation = ["Rental Car", 'Uber', 'Bus', 'Train' ]
enterainments = ['Movies', 'Skatebroading', 'Arcarde', 'Mini Golf'] 
# picking options with random generated numbers
def random_destination():
    destination_number = random.randint(0,3)
    if destination_number == 0:
        print(f'Traveling to: {destinations[0]}')
    elif destination_number == 1:
        print(f'Traveling to: {destinations[1]}')
    elif destination_number == 2:
        print(f'Traveling to: {destinations[2]}')
    elif destination_number == 3:
        print(f'Traveling to: {destinations[3]}')



def ran_restaurant():
    restaurant_number = random.randint(0,3)
    if  restaurant_number== 0:
        print(f'Eating at: {restaurants[0]}')
    elif  restaurant_number == 1:
        print(f'Eating at: {restaurants[1]}')
    elif  restaurant_number == 2:
        print(f'Eating at: {restaurants[2]}')
    elif restaurant_number == 3:
        print(f'Eating at: {restaurants[3]}') 

 

def ran_transportation():
    transportation_number = random.randint(0,3)
    if transportation_number == 0:
        print(f'Way of transportation: {ways_of_transportation[0]}')
    elif transportation_number == 1:
        print(f'Way of transportation: {ways_of_transportation[1]}')
    elif transportation_number == 2:
        print(f'Way of transportation: {ways_of_transportation[2]}')
    elif transportation_number == 3: 
        print(f'Way of transportation: {ways_of_transportation[3]}')



def ran_entertainment():
    entertainment_number = random.randint(0,3)
    if entertainment_number == 0: 
        print(f'Thing to do: {enterainments[0]}')
    elif entertainment_number == 1:
        print(f'Thing to do:{enterainments[1]}')
    elif entertainment_number == 2:
        print(f'Thing to do: {enterainments[2]}')
    elif entertainment_number == 3:
        print(f'Thing to do: {enterainments[3]}')



# re-selecting a destination
def selecting():
    random_destination()
    print('')
    ran_restaurant()
    print('')
    ran_transportation()
    print('')
    ran_entertainment()
    print('')

    yes = True
    while yes is True:
        user_response = input('Did you like your options? pick Yes or No. ')
        if user_response == 'Yes' or user_response == 'yes':
            print('Glad you liked your options.')
            break
        elif user_response == 'No' or user_response == 'no':
            print('re-selecting options...') 
            random_destination()
            print('')
            ran_restaurant()
            print('')
            ran_transportation()
            print('')
            ran_entertainment()
            print('')
            
        else:
            print('') 

selecting()
    