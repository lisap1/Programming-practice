valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "m and m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]
snack_response = ""
# holds snack order for single user
snack_order = []
# initialise variables


def snack_checker():
    snack_ok = ""
    snack_amount = ""
    num_snacks = ""

    # ask user for the snacks they want
    while snack_ok != "yes":
        snack_wanted = input("Snack: ").lower()
        for var_list in valid_snacks:
            # if the snack wanted is in one of the lists, prompt for how many
            if snack_wanted in var_list:
                snack = var_list[0].title()
                snack_ok = "yes"
                # make sure number is integer and less than 4
                while not num_snacks.isdigit():
                    num_snacks = input("How many items of " + snack + ": ")
                    if int(num_snacks) <= 4:
                        snack_amount = str(num_snacks + " " + snack)
                    else:
                        print("Please enter a whole number between 1 and 4")
                        num_snacks = ""
            else:
                snack_ok = "no"

        # if the snack is ok ask question again
        print(snack_ok)
        if snack_ok == "yes":
            print("Snack choice: ", snack_amount)
        else:
            print("Invalid choice")
            snack_ok = ""


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
    snacks_question = yes_no(["yes", "y", "no", "n"])
    if snacks_question == "yes":
        snack_checker()
    else:
        snack_response = "no"
