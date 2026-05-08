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
    if not student_list:
        print("\n[!] Hiện chưa có sinh viên nào trong danh sách.")
        return

    print(f"\n{'ID':<10} | {'Full Name':<20} | {'Age':<5} | {'GPA':<5}")
    print("-" * 45)

    for s in student_list:
        print(f"{s.student_id:<10} | {s.full_name:<20} | {s.age:<5} | {s.gpa:<5}")


def search(keyword):
    """Search for a student by name or student ID."""
