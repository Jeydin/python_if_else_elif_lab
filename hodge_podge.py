def is_multiple_of(x, y):
	if(x % y == 0):
		return "True"
	else:
		return "False"

print(is_multiple_of(12, 5))

def is_leap_year(x):
	if(x % 100 == 0):
		if(x % 400 == 0):
			return "True"
		else:
			return "False"
	elif(x % 4 == 0):
		return "True"
	else:
		return "False"

print(is_leap_year(1900))

def determine_quadrant(x, y):
	if(x == 0 and y == 0):
		return "Origin"
	if(x > 0 and y > 0):
		return "I"
	elif(x < 0 and y > 0):
		return "II"
	elif(x < 0 and y < 0):
		return "III"
	elif(x > 0 and y < 0):
		return "IV"
	elif(x > 0 and y == 0):
		return "+ x-axis"
	elif(x < 0 and y == 0):
		return "- x-axis"
	elif(x == 0 and y > 0):
		return "+ y-axis"
	elif(x == 0 and y < 0):
		return "- y-axis"

print(determine_quadrant(3, 0))

def calc_federal_income_tax(x):
	if(x >= 0 and x <= 9225):
		return x * .1
	elif(x >= 9226 and x <= 37450):
		return 922.5 + (x - 9225) * .15
	elif(x >= 37451 and x <= 90750):
		return 5156.25 + (x - 37450) * .25
	elif(x >= 90751 and  x <= 189300):
		return 18481.25 + (x - 90750) * .25
	elif(x >= 189301 and x <= 411500):
		return 46075.25 + (x - 189300) * .33
	elif(x >= 411501 and x <= 413200):
		return 119401.25 + (x - 441500) * .35
	elif(x >= 413201):
		return 119996.25 + (x - 413200) * .396

print(calc_federal_income_tax(50000))