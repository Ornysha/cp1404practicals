# Line 1 (random.randint(5, 20)):
# Observed values: [12, 6, 7, 16, 9]
# Smallest possible number: 5
# Largest possible number: 20
# Line 2 (random.randrange(3, 10, 2)):
# Observed values: [7, 7, 3, 7, 5]
# Smallest possible number: 3
# Largest possible number: 9
# Could it have produced a 4? No, because the step is 2, so only odd numbers (3, 5, 7, 9) are possible.
# Line 3 (random.uniform(2.5, 5.5)):
# Observed values: [4.8321, 4.2422, 4.9659, 3.6590, 3.4954]
# Smallest possible number: 2.5
# Largest possible number: 5.5
import random
print(random.randint(1, 100))