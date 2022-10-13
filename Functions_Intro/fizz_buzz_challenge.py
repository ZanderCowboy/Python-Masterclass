def fizz_buzz(number: int) -> str:
	"""
	A Fizz Buss game that returns the next answer, usually played
	by 2 or more people.

	:param number: input number
	:return: a string with either "fizz" when divisible by 3, or
		a string with "buzz" when divisible by 5, or
		a string with "fizz buzz" when divisible by 3 and 5, or
		a string with the number not divisible by 3 and 5.
	"""
	if number % 3 == 0 and number % 5 == 0:
		# result = "fizz buzz"
		return "fizz buzz"
	elif number % 3 == 0:
		# result = "fizz"
		return "fizz"
	elif number % 5 == 0:
		# result = "buzz"
		return "buzz"
	else:
		return str(number)


for i in range(1, 101):
	print(fizz_buzz(i))
