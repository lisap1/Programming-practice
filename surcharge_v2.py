import pandas


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


pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

name = ""
while name != "xxx":
    name = input("Name: ")
    if name == "xxx":
        break

    # ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash or credit): ")
        how_pay = string_check(how_pay, pay_method)
        if how_pay == "invalid choice":
            print("please enter a valid option")
            continue
    # ask for subtotal (testing purposes)
    subtotal = float(input("Sub total? $"))

    if how_pay == "Credit":
        surcharge = 0.05 * subtotal
    else:
        surcharge = 0

    total = subtotal + surcharge

    print("Name: {} | Subtotal: ${:.2f} | Surcharge: ${:.2f} |"
          "Total Payable: ${:.2f}".format(name, subtotal, surcharge, total))
