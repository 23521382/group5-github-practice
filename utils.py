def input_number(prompt, data_type=float):
    """Read a number from input; returns None if invalid."""
    try:
        return data_type(input(prompt))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        return None


def input_required(prompt):
    """Read a non-empty string from input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("⚠️ This field cannot be empty, please try again.")


def print_header(title):
    """Print a bordered section header."""
    width = 45
    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width)
