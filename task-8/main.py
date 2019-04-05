M = 1788888924

def num_of_digits(order):
    num = 0

    for i in range(order):
        num = num + 9 * 10**i * (i + 1)

    return num

def num_of_pages(order):
    num = 0

    for i in range(order):
        num = num + 9 * 10**i

    return num

def calc_N(M):
    right_digits_bound = 0
    right_index = 0

    while M >= right_digits_bound:
        right_digits_bound = num_of_digits(right_index)

        right_index = right_index + 1

    right_index = right_index - 1
    left_index = right_index - 1

    left_digits_bound = num_of_digits(left_index)
    left_pages_bound = num_of_pages(left_index)

    normalized_digits_count = M - left_digits_bound

    pages_count = normalized_digits_count / right_index

    result = left_pages_bound + pages_count

    return result
    
print(calc_N(M))
