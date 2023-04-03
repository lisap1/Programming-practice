import pandas

all_names = ['Rangi', 'Manaia', 'Talia', 'Arihi', 'Fetu']

popcorn = []
mms = []
pita_chips = []
water = []

snack_lists = [popcorn, mms, pita_chips, water]

movie_data_dict = {
    'Name': all_names,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
}

test_data = [
    [[2, 'Popcorn'], [1, 'Pita Chips']],
    [[]],
    [[3, 'Water']],
    [[1, 'Popcorn']],
    [[1, "M&Ms"], [2, 'Pita Chips']]
]

count = 0
for client_order in test_data:
    # assume no snacks have been bought
    for item in snack_lists:
        item.append(0)

    # print snack lists
    # get order (hard coded for easy testing)
    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

print()

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index("Name")
print(movie_frame)
