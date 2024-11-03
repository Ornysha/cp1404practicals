class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar based on the current year."""
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50+ years old)."""
        return self.get_age() >= 50
