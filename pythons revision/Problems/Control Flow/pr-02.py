"""
2. Vending Machine: Simulate a simple vending machine. The program should have a list of available items with prices. The user can choose an item and insert money. Use if statements to check if the chosen item exists and if the inserted money is enough. If so, dispense the item and provide change if necessary. Otherwise, inform the user about invalid choices or insufficient funds.
"""

print('Grab Your Favourite Drink Here!')

list_of_products = [
    {'Coke': 10},
    {'Thumbs up': 12},
    {'Mirinda': 9},
    {'Sprite': 13},
    {'Pepsi': 15},
]


def display_products(arr_of_products):
    for count, product in enumerate(arr_of_products, 1):
        for p_name in product:
            print(p_name)


display_products(list_of_products)
usr_inp = input('Please pick Your Drink: ')

list_of_drink_names = [
    items for products in list_of_products for items in products
]

while usr_inp in list_of_drink_names:
    print('This is your selected drink: ', usr_inp)
    # usr_inp = input('Please pick Your Drink: ')
    for count, product in enumerate(list_of_products):
        for p_name, p_price in product.items():
            if p_name == usr_inp:
                drink_price = p_price

    print('The price of {} is ${}'.format(
        usr_inp, drink_price))
    # ask user for money
    pay_amount = int(input('Insert the money: '))
    if pay_amount == drink_price:
        print('Here is Your drink "{}", Visit again'.format(usr_inp))
        break
    else:
        print('This is not the correct amount, the amount is {}'.format(drink_price))
        continue
