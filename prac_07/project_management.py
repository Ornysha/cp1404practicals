"""
CP1404/CP5632 Practical - Project management program.
"""
from datetime import datetime
from project import Project

FILENAME = "projects.txt"


def load_projects(filename):
    """Load projects from a tab-delimited file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip the header line
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
    return projects


def save_projects(filename, projects):
    """Save projects to a tab-delimited file."""
    with open(filename, 'w', newline='') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display completed and incomplete projects."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in sorted(completed_projects):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter projects by a start date provided by the user."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]

    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(f"  {project}")


def add_new_project(projects):
    """Add a new project based on user input."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Update an existing project's completion and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    chosen_project = projects[project_choice]

    new_completion = input("New Percentage: ")
    if new_completion:
        chosen_project.update_completion(int(new_completion))

    new_priority = input("New Priority: ")
    if new_priority:
        chosen_project.update_priority(int(new_priority))


def main():
    """Main function to run the project management program."""
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu_options = {
        'L': "Load projects",
        'S': "Save projects",
        'D': "Display projects",
        'F': "Filter projects by date",
        'A': "Add new project",
        'U': "Update project",
        'Q': "Quit"
    }

    choice = ""
    while choice != 'Q':
        print("\nMenu options:")
        for key, description in menu_options.items():
            print(f"- ({key}) {description}")

        choice = input(">>> ").upper()

        if choice == 'L':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            save = input(f"Would you like to save to {FILENAME}? (y/n): ").lower()
            if save == 'y':
                save_projects(FILENAME, projects)
            print("Thank you for using the project management program.")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
