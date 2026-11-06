def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def main():
    numbers = [2, 5, 8, 10]

    total = 0
    for n in numbers:
        total += n

    product = 1
    for n in numbers:
        product *= n

    print("Numbers:", numbers)
    print("Sum:", total)
    print("Product:", product)
    print("Add 7 + 3:", add(7, 3))
    print("Multiply 6 * 4:", multiply(6, 4))


if __name__ == "__main__":
    main()
