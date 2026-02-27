def power(base, exp):
    return base ** exp

def average(numbers_list):
    if not numbers_list:
        return 0
    return sum(numbers_list) / len(numbers_list)