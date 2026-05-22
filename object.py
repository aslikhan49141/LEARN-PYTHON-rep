# object.py
# Simple object-oriented programming example in Python

class Person:
    """A basic Person class with name, age, and greeting behavior."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self._is_logged_in = False  # protected/internal attribute

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def login(self) -> None:
        self._is_logged_in = True

    def logout(self) -> None:
        self._is_logged_in = False

    def is_logged_in(self) -> bool:
        return self._is_logged_in


class Student(Person):
    """A Student extends Person with a student ID and grade point average."""

    def __init__(self, name: str, age: int, student_id: str, gpa: float) -> None:
        super().__init__(name, age)
        self.student_id = student_id
        self.gpa = gpa

    def study(self) -> str:
        return f"{self.name} is studying for exams."

    def get_report(self) -> str:
        return f"Student {self.name} (ID: {self.student_id}) has GPA {self.gpa:.2f}."


def main() -> None:
    alice = Person("Alice", 30)
    print(alice.greet())

    bob = Student("Bob", 20, "S12345", 3.75)
    print(bob.greet())
    print(bob.study())
    print(bob.get_report())

    print("Logged in before login:", bob.is_logged_in())
    bob.login()
    print("Logged in after login:", bob.is_logged_in())


if __name__ == "__main__":
    main()
        