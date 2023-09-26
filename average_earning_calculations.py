import sys
def get_a_float(prompt):
	problem_with_input=True
	while(problem_with_input):
		sys.stdout.write(prompt)
		try:
			user_entered_float = float( sys.stdin.readline() )
			problem_with_input=False
		except ValueError:
			sys.stdout.write("You must enter a number!\n")
	return user_entered_float

def get_an_int(prompt):
	return int( get_a_float(prompt) )

def average_earnings_calculator_v2():
	total_income = get_a_float("Enter your total income for 2020: ")
	num_days_worked = get_an_int("Enter number of days worked in 2020: ")
	try:
		average_income_per_day = total_income / num_days_worked
		sys.stdout.write("You've earned an average daily income of $"+str(average_income_per_day))
	except ZeroDivisionError:
		sys.stdout.write("Sorry, we can't calculate the average daily earnings!")

average_earnings_calculator_v2()
