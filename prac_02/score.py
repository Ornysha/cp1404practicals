import random


def main():
    score = float(input("Enter score: "))
    while score >= 0:
        status = determine_status(score)
        print(f"{status}")
        score = float(input("Enter score: "))

    number_of_scores = int(input("How many random scores: "))
    for i in range(number_of_scores):
        score = random.randint(0, 100)
        status = determine_status(score)
        print(f"{score} = {status}")


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
