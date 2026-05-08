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
    """Search for students by name or student ID.

    The search is case-insensitive and returns every student whose name
    contains the keyword or whose student ID matches it exactly.
    """
    if keyword is None:
        print("No search keyword provided.")
        return []

    search_text = str(keyword).strip().lower()
    if not search_text:
        print("No search keyword provided.")
        return []

    matches = [
        student
        for student in student_list
        if search_text in (getattr(student, "full_name", "") or "").lower()
        or search_text == str(getattr(student, "student_id", "")).lower()
    ]

    if matches:
        print(f"Found {len(matches)} student(s):")
        for student in matches:
            print(student)
    else:
        print(f"No students found for '{keyword}'.")

    return matches
