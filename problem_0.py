# Problem 0


def solve(n):
    sum = 0
    for i in range(int(n / 2)):
        sum += (2 * i + 1) ** 2

    return sum


def main():
    n = 754000
    ans = solve(n)
    print(f"Sum of odd squares is {ans}")


if __name__ == "__main__":
    main()
