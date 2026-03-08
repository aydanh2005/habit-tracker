from datetime import datetime, timedelta


def get_all_habits(habits):
    """
    Return a list of all habit names.
    """
    return list(map(lambda h: h.name, habits))


def get_habits_by_periodicity(habits, periodicity):
    """
    Return habits with a specific periodicity.
    """
    return list(filter(lambda h: h.periodicity == periodicity, habits))


def _daily_streak(dates):
    if not dates:
        return 0

    longest = 1
    current = 1

    for i in range(1, len(dates)):
        if (dates[i] - dates[i - 1]).days == 1:
            current += 1
        else:
            current = 1
        longest = max(longest, current)

    return longest


def _weekly_streak(dates):
    if not dates:
        return 0

    week_starts = sorted({
        d - timedelta(days=d.weekday()) for d in dates
    })

    longest = 1
    current = 1

    for i in range(1, len(week_starts)):
        if (week_starts[i] - week_starts[i - 1]).days == 7:
            current += 1
        else:
            current = 1
        longest = max(longest, current)

    return longest


def longest_streak_for_habit(habit):
    """
    Calculate the longest streak for a given habit based on its periodicity.
    Daily habits require consecutive days.
    Weekly habits require consecutive weeks.
    """
    if not habit.completions:
        return 0

    dates = sorted({
        datetime.fromisoformat(timestamp).date()
        for timestamp in habit.completions
    })

    if habit.periodicity == "daily":
        return _daily_streak(dates)
    elif habit.periodicity == "weekly":
        return _weekly_streak(dates)

    return 0


def longest_streak_all(habits):
    """
    Return the habit with the longest streak.
    """
    if not habits:
        return None

    return max(habits, key=longest_streak_for_habit)