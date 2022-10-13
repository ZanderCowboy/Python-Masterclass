def sum_numbers(*numbers: float) -> float:
	"""
	Taking number arguments, it returns the sum.
	:param numbers: a star argument taking the `float` values
		to be added together.
	:return: the sum of the given `floats`
	"""
	answer = 0
	for number in numbers:
		answer += number

	return answer


print(sum_numbers(1,2,3))
print(sum_numbers(8,20,2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
