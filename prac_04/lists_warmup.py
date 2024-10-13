numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] = 3 (first element)
# numbers[-1] = 2 (last element)
# numbers[3] = 1 (fourth element)
# numbers[:-1] = [3, 1, 4, 1, 5, 9] (all elements except the last)
# numbers[3:4] = [1] (sublist with the fourth element only)
# 5 in numbers = True (5 is in the list)
# 7 in numbers = False (7 is not in the list)
# "3" in numbers = False (string "3" is not the same as number 3)
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] (adding the numbers at the end of the list)

# Change the first element of numbers to "ten"
numbers[0] = "ten"
# Change the last element of numbers to 1
numbers[-1] = 1
# Print all the elements from numbers except the first two (slice)
print(numbers[2:])
# Print whether 9 is an element of numbers
print(9 in numbers)
