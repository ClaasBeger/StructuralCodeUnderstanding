class Employee:
    def __init__(self, id=0, first_name="", last_name="", salary=0):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._salary = salary

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary

    def get_name(self):
        return f"{self._first_name} {self._last_name}"

    def get_annual_salary(self):
        return self._salary * 12

    def raise_salary(self, percent):
        self._salary += (self._salary * percent) // 100
        return self._salary

    def __str__(self):
        return f"Employee[id={self._id}, name={self._first_name} {self._last_name}, salary={self._salary}]"


# Test the Employee class
if __name__ == "__main__":
    # Test constructor and __str__()
    e1 = Employee(8, "Peter", "Tan", 2500)
    print(e1)  # __str__()

    # Test Setters and Getters
    e1.set_salary(999)
    print(e1)  # __str__()
    print("id is:", e1.get_id())
    print("firstname is:", e1.get_first_name())
    print("lastname is:", e1.get_last_name())
    print("salary is:", e1.get_salary())

    print("name is:", e1.get_name())
    print("annual salary is:", e1.get_annual_salary())  # Test method

    # Test raise_salary()
    print(e1.raise_salary(10))
    print(e1)