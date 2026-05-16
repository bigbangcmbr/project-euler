# Problem 2


def fib(n):
    # Generate n'th fib

    if n <= 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n):
        b = a + b
        a = b - a

    return a + b


i = 0
n = fib(i)
sum = 0

while n < (4000000):
    i += 1
    n = fib(i)
    if n % 2 == 0:
        sum += n

print(
    f"Sum of even valued fibonacci terms, whose value do not exceed 4 million is: {sum}"
)
