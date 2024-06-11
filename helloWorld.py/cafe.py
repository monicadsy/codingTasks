# 1st Create a list called menu which contain 4 items sold in the cafe
# 2nd create a dictionary called stock contain the stock value for each item on menu
# 3rd create a dictionary called price contain the price for each item on menue
# Last, calculate the total stock worth in the cafe and print the result

menu = ['mocha', 'tea', 'coffee', 'juice']
stock = {'mocha': 5, 'tea': 5, 'coffee': 10, 'juice': 5}
price = {'mocha': 3, 'tea': 2, 'coffee': 3, 'juice': 2}
total_stock = 0
for i in menu:
    total_stock += stock[i] * price[i]
print(total_stock)