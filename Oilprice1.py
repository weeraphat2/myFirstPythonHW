def menu1():	
	print("################################################################################")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#				      		 	                       #")
	print("#		                                                               #")
	print("#				                                               #")
	print("#			   	     Welcome	                               #")
	print("#						                               #")
	print("#						                               #")
	print("#				        	                               #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("################################################################################")

def menu2():	
	print("################################################################################")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#					Menu				       #")
	print("#			      1.Gasoline 95 price 29.16 BAHT                   #")
	print("#			      2.Gasoline 91 price 25.30 BAHT		       #")
	print("#			      3.Gasohol 91  price 21.68 BAHT		       #")
	print("#			      4.Gasohol E20 price 20.2  BAHT		       #")
	print("#			      5.Gasohol 95  price 21.2  BAHT		       #")
	print("#			      6.Diesel      price 21.1  BAHT		       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("################################################################################")

def menu3():
	print("################################################################################")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#				    		                               #")
	print("#			                                                       #")
	print("#			      	  	                                       #")
	print("#			            working type                               #")
	print("#			      	  1.Money to Liter                             #")
	print("#			      	  2.Liter to Money	                       #")
	print("#			      		                                       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("################################################################################")

def menu4():
	print("################################################################################")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#				    		                               #")
	print("#			                                                       #")
	print("#			      	  	                                       #")
	print("#			                                                       #")
	print("#			      	                                               #")
	print("#			       press enter a value          	               #")
	print("#			      		                                       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("################################################################################")
		
def menu5():
	print("################################################################################")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#				    		                               #")
	print("#			                                                       #")
	print("#			      	  	                                       #")
	print("#			                                                       #")
	print("#			      	                                               #")
	print("#			           1.Exit the program      	               #")
	print("#			      	   2.Start work again	                       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("#									       #")
	print("################################################################################")
		
while True :

	menu1()
	a = input("press anything to enter the program")

	a = 0
	while not(a in [1,2,3,4,5,6]) :	
		menu2()
		b = input("select Oil :")
		if b.isnumeric() :
			a = int(b)

		else:
			a = 0

	c = 0
	while not(c in [1,2]) :
		menu3()
		d = input("select working type :")
		
		if d.isnumeric() :
			c = int(d)
		else:
			c = 0
	

	e = 0
	while not(e) :
		menu4()
		f = input("press enter a value :")

		if f.isnumeric() :
			e = float(f)
		else:
			e = 0
		f=float(f)
		if d == '1' :
			if b == '1' :		
				e = f*29.16
				print("amount received = {}".format(e),"Baht")
			elif b == '2' :		
				e = f*25.30
				print("amount received = {}".format(e),"Baht")
			elif b == '3' :		
				e = f*21.68
				print("amount received = {}".format(e),"Baht")
			elif b == '4' :		
				e = f*20.2
				print("amount received = {}".format(e),"Baht")
			elif b == '5' :		
				e = f*21.0
				print("amount received = {}".format(e),"Baht")
			else :		
				e = f*21.1
				print("amount received = {}".format(e),"Baht")

		if d == '2' :
			if b == '1' :		
				e = f/29.16
				print("Number of liters received = {}".format(e),"Liter")
			elif b == '2' :		
				e = f/25.30
				print("Number of liters received = {}".format(e),"Liter")
			elif b == '3' :		
				e = f/21.68
				print("Number of liters received = {}".format(e),"Liter")
			elif b == '4' :		
				e = f/20.2
				print("Number of liters received = {}".format(e),"Liter")
			elif b == '5' :		
				e = f/21.0
				print("Number of liters received = {}".format(e),"Liter")
			else :		
				e = f/21.1
				print("Number of liters received = {}".format(e),"Liter")
	g = input("")	

	a = 0
	while not(a in [1,2]) :
		menu5()
		b = input("Exit the program :")
		if b.isnumeric() :
			a = int(b)
		else:
			a = 0
	if a == 1 :
		break
