def buy_and_sell_stock(arr_stock):
	minimum = -1 
	profit = 0
	for price in arr_stock:
		if (minimum == -1 ) or (price < minimum):
			minimum = price 
		else:
			profit = max(profit, price - minimum)
	return profit 

