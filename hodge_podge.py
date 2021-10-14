def is_multiple_of(x, y):
	if(x % y == 0):
		print("True")
	else:
		print("False")

is_multiple_of(12, 5)

def is_leap_year(x):
	if(x % 100 == 0):
		if(x % 400 == 0):
			print("True")
	elif(x % 4 == 0):
		print("True")
	else:
		print("False")

is_leap_year(2016)

def determine_quadrant(x, y):
	if(x == 0 and y == 0):
		print("Origin")
	if(x > 0 and y > 0):
		print("I")
	elif(x < 0 and y > 0):
		print("II")
	elif(x < 0 and y < 0):
		print("III")
	elif(x > 0 and y < 0):
		print("IV")
	elif(x > 0 and y == 0):
		print("+ x-axis")
	elif(x < 0 and y == 0):
		print("- x-axis")
	elif(x == 0 and y > 0):
		print("+ y-axis")
	elif(x == 0 and y < 0):
		print("- y-axis")

determine_quadrant(3, 0)

def calc_federal_income_tax(x):
	if(x >= 0 and x <= 9225):
		print(x * .1)
	elif(x >= 9226 and x <= 37450):
		pass
	elif(x >= 37451 and x <= 90750):
		pass
	elif(x >= 90751 and  x <= 189300):
		pass
	elif(x >= 189301 and x <= 411500):
		pass
	elif(x >= 411501 and x <= 413200):
		pass
	elif(x >= 413201):
		pass

calc_federal_income_tax(5000)