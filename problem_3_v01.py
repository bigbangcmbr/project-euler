# Problem 3


def largest_p(num):

    max_prime = 0
    # Remove all powers of 2
    while num % 2 == 0:
        max_prime = 2
        num //= 2

    factor = 3
    while factor**2 <= num:
        while num % factor == 0:
            max_prime = factor
            num //= factor
        factor += 2

    if num > 2:
        max_prime = num
    return max_prime


num = 13195
num = 600851475143
print(f"Largest prime factor of {num} is {largest_p(num)}")
