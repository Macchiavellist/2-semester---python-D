def generate_squares(N):
    for i in range(N + 1):
        yield i ** 2

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

def main():
    N = int(input("Enter a number N to generate squares: "))
    for square in generate_squares(N):
        print(square)

    n = int(input("\nEnter the value of n for even numbers: "))
    print(", ".join(map(str, even_numbers(n))))

    n = int(input("\nEnter the value of n for numbers divisible by 3 and 4: "))
    for number in divisible_by_3_and_4(n):
        print(number)

    a = int(input("\nEnter the starting number (a): "))
    b = int(input("Enter the ending number (b): "))
    for square in squares(a, b):
        print(square)

    n = int(input("\nEnter the starting number for countdown: "))
    for number in countdown(n):
        print(number)

main()
