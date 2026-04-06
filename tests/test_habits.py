import sys
import os
from datetime import datetime, timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from habit import Habit
from analytics import (
    get_all_habits,
    get_habits_by_periodicity,
    longest_streak_for_habit,
    longest_streak_all
)
from db import (
    initialize_db,
    save_habit,
    load_habits,
    delete_habit,
    reset_database,
    create_predefined_habits
)


def setup_function():
    """
    Reset the database before each test for isolation.
    """
    reset_database()


def test_create_habit():
    habit = Habit("Drink Water", "daily")
    assert habit.name == "Drink Water"
    assert habit.periodicity == "daily"
    assert len(habit.completions) == 0


def test_edit_habit():
    habit = Habit("Drink Water", "daily")
    habit.edit(name="Drink More Water", periodicity="weekly")

    assert habit.name == "Drink More Water"
    assert habit.periodicity == "weekly"


def test_check_off_habit():
    habit = Habit("Exercise", "daily")
    habit.check_off("2026-03-01T10:00:00")
    assert len(habit.completions) == 1
    assert habit.completions[0] == "2026-03-01T10:00:00"


def test_save_and_load_habit():
    habit = Habit("Meditate", "daily")
    habit.check_off("2026-03-01T08:00:00")
    save_habit(habit)

    habits = load_habits()

    assert len(habits) == 1
    assert habits[0].name == "Meditate"
    assert habits[0].periodicity == "daily"
    assert len(habits[0].completions) == 1


def test_delete_habit():
    habit = Habit("Meditate", "daily")
    save_habit(habit)

    deleted = delete_habit("Meditate")
    habits = load_habits()

    assert deleted is True
    assert len(habits) == 0


def test_get_all_habits():
    h1 = Habit("Drink Water", "daily")
    h2 = Habit("Read Book", "weekly")
    habits = [h1, h2]

    result = get_all_habits(habits)
    assert result == ["Drink Water", "Read Book"]


def test_get_habits_by_periodicity():
    h1 = Habit("Drink Water", "daily")
    h2 = Habit("Read Book", "weekly")
    h3 = Habit("Exercise", "daily")
    habits = [h1, h2, h3]

    result = get_habits_by_periodicity(habits, "daily")
    assert len(result) == 2
    assert result[0].name == "Drink Water"
    assert result[1].name == "Exercise"


def test_get_habits_by_periodicity_no_match():
    h1 = Habit("Drink Water", "daily")
    h2 = Habit("Exercise", "daily")
    habits = [h1, h2]

    result = get_habits_by_periodicity(habits, "weekly")
    assert result == []


def test_longest_streak_for_daily_habit():
    habit = Habit("Exercise", "daily")

    habit.check_off("2026-03-01T10:00:00")
    habit.check_off("2026-03-02T10:00:00")
    habit.check_off("2026-03-03T10:00:00")

    assert longest_streak_for_habit(habit) == 3


def test_longest_streak_for_weekly_habit():
    habit = Habit("Call family", "weekly")

    habit.check_off("2026-03-01T10:00:00")
    habit.check_off("2026-03-08T10:00:00")
    habit.check_off("2026-03-15T10:00:00")

    assert longest_streak_for_habit(habit) == 3


def test_longest_streak_break_daily():
    habit = Habit("Read", "daily")

    habit.check_off("2026-03-01T10:00:00")
    habit.check_off("2026-03-02T10:00:00")
    habit.check_off("2026-03-05T10:00:00")

    assert longest_streak_for_habit(habit) == 2


def test_longest_streak_break_weekly():
    habit = Habit("Plan week", "weekly")

    habit.check_off("2026-03-01T10:00:00")
    habit.check_off("2026-03-08T10:00:00")
    habit.check_off("2026-03-22T10:00:00")

    assert longest_streak_for_habit(habit) == 2


def test_longest_streak_no_completions():
    habit = Habit("Journal", "daily")
    assert longest_streak_for_habit(habit) == 0


def test_longest_streak_all():
    h1 = Habit("Drink Water", "daily")
    h2 = Habit("Read Book", "daily")

    h1.check_off("2026-03-01T10:00:00")
    h1.check_off("2026-03-02T10:00:00")
    h1.check_off("2026-03-03T10:00:00")

    h2.check_off("2026-03-01T10:00:00")
    h2.check_off("2026-03-02T10:00:00")

    habits = [h1, h2]

    result = longest_streak_all(habits)
    assert result.name == "Drink Water"


def test_longest_streak_all_empty():
    assert longest_streak_all([]) is None


def test_create_predefined_habits():
    create_predefined_habits()
    habits = load_habits()

    assert len(habits) == 5

    daily_habits = [h for h in habits if h.periodicity == "daily"]
    weekly_habits = [h for h in habits if h.periodicity == "weekly"]

    assert len(daily_habits) == 3
    assert len(weekly_habits) == 2

    for habit in daily_habits:
        assert len(habit.completions) == 28

    for habit in weekly_habits:
        assert len(habit.completions) == 4