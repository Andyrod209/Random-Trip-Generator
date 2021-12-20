import random 
# list of options for trip
destinations = ["Sacramento", 'Las Vegas', 'Salt Lake City', 'Toronto' ]
restaurants = ['Jack in the Box', 'KFC', 'Subway', 'Pizza Hut']
ways_of_transportation = ["Rental Car", 'Uber', 'Bus', 'Train' ]
entertainments = ['Movies', 'Skatebroading', 'Arcarde', 'Mini Golf'] 
# picking options with randomly generated numbers
def random_list_trip():
    destination_to = destinations[random.randint(0,3)]
    print(f'Destination to!... {destination_to}')
    restaurant_is = restaurants[random.randint(0, 3)]
    print(f'Eating at!... {restaurant_is}')
    transportation_is = ways_of_transportation[random.randint(0,3)]
    print(f'Riding in!... {transportation_is}')
    entertainment_is = entertainments[random.randint(0, 3)]
    print(f"What you're doing!.. {entertainment_is}")

def changing_option(list_change):
    change = True
    while change is True:       
    user_changing_option = input('choose a number from... \n 1. Destinations \n 2. restaurants \n 3. Ways of transportations \n 4. Enterainment \n : ')
    print('')                      
    if user_changing_option == "1":
        print(' New destination is:')
        random_list_trip(destinations)
        break                                   
                    
    elif user_changing_option == '2':
        print(' New restaurant is:')
        random_list_trip(restaurants)
        break
                
    elif user_changing_option == '3':
        print(' New transportation is:')
        random_list_trip(ways_of_transportation)
        break
                    
    elif user_changing_option == '4':
        print(' New entertainment is:')
        random_list_trip(entertainments)
        break
    else:
        print('')
    
def selecting():

    random_list_trip()       

    # created a while loop to get users response for their change
    yes = True
    while yes is True:
        user_response = input('Did you like your options? pick Yes or No.\n To change a specific option type "change" ')
        user_response =  user_response.capitalize()
        if user_response == 'Yes':
            print('Glad you liked your options.')
            break
        
        elif user_response == 'No':
            random_list_trip()
        
        elif user_response == "Change":
            
            print('')
        
        else:
            print('') 

selecting()   