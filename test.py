num_snacks = ""
snack = "popcorn"

while not num_snacks.isdigit():
    num_snacks = input("How many items of " + snack + ": ")
    if int(num_snacks) <= 4:
        snack_amount = str(num_snacks + " " + snack)
    else:
        print("Please enter a whole number between 1 and 4")
        num_snacks = ""
