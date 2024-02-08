'''
list 'menu' to hold atleast 4 items
dictionary 'stock' to hold stock value for each 'menu' item
dictionary 'price' to hold cost for each 'menu' item
iterate through each key:value pair
calculate total items held
calculate total_stock worth with:
total_stock = (stock[] * price[])
print
'''
menu = ['Sausages', 'Toast', 'Omelette', 'Yogurt']
#keys are indexed to the menu to allow alterations to the list menu
stock = { menu[0]: 5,
menu[1]: 10,
menu[2]: 8,
menu[3]: 2}

price = {menu[0]: 4.00,
menu[1]: 2.00,
menu[2]: 2.50,
menu[3]: 1.00}

total_items= 0 # placeholder value
for keys in stock.keys():
# for each key, add one value to total stock to accumulate total amount
    total_items += stock[keys]
print(f'The total amount you hold in stock is {total_items} items')

total_stock = 0 # placeholder value
for key in stock.keys():
# for each interation, times the price by the quantity then sum up
    total_stock += stock[key] * price[key]
print(f'The total value of your stock is £{int(total_stock)}')
