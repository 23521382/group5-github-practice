import student
import utils


def show_menu():
    utils.print_header("STUDENT MANAGEMENT")
    print("  1. Add student")
    print("  2. Display all students")
    print("  3. Search student")
    print("  0. Exit")
    print("-" * 45)


def handle_add():
    utils.print_header("ADD STUDENT")
    student_id = utils.input_required("Student ID : ")
    full_name  = utils.input_required("Full name  : ")
    age        = utils.input_number("Age        : ", data_type=int)
    gpa        = utils.input_number("GPA        : ", data_type=float)

    if age is None or gpa is None:
        print("❌ Could not add student due to invalid input.")
        return

    student.add_student(student_id, full_name, age, gpa)


def handle_search():
    utils.print_header("SEARCH")
    keyword = utils.input_required("Enter name or student ID: ")
    student.search(keyword)


def main():
    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            handle_add()
        elif choice == "2":
            student.display_all()
        elif choice == "3":
            handle_search()
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option, please try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
