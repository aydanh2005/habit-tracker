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


def test_create_habit():
    habit = Habit("Drink Water", "daily")
    assert habit.name == "Drink Water"
    assert habit.periodicity == "daily"
    assert len(habit.completions) == 0


def test_check_off_habit():
    habit = Habit("Exercise", "daily")
    habit.check_off()
    assert len(habit.completions) == 1


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


def test_longest_streak_for_daily_habit():
    habit = Habit("Exercise", "daily")
    base = datetime.now()

    habit.check_off((base - timedelta(days=2)).isoformat())
    habit.check_off((base - timedelta(days=1)).isoformat())
    habit.check_off(base.isoformat())

    assert longest_streak_for_habit(habit) == 3


def test_longest_streak_for_weekly_habit():
    habit = Habit("Call family", "weekly")
    base = datetime.now()

    habit.check_off((base - timedelta(weeks=2)).isoformat())
    habit.check_off((base - timedelta(weeks=1)).isoformat())
    habit.check_off(base.isoformat())

    assert longest_streak_for_habit(habit) == 3


def test_longest_streak_break_daily():
    habit = Habit("Read", "daily")
    base = datetime.now()

    habit.check_off((base - timedelta(days=4)).isoformat())
    habit.check_off((base - timedelta(days=3)).isoformat())
    habit.check_off(base.isoformat())

    assert longest_streak_for_habit(habit) == 2


def test_longest_streak_all():
    h1 = Habit("Drink Water", "daily")
    h2 = Habit("Read Book", "daily")
    base = datetime.now()

    h1.check_off((base - timedelta(days=2)).isoformat())
    h1.check_off((base - timedelta(days=1)).isoformat())
    h1.check_off(base.isoformat())

    h2.check_off((base - timedelta(days=1)).isoformat())
    h2.check_off(base.isoformat())

    habits = [h1, h2]

    result = longest_streak_all(habits)
    assert result.name == "Drink Water"