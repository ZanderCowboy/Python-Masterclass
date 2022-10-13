def factorial(number: int) -> int:
	"""
	Given an integer, it returns its factorial.
	:param number: given integer to determine factorial
	:return: the calculated factorial integer.
	"""
	answer = 1
	while number != -1:
		if number == 0:
			return answer
		answer *= number
		number -= 1


for i in range(36):
	print(i, factorial(i))
