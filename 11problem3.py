#self increament salary by 10% if salary < 10000
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increment_salary(self):
        if self.salary < 10000:
            self.salary *= 1.10  # Increase salary by 10%
        return self.salary
# Example usage:
emp = Employee("John Doe", 9000)
new_salary = emp.increment_salary()
print(f"New salary of {emp.name} is: {new_salary}")
