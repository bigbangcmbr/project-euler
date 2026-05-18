# Problem 3


def is_prime(n):

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def largest_p(num):
    max_prime = 1

    for i in range(2, num):
        if num % i == 0 and is_prime(i):
            max_prime = i
    return max_prime


num = 600851475143
print(f"Largest prime factor of {num} is {largest_p(num)}")
