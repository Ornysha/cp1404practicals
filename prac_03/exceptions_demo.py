try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
# 1. when we give anything other than a value , like any alphabet or simbols or nothing at all in the place of numerator or denominator, the ValueError will occur.
# 2. when the denominator is 0, the ZeroDivisionError will occur.
# 3.
