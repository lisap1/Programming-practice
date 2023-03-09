# valid snacks holds list of all snacks
# each item in valid snacks is a list with
# valid options for each snack <full name, letter code (a - e)
# and possible abbreviations etc.
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "m and m", "b"],
    ["pita chips", "chips","pc", "pita", "c"],
    ["water", "w", "d"]
]

# initialise variables
snack_ok = ""
snack = ""


# loop to make testing easier
for item in range(0, 3):
    # ask user for the snacks they want
    snack_wanted = input("Snack: ").lower()

    for var_list in valid_snacks:
        # if the snack wanted is in one of the lists, return full name
        if snack_wanted in var_list:
            snack = var_list[0].title()
            snack_ok = "yes"
            break
        else:
            snack_ok = "no"

    # if the snack is ok ask question again
    if snack_ok == "yes":
        print("Snack choice: ", snack)
    else:
        print("Invalid choice")
