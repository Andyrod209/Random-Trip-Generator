import random 
# list of options for trip
destinations = ["Sacramento", 'Las Vegas', 'Salt Lake City', 'Toronto' ]
restaurants = ['Jack in the Box', 'KFC', 'Subway', 'Pizza Hut']
ways_of_transportation = ["Rental Car", 'Uber', 'Bus', 'Train' ]
entertainments = ['Movies', 'Skatebroading', 'Arcarde', 'Mini Golf'] 
# picking options with randomly generated numbers
def random_list_trip(trip_to):
    random_number = random.randint(0, 3) 
    if random_number == 0:
        print(trip_to[0]) 
    elif random_number == 1:
        print(trip_to[1])
    elif random_number == 2:
        print(trip_to[2])
    elif random_number == 3:
        print(trip_to[3])
    return trip_to


# re-selecting 
def selecting():

    print('Destination:')
    random_list_trip(destinations)
    print('')

    print('Restaurant:')
    random_list_trip(restaurants)
    print('')

    print('Way of transportation')
    random_list_trip(ways_of_transportation)
    print('')

    print('entertainment')
    random_list_trip(entertainments)
    print('')
    # created a while loop to get users response for their change
    yes = True
    while yes is True:
        user_response = input('Did you like your options? pick Yes or No.\n To change a specific option type "change" ')
        user_response =  user_response.capitalize()
        if user_response == 'Yes':
            print('Glad you liked your options.')
            break
        
        elif user_response == 'No':
            print('re-selecting options...') 
            print('')
            print('New destination:')
            random_list_trip(destinations)
            print('')
            print('New restaurant:')
            random_list_trip(restaurants)
            print('')
            print('New way of transportation:')
            random_list_trip(ways_of_transportation)
            print('')
            print('New entertainment:')
            random_list_trip(entertainments)
            print('')
        
        elif user_response == "Change":
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
            print('')
        
        else:
            print('') 

selecting()     
                



                        
                
               
       
            