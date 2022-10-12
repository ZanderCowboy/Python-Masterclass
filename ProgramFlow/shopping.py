shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]                  # Video Number: 61

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        continue    # skipped everything else in the block to be ignored
        # break

    print("Buy " + item)
