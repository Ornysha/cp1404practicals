"""
CP1404/CP5632 Practical - Project class for project management program.
"""

from datetime import datetime


class Project:
    """Class to represent a project with its details."""

    def __init__(self, name: str, start_date: str, priority: int, cost_estimate: float, completion_percentage: int):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self) -> str:
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Less-than operator for sorting projects by priority."""
        return self.priority < other.priority

    def is_complete(self) -> bool:
        """Return True if the project is complete (100% completion)."""
        return self.completion_percentage == 100

    def update_completion(self, new_completion: int):
        """Update the completion percentage."""
        self.completion_percentage = new_completion

    def update_priority(self, new_priority: int):
        """Update the priority level."""
        self.priority = new_priority
