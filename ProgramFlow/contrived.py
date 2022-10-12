numbers = [1, 45, 31, 15, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list if divisible by 8
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine")
