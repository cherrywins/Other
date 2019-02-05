
operations = ["addition", "subtraction", "division", "multiplication", "exponentiation", "1", "2", "3", "4", "5"]

def get_numbers_and_operation():
	"""
	Asks user to specify a operation to perform and two numbers.
	Returns:
        (str) operation - name of the operation from the list
        (int) x - first number
        (int) y - secons number
	"""
	# We get user's input for city
	print("Hello! Welcome to Katya\'s calculator! Please choose the operation you want to use: addition (or 1), subtraction (2), division (3), multiplication (4), exponentiation(5): ")
	while True:
		operation = input('Please enter the name of operation or operation\'s number: ')
		if operation in operations:
			break
		else:
			print("Please enter the operation or operation's number from the list above")

	# We get user's input for the numbers
	
			
	while True:
		x = input('Enter the first number: ')
		y = input('Enter the second number: ')
		if isinstance(x,(float, int)) and isinstance(y, (float, int)):
			break
		else:
		    print("Please enter the number! Both intereger and float types will work")	

	return operation, x, y



def addition(x, y):
	summ = x+y
	print("The sum: " + str(summ))


def subtraction(x,y):
	sub = x-y
	print("The subtraction: " + str(sub))

def division(x,y):
	div = round(x/y,2)
	print("The division: " + str(div))
	
def multiplication(x,y):
	mult = x*y
	print("The multiplication: " + str(mult))

def exponentiation(x,y):
	exp = x**y
	print("The exponentiation: " + str(exp))




def calculator(operation, x, y):
	if operation == "addition" or operation == "1":	
		print("We are doing a addition!")	
		addition(x,y)
	elif operation == "subtraction" or operation == "2":
		print("We are doing a subtraction!")
		subtraction(x,y)
	elif operation == "division" or operation == "3":
		print("We are doing a division!")
		division(x,y)
	elif operation == "multiplication" or operation == "4":
		print("We are doing a multiplication!")
		multiplication(x,y)
	elif operation == "exponentiation" or operation == "5":
		print("We are doing a exponentiation!")
		exponentiation(x,y)
	

def main():
	while True:
		operation, x, y = get_numbers_and_operation()
		calculator(operation, x, y)
		
		restart = input('\nWould you like to restart? Enter yes or no.\n')
		if restart.lower() != 'yes':
			break

if __name__ == "__main__":
	main()
