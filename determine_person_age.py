from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        birth_date = datetime.strptime(self.date_of_birth, '%Y-%m-%d')
        current_date = datetime.now()
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
        return age

# Get user input for person details
name = input("Enter the person's name: ")
country = input("Enter the person's country: ")
date_of_birth = input("Enter the person's date of birth (YYYY-MM-DD): ")

# Create a Person object with the provided details
person = Person(name, country, date_of_birth)

# Display the person's age
print(f"{person.name} is {person.calculate_age()} years old.")
