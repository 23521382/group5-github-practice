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
    for s in student_list:
        if s.student_id == student_id:
            print(f"Error: Student ID '{student_id}' already exists!")
            return False

    new_student = Student(student_id, full_name, age, gpa)

    student_list.append(new_student)
    print(f"Successfully added: {full_name}")
    return True



def display_all():
    """Display all students in the list."""



def search(keyword):
    """Search for a student by name or student ID.

    Matches when `keyword` is a case-insensitive substring of the student's
    full name, or when it exactly equals the student's ID (case-insensitive).
    Prints matched students and returns a list of `Student` objects.
    """
    if keyword is None:
        print("⚠️ No search keyword provided.")
        return []

    kw = str(keyword).strip().lower()
    if not kw:
        print("⚠️ No search keyword provided.")
        return []

    matches = []
    for s in student_list:
        name = getattr(s, "full_name", "") or ""
        sid = str(getattr(s, "student_id", ""))
        if kw in name.lower() or kw == sid.lower():
            matches.append(s)

    if not matches:
        print(f"No students found for '{keyword}'.")
    else:
        print(f"Found {len(matches)} student(s):")
        for m in matches:
            print(m)

    return matches
