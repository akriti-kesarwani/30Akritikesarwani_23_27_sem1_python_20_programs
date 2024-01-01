class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}, Salary: {self.salary}")

    def work(self):
        print(f"{self.name} is working hard.")


class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, Grade: {self.grade}")

    def study(self):
        print(f"{self.name} is studying diligently.")


class PersonInfo(Employee, Student):
    def __init__(self, name, age, employee_id, salary, student_id, grade):
        # Call constructors of both parent classes
        Employee.__init__(self, name, age, employee_id, salary)
        Student.__init__(self, name, age, student_id, grade)

    def display_info(self):
        print("Person Information:")
        super().display_info()


# Example usage with user input:
name = input("Enter name: ")
age = int(input("Enter age: "))
employee_id = input("Enter employee ID: ")
salary = float(input("Enter salary: "))
student_id = input("Enter student ID: ")
grade = input("Enter grade: ")

person_info = PersonInfo(name=name, age=age, employee_id=employee_id, salary=salary, student_id=student_id, grade=grade)
person_info.display_info()
person_info.work()  # Call Employee method
person_info.study()  # Call Student method
