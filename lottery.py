import random

min = 46
max = 49
quantity = 4


def get_numbers_ticket(min, max, quantity):

    list_lottery_numbers = list(range(min, max+1))

    if list_lottery_numbers and quantity < len(list_lottery_numbers):
        random_numbers = random.sample(list_lottery_numbers, quantity)
        return sorted(random_numbers)
    else:
        return []


print(get_numbers_ticket(min, max, quantity))
