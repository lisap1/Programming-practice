# function goes here
def int_check(question, low_num, high_num):
    # error message
    error = "Please enter a whole number between {} and {}"\
        .format(low_num, high_num)
    valid = False
    while not valid:
        # ask user for number and check if valid
        try:
            response = int(input(question))

            if low_num <= response <= high_num:
                return response
            else:
                print(error)

        # if integer is not present, print error
        except ValueError:
            print(error)


# main routine goes here
int_check("Age: ", 12, 130)


