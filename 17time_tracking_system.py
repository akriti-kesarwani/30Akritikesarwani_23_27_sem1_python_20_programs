from datetime import datetime, timedelta

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

class Project:
    def __init__(self, project_id, name):
        self.project_id = project_id
        self.name = name
        self.time_entries = []

    def log_hours(self, employee, hours, date):
        time_entry = TimeEntry(employee, self, hours, date)
        self.time_entries.append(time_entry)

    def generate_timesheet(self, start_date, end_date):
        timesheet = {}
        for entry in self.time_entries:
            if start_date <= entry.date <= end_date:
                if entry.employee.name not in timesheet:
                    timesheet[entry.employee.name] = 0
                timesheet[entry.employee.name] += entry.hours
        return timesheet

class TimeEntry:
    def __init__(self, employee, project, hours, date):
        self.employee = employee
        self.project = project
        self.hours = hours
        self.date = date

class TimeTrackingSystem:
    def __init__(self):
        self.employees = []
        self.projects = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_project(self, project):
        self.projects.append(project)

    def calculate_overtime(self, employee):
        total_hours = sum(entry.hours for project in employee.projects for entry in project.time_entries)
        regular_hours = min(total_hours, 40)
        overtime_hours = max(total_hours - 40, 0)
        return regular_hours, overtime_hours

# Example Usage with Simplified Date Format:
if __name__ == "__main__":
    system = TimeTrackingSystem()

    # Adding employees
    employee_name1 = input("Enter the name of the first employee: ")
    employee1 = Employee(1, employee_name1)
    system.add_employee(employee1)

    employee_name2 = input("Enter the name of the second employee: ")
    employee2 = Employee(2, employee_name2)
    system.add_employee(employee2)

    # Adding projects
    project_name1 = input("Enter the name of the first project: ")
    project1 = Project(101, project_name1)
    system.add_project(project1)

    project_name2 = input("Enter the name of the second project: ")
    project2 = Project(102, project_name2)
    system.add_project(project2)

    # Logging hours for projects
    log_hours_input = input("Do you want to log hours? (yes/no): ").lower()
    while log_hours_input == 'yes':
        employee_id = int(input("Enter employee ID: "))
        project_id = int(input("Enter project ID: "))
        hours = float(input("Enter hours logged: "))
        date_str = input("Enter date (e.g., 2023-01-01): ")
        date = datetime.strptime(date_str, "%Y-%m-%d")

        employee = next((emp for emp in system.employees if emp.employee_id == employee_id), None)
        project = next((proj for proj in system.projects if proj.project_id == project_id), None)

        if employee and project:
            project.log_hours(employee, hours, date)
            print("Hours logged successfully!")
        else:
            print("Employee or project not found. Please try again.")

        log_hours_input = input("Do you want to log more hours? (yes/no): ").lower()

    # Generating timesheets
    start_date_str = input("Enter start date for timesheet (e.g., 2023-01-01): ")
    end_date_str = input("Enter end date for timesheet (e.g., 2023-01-31): ")
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    for project in system.projects:
        timesheet = project.generate_timesheet(start_date, end_date)
        print(f"Timesheet for {project.name}:", timesheet)

    # Calculating overtime
    employee_id_overtime = int(input("Enter employee ID to calculate overtime: "))
    employee_overtime = next((emp for emp in system.employees if emp.employee_id == employee_id_overtime), None)

    if employee_overtime:
        regular_hours, overtime_hours = system.calculate_overtime(employee_overtime)
        print(f"{employee_overtime.name} worked {regular_hours} regular hours and {overtime_hours} overtime hours.")
    else:
        print("Employee not found.")
