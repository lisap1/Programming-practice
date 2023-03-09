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
snack_response = ""

# initialise variables
# loop to make testing easier


def snack_checker():
    snack_ok = ""
    snack_amount = ""

    # ask user for the snacks they want
    snack_wanted = input("Snack: ").lower()

    for var_list in valid_snacks:
        # if the snack wanted is in one of the lists, return full name
        if snack_wanted in var_list:
            snack = var_list[0].title()
            snack_ok = "yes"
            num_snacks = input("How many items of " + snack + ": ")
            snack_amount = str(num_snacks + " " + snack)
            break
        else:
            snack_ok = "no"

    # if the snack is ok ask question again
    if snack_ok == "yes":
        print("Snack choice: ", snack_amount)
    else:
        print("Invalid choice")


def yes_no(to_check):
    error = "Please enter 'yes' or 'no'"
    # loop until valid response
    valid = False
    while not valid:
        response = input("Would you like to order snacks: ").lower()
        if response in to_check:
            return response
        else:
            for item in to_check:
                if response == item[0]:
                    return item
        print(error)


# main routine
while snack_response != "no":
    snacks_question = yes_no(["yes", "no"])
    if snacks_question == "yes":
        snack_checker()
    else:
        snack_response = "no"
