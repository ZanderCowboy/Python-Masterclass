name = input("Please enter your name: ")                    # Video Number: 53, 54
age = int(input("Please enter your age: "))

if 18 <= age < 31:
    print("Welcome to the holiday, {}".format(name))
else:
    if age <= 18:
        print("Sorry {}, you need to be older.".format(name))
    else:
        print("Sorry {}, you need to be younger than 31.".format(name))
