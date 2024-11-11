"""
CP1404/CP5632 Practical - Program to manage guitars.
Reads from a CSV file, allows user input, and saves back to the file.
"""

import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def load_guitars(filename):
    """Load guitars from a CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            name, year, cost = line
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars(filename, guitars):
    """Save a list of Guitar objects to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    """Main function to load, display, add, and save guitars."""
    guitars = load_guitars(FILENAME)

    # Display all loaded guitars
    print("These are the guitars loaded from file:")
    for guitar in guitars:
        print(guitar)

    # Sort guitars by year and display them
    guitars.sort()
    print("\nSorted guitars by year:")
    for guitar in guitars:
        print(guitar)

    # Allow user to add new guitars
    print("\nAdd your new guitars (press Enter to stop):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")

    # Save all guitars back to the CSV file
    save_guitars(FILENAME, guitars)
    print("\nGuitars have been saved to the file.")


if __name__ == "__main__":
    main()
