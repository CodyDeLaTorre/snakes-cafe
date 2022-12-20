order_dict = {
    'Wings': 0,
    'Cookies': 0,
    'Spring Rolls': 0,
    'Salmon': 0,
    'Steak': 0,
    'Meat Tornado': 0,
    'A Literal Garden': 0,
    'Ice Cream': 0,
    'Cake': 0,
    'Pie': 0,
    'Coffee': 0,
    'Tea': 0,
    'Unicorn Tears': 0
}

greeting_string = ''' **************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**************************************'''

menu_string = '''Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

'''

print(greeting_string)
print(menu_string)
order = ''
while order != 'quit':
    order = input('''
    ***********************************
    ** What would you like to order? **
    ***********************************
    ** To quit at any time, type "quit" **
    > ''')
    order_dict[order] += 1
    print(f'{order_dict[order]} order of {order} have been added to your meal')
if order == 'quit':
    exit()
