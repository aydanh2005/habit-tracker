from habit import Habit
from db import initialize_db, save_habit, load_habits, delete_habit, create_predefined_habits
from analytics import (
    get_all_habits,
    get_habits_by_periodicity,
    longest_streak_all,
    longest_streak_for_habit
)


def show_menu():
    print("\nHabit Tracker")
    print("1. Create a new habit")
    print("2. Delete a habit")
    print("3. Check off a habit")
    print("4. View all habits")
    print("5. View habits by periodicity")
    print("6. View habit with longest streak")
    print("7. Load predefined habits")
    print("8. Exit")


def create_habit():
    name = input("Enter habit name: ")
    periodicity = input("Enter periodicity (daily/weekly): ").lower()

    if periodicity not in ["daily", "weekly"]:
        print("Invalid periodicity. Please enter 'daily' or 'weekly'.")
        return

    habit = Habit(name, periodicity)
    save_habit(habit)
    print(f"Habit '{name}' created successfully.")


def remove_habit():
    name = input("Enter the name of the habit to delete: ")
    deleted = delete_habit(name)

    if deleted:
        print(f"Habit '{name}' deleted successfully.")
    else:
        print("Habit not found.")


def check_off_habit():
    habits = load_habits()
    name = input("Enter the name of the habit to check off: ")

    for habit in habits:
        if habit.name.lower() == name.lower():
            habit.check_off()
            save_habit(habit)
            print(f"Habit '{habit.name}' checked off successfully.")
            return

    print("Habit not found.")


def view_all_habits():
    habits = load_habits()
    names = get_all_habits(habits)

    if not names:
        print("No habits found.")
        return

    print("\nAll habits:")
    for name in names:
        print(f"- {name}")


def view_by_periodicity():
    habits = load_habits()
    periodicity = input("Enter periodicity (daily/weekly): ").lower()

    filtered = get_habits_by_periodicity(habits, periodicity)

    if not filtered:
        print(f"No {periodicity} habits found.")
        return

    print(f"\n{periodicity.capitalize()} habits:")
    for habit in filtered:
        print(f"- {habit.name}")


def view_longest_streak():
    habits = load_habits()
    longest = longest_streak_all(habits)

    if not longest:
        print("No habits available.")
        return

    streak = longest_streak_for_habit(longest)

    print("\nHabit with longest streak:")
    print(f"{longest.name} ({streak} consecutive {longest.periodicity} periods)")


def main():
    initialize_db()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            create_habit()
        elif choice == "2":
            remove_habit()
        elif choice == "3":
            check_off_habit()
        elif choice == "4":
            view_all_habits()
        elif choice == "5":
            view_by_periodicity()
        elif choice == "6":
            view_longest_streak()
        elif choice == "7":
            create_predefined_habits()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()