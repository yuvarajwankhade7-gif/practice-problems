def add_message(cls):
    class NewClass(cls):
        def display(self):
            print("Welcome!")
            super().display()
    return NewClass

@add_message
class Student:
    def display(self):
        print("python class.")

# Create object
s = Student()
s.display()
