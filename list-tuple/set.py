# subcribed users
# subscribers = {'Alex', 'Sergei', 'Abdulloh', 'Ali', 'Nazarbek', 'Oyniso', 'Jahonbaxsh', 'Azamat', 'Anvar', 'Gaf\'ur', 'G\'ulom', 'Taylor', 'Kendrick', 'Marcos', 'Mark', 'Steven'}


# subscriber = input('Enter your name: ')
# if subscriber in subscribers:
#       print('You are already subscribed. Enjoy the app')
# else:
#       subscribers.add(subscriber)
#       print('You are subscribed to our app. Thank you for your subscription. ')

# basket

shopping_list = {'T Shirt', 'NB sneakers', 'Polo Shirt', 'LV shorts', 'NB socks', 'North Face Jacket', 'Cap', 'Tom Ford', 'Casio'}
basket = set(input('What have you bought already?: ').split(', '))
intersection = shopping_list & basket
difference = shopping_list - basket

intersection_str = ', '.join(intersection)
difference_str = ', '.join(difference)


print(f'You have bought {intersection_str}. You didn\'t buy {difference_str} yet.')
