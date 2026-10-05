class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


employee_list: list[Employee] = []

employee_list.append(Employee("John", 23, 50000))
employee_list.append(Employee("Mike", 45, 60000))
employee_list.append(Employee("Lisa", 33, 90000))
employee_list.append(Employee("Elon", 50, 100000))
employee_list.append(Employee("Jeff", 60, 120000))
employee_list.append(Employee("Bill", 70, 150000))


def get_all_employees_names():
    return [e.name for e in employee_list]


def get_maximum_salary():
    return max([e.salary for e in employee_list])


def get_salary_bigger_than(salary: int):
    return [e.name for e in employee_list if e.salary > salary]


print(f"All employees names: {get_all_employees_names()}")
print(get_maximum_salary())
print(get_salary_bigger_than(75000))
print(get_salary_bigger_than(105000))
