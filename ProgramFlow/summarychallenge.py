items = ["Cakes", "Doughnut", "Candy", "Pancakes", "Coca-Cola", "Sweets"]

option = 99
while option != 0:
    print("Please select one of the following options:\n"
          "1.\tCakes\n"
          "2.\tDoughnut\n"
          "3.\tCandy\n"
          "4.\tPancakes\n"
          "5.\tCoca-Cola\n"
          "6.\tSweets\n"
          "0.\tExit")
    option = int(input())
    if option < 0 or option > 6:
        print("Invalid! Please enter a valid option.\n")
        continue
    elif option == 0:
        print("Exiting.")
    else:   # Option is valid
        print("You selected option {} as {}\n".format(option, items[option]))
