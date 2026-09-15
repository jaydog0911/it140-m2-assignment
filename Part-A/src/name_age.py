"""Gets a person's name and age and figures out their approximate birth year.

Input:
    The person's name is a string entered by the user.
    The person's age is an integer entered by the user.
    

Process:
    Subtract the person's age from the current year to figure out their approximate birth year.

Output:
    A message with the person's name and approximate birth year is displayed on the screen.

Typical usage example:
    Enter your name: Jason
    Enter your age: 46
    Hello Jason, you were approximately born in 1980.
"""
# === Imports ===
from datetime import date


# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name? ")
    age = int(input("What is your age? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"Hello {name}, you were approximately born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===


