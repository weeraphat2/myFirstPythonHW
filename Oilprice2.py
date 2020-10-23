from zeep import Client
from lxml import rtree
client = Client('http://www.pttor.com/oilPrice.asmx?WSDL')
resoult = client.service.CurrentOilPrice(Language="en")
root = etree.formstring(result)
n = len(root)
name = ['none']
price = [0]

def menu1():
    print("#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 28 + "Welcome to the program" + " " * 28 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)

def menu2():
    print("#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 37 + "Menu" + " " * 37 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 24 + "1.Gasoline 95   ราคา 29.16 BATH" + " " * 23 + "#")
    print("#" + " " * 24 + "2.Gasoline 91   ราคา 25.30 BATH" + " " * 23 + "#")
    print("#" + " " * 24 + "3.Gassohol 91   ราคา 21.68 BATH" + " " * 23 + "#")
    print("#" + " " * 24 + "4.Gassohol E20  ราคา 20.2  BATH" + " " * 23 + "#")
    print("#" + " " * 24 + "5.Gassohol 95   ราคา 21.0  BATH" + " " * 23 + "#")
    print("#" + " " * 24 + "6.Diesel        ราคา 21.1  BATH" + " " * 23 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)

def menu3():
    print("#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 33 + "เลือกฟังก์ชันในการคำนวน" + " " * 26 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 33 + "1.เงินเป็นลิตร" + " " * 34 + "#")
    print("#" + " " * 33 + "2.ลิตรเป็นเงิน" + " " * 34 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)

def menu4():
    print("#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 31 + "กรุณาใส่จำนวน" + " " * 36 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)

def menu5():
    print("#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 30 + "ออกจากโปรแกรมหรือไม่" + " " * 30 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 31 + "1. ออกจากโปรแกรม" + " " * 31 + "#")
    print("#" + " " * 31 + "2. เริ่มการทำงานใหม่อีกครั้ง" + " " * 25 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)

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
