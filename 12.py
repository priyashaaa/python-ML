def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("The sum of the digits of", num, "is", result)