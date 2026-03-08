import sqlite3
import json
import os
from datetime import datetime, timedelta
from habit import Habit


DB_NAME = os.path.join(os.path.dirname(__file__), "habit_tracker.db")


def get_connection():
    return sqlite3.connect(DB_NAME)


def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS habits (
        name TEXT PRIMARY KEY,
        periodicity TEXT,
        created_at TEXT,
        completions TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_habit(habit: Habit):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO habits (name, periodicity, created_at, completions)
    VALUES (?, ?, ?, ?)
    """, (
        habit.name,
        habit.periodicity,
        habit.created_at,
        json.dumps(habit.completions)
    ))

    conn.commit()
    conn.close()


def load_habits():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, periodicity, created_at, completions FROM habits")
    rows = cursor.fetchall()

    habits = []

    for row in rows:
        name, periodicity, created_at, completions = row
        completions = json.loads(completions)

        habit = Habit(
            name=name,
            periodicity=periodicity,
            created_at=created_at,
            completions=completions
        )

        habits.append(habit)

    conn.close()
    return habits


def delete_habit(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM habits WHERE LOWER(name) = LOWER(?)", (name,))
    deleted = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return deleted


def reset_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS habits")
    conn.commit()
    conn.close()
    initialize_db()


def create_predefined_habits():
    """
    Create predefined habits with 4 weeks of sample completion data.
    Completely resets old data first.
    """
    reset_database()

    habits = [
        Habit("Practice German vocabulary", "daily"),
        Habit("Work on AI/Python exercises", "daily"),
        Habit("Read 10 pages of a technical or non-fiction book", "daily"),
        Habit("Plan the next study week", "weekly"),
        Habit("Call a family member", "weekly")
    ]

    now = datetime.now()

    for habit in habits:
        if habit.periodicity == "daily":
            for i in range(28):
                completion_date = (now - timedelta(days=i)).isoformat()
                habit.check_off(completion_date)
        elif habit.periodicity == "weekly":
            for i in range(4):
                completion_date = (now - timedelta(weeks=i)).isoformat()
                habit.check_off(completion_date)

        save_habit(habit)

    print("Predefined habits with 4-week test data created successfully.")