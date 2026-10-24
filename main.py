# print("Hello!")
#
# name = "Rostuslav"
#
# print(name)
#
# age = 12
# print(age)
from tkinter.font import names


class Student:
    def __init__(self, name="Unknown", height=160):
        self.name = name
        self.height = height

    def grow(self, cm):
        self.height += cm
        print(f"{self.name} виріс! Зріст {self.height}")

    def __str__(self):
        return f"Student {self.name}, hes height - {self.height}"

    def __del__(self):
        print(f"Student {self.name} has been deleted")


Bob = Student("Bob", 150)
Kate = Student("Kate", 160)


Bob.grow(10)
print(Bob)
del Bob