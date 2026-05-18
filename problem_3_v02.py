# Problem 3
# Using wheel factorization


def largest_p(num):

    max_prime = 0
    # Remove all powers of 2
    while num % 2 == 0:
        max_prime = 2
        num //= 2

    base_primes = [2, 3, 5]
    diffs = [2, 2, 4, 2, 4, 2, 4, 6, 2, 2]
    diff_index = 0
    factor = 3

    while factor**2 <= num:
        while num % factor == 0:
            max_prime = factor
            num //= factor

        factor += diffs[diff_index]
        diff_index += 1
        diff_index %= len(diffs)

    if num > 2:
        max_prime = num

    return max_prime


num = 13195
num = 600851475143
print(f"Largest prime factor of {num} is {largest_p(num)}")
