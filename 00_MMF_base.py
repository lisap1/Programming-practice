# import statements
ticket_count = 0
max_tickets = 5
name = ""
profit = 0


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


# ******** Main Routine ********


# set up dictionaries / lists needed to hold data

# ask user if they have used the program before and show instructions if necessary

# Loop to get tickets details

while ticket_count < max_tickets:
    # Get name (can't be blank)
    name = not_blank("Name: ")
    # exit code
    if name == "xxx":
        print("Profit from tickets : ${:.2f}".format(profit))
        break
    # Get age ( between 12 and 130)
    age = int_check("Age: ", 12, 130)
    if age < 12:
        print("Sorry - You must be over the age of 11 to buy tickets")
        continue
    if age > 130:
        print("Sorry - You are too old, this looks like a mistake")
        continue
    # ticket price calculations go here
    if age < 16:
        ticket_price = 7.5
    elif age >= 65:
        ticket_price = 6.5
    else:
        ticket_price = 10.5

    profit_made = ticket_price - 5
    profit += profit_made

    print("{} : ${:.2f}".format(name, ticket_price))

    # ticket_count tickets
    if name != "xxx":
        ticket_count += 1
    tickets_left = max_tickets - ticket_count
    # display tickets sold and tickets left
    if tickets_left > 0:
        print("You have sold {} tickets. \nThere are {} tickets left.".format
              (ticket_count, tickets_left))
    else:
        print("You have sold all the tickets!")

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # ask for payment method ( and apply surcharge if necessary)

# Calculate total sales and profit

# Output data to text files
