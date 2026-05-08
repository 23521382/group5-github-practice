class Student:
    def __init__(self, student_id, full_name, age, gpa):
        self.student_id = student_id
        self.full_name = full_name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        return f"[{self.student_id}] {self.full_name} | Age: {self.age} | GPA: {self.gpa}"


# In-memory student list
student_list = []


def add_student(student_id, full_name, age, gpa):
    """Add a new student to the list."""



def display_all():
    """Display all students in the list."""



def search(keyword):
    """Search for a student by name or student ID."""
