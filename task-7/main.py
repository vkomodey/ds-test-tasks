import time
def devided_at(N, m):
    start = 10**(N - 1)
    end = 10**N
    amount = 0

    for value in range(start, end, 1):
        devided = value / m
        rounded = round(devided)

        if devided == rounded:
            amount = amount + 1

    return amount

result = devided_at(4, 20)
