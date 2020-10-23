water = 400
milk = 540
coffeebeans = 120
disposablecups = 9
money = 550

def printall() :
	print("the coffee machine has : ")
	print(water,"of water")
	print(milk,"of milk")
	print(coffeebeans, "of coffeebeans")
	print(disposablecups,"of disposablecups")
	print(money,"of money")

printall()
while True :
	p = ''
	while not(p in ['buy','fill','take']) :
			p = input("write action (buy,fill,take) :\n>")
	if p == 'buy' :
		a = 0
		while not (a in ['1','2','3']) :
			a = input("What do you want to buy?  1 - espresso, 2 - latte, 3 - cappuccino : \n>")
		if a == '1' :
			water -= 250
			milk -= 0
			coffeebeans -= 16
			disposablecups -= 1
			money += 4
		if a == '2' :
			water -= 350
			milk -= 75
			coffeebeans -= 20
			disposablecups -= 1
			money += 7
		if a == '3' :
			water -= 200
			milk -= 100
			coffeebeans -= 12 
			disposablecups -= 1
			money += 6
		printall()
	
	if l == 'fill' :
		water += int(input("how many ml of water do you want to add :\n>"))
		milk += int(input("how many al of milk do you want to add :\n>"))
		coffeebeans += int(input("how many grams of coffee beans do you want to add :\n>"))
		disposablecups += int(input("how many disposable cups of coffee do yu want to add :\n>"))

	if m == 'take' :
		print('I gave $',money)
		money = 0
		printall()
		
	y = 0
	while not(y in ['1','2']) :
		y = input('1-exit ,2-back to menu') 
	if y == '1' :
		break
