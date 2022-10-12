parrot = "Norwegian Blue"                               # Video Number: 52

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")
