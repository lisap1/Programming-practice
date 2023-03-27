import re


# function goes here
def string_check(choice, options):

    for var_list in options:

        if choice in var_list:
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        else:
            is_valid = "no"

    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


def get_snack():
    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # each item in valid snacks is a list with
    # valid options for each snack <full name, letter code (a - e)
    # , and possible abbreviations etc.>
    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["M&M's", "m&m's", "mms", "m", "m and m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "d"]
    ]

    # holds snack order for a single user.
    snack_order = []

    # if they say yes, ask what snacks they want (and add to our snack order)
    desired_snack = ""
    while desired_snack != "xxx":
        # ask user for desired snack and put it in lowercase
        desired_snack = input("snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1

        desired_snack = desired_snack.strip()

        snack_choice = string_check(desired_snack, valid_snacks)

        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "invalid choice"
        # add snack amount to list...
        amount_snack = [amount, snack_choice]
        print(amount_snack)
        # check that snack is ot the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(amount_snack)


# valid options for yes / no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]
# show snack orders
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("do you want to order snacks: ").lower()
    check_snack = string_check(want_snack, yes_no)
    if check_snack == "invalid choice":
        print("invalid - Please enter yes or no")

if check_snack == "Yes":
    get_order = get_snack()
else:
    get_order = []

print()
if len(get_order) == 0:
    print("Snacks ordered: None")
else:
    print("Snacks ordered: ")
    for item in get_order:
        print(item)
