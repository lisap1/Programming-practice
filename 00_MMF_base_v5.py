import re
import pandas


# functions go here
# checks name is valid
def not_blank(question):
    valid = False

# while valid= False, continue asking
    while not valid:
        response = input(question)

        if response != "" and response.isalpha():
            return response
        elif response == "":
            print("Sorry - This can't be blank, please enter your name")
        elif not response.isalpha():
            print("Sorry - Your name cannot contain numbers or symbols")
        else:
            print("Error - Please try again")


# checks age is valid
def int_check(question, low_num, high_num):
    # error message
    error = "Please enter a whole number between {} and {}"\
        .format(low_num, high_num)
    valid = False
    while not valid:
        # ask user for number and check if valid
        try:
            response = int(input(question))
            return response

        except ValueError:   # if integer is not present, print error
            print(error)


# checks string is valid
def string_check(choice, options):
    is_valid = ""
    chosen = ""
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


# get snacks
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


# check price based on age
def age_price():
    valid = False
    while not valid:
        age = int_check("Age: ", 12, 130)
        if age < 12:
            print("Sorry - You must be over the age of 11 to buy tickets")
            continue
        if age > 130:
            print("Sorry - You are too old, this looks like a mistake")
            continue
        # ticket price calculations go here
        if age < 16:
            price = 7.5
        elif age >= 65:
            price = 6.5
        else:
            price = 10.5
        return price


# show snack order
def order():
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
    return get_order


def ticket_display(names, count):
    if names != "xxx":
        count += 1
    tickets_left = max_tickets - count
    # display tickets sold and tickets left
    if tickets_left > 0:
        print("There are {} tickets left.".format
              (tickets_left))
        return count
    else:
        print("You have sold all the tickets!")


def payment_method():
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash or credit): ")
        how_pay = string_check(how_pay, pay_method)
        if how_pay == "invalid choice":
            print("please enter a valid option")
            continue
    # ask for subtotal (testing purposes)

    if how_pay == "Credit":
        charge = 0.05
        return charge
    else:
        charge = 0
        return charge


# ******** Main Routine ********
# set up dictionaries / lists needed to hold data
# import statements
max_tickets = 5
name = ""
profit = 0
ticket_count = 0

all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []

snack_lists = [popcorn, mms, pita_chips, water]

# store surcharge multipliers
surcharge_mult_list = []

pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Surcharge_Multiplier': surcharge_mult_list
}

price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
}
# ask user if they have used the program before and show instructions if necessary

# Loop to get tickets details
while ticket_count < max_tickets:
    # Get name (can't be blank)
    name = not_blank("Name: ")
    # exit code
    if name == "xxx":
        # print details
        movie_frame = pandas.DataFrame(movie_data_dict)
        movie_frame = movie_frame.set_index("Name")
        print()

        # Create column for snacks total
        movie_frame["Snacks"] = \
            movie_frame['Popcorn'] * price_dict['Popcorn'] + \
            movie_frame['Water'] * price_dict['Water'] + \
            movie_frame['Pita Chips'] * price_dict['Pita Chips'] + \
            movie_frame['M&Ms'] * price_dict['M&Ms']

        # create column called 'Sub total'
        movie_frame["Sub Total"] = \
            movie_frame['Ticket'] + \
            movie_frame['Snacks']

        movie_frame["Surcharge"] = \
            movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

        movie_frame["Total"] = movie_frame["Sub Total"] + \
            movie_frame["Surcharge"]

        movie_frame = movie_frame.rename(columns={'Pita Chips': 'Chips',
                                                  'Surcharge_Multiplier': 'SM'})
        pandas.set_option('display.max_columns', None)

        print_all = input("Print all columns? y for yes: ")
        if print_all == "y":
            print(movie_frame)
        else:
            print(movie_frame[['Ticket', 'Snacks', 'Sub Total', 'Surcharge', 'Total']])
            print()
        # Calculate total sales and profit
        print("Profit from tickets : ${:.2f}".format(profit))
        ticket_count = ticket_display(name, ticket_count)
        break
    # Get age ( between 12 and 130)
    ticket_price = age_price()
    profit_made = ticket_price - 5
    profit += profit_made

    # add names and ticket price to list
    all_names.append(name)
    all_tickets.append(ticket_price)

    print("{} : ${:.2f}".format(name, ticket_price))

    # Loop to ask for snacks
    total_order = order()

    # Calculate snack price

    for item in snack_lists:
        item.append(0)

    for item in total_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    count = 0
    for client_order in total_order:
        # assume no snacks have been bought

        # print snack lists
        # get order (hard coded for easy testing)
        snack_order = total_order[count]
        count += 1

    # ask for payment method ( and apply surcharge if necessary)
    surcharge = payment_method()
    surcharge_mult_list.append(surcharge)
    print(surcharge_mult_list)
    # display tickets left
    ticket_count = ticket_display(name, ticket_count)


# Output data to text files
