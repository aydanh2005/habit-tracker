# Habit Tracker CLI Application

This project is a command-line Habit Tracker application developed in Python using Object-Oriented Programming principles. The application allows users to create and manage habits, track their completion, and analyze habit streaks.

This project was developed as part of the IU International University portfolio project for the module:

DLBDSOOFPP01 – Object-Oriented and Functional Programming with Python

## Features

- Create and manage habits
- Track habit completion
- Analyze habit streaks
- View habits by periodicity (daily or weekly)
- Predefined habits for testing and demonstration
- Data stored using SQLite
- Unit testing implemented with pytest

## Technologies Used

- Python 3.11
- SQLite database
- pytest for unit testing
- Object-Oriented Programming (OOP)

## Project Structure

habit-tracker/
├── src/
│   ├── main.py        # CLI entry point of the application
│   ├── habit.py       # Habit class and habit logic
│   ├── db.py          # Database management
│   └── analytics.py   # Habit analysis functions
│
├── tests/
│   └── test_habits.py # Unit tests
│
└── README.md

## How to Run the Application

Clone the repository

git clone https://github.com/aydanh2005/habit-tracker.git

Navigate to the project folder

cd habit-tracker

Run the program

python src/main.py

## How to Use the Application

When the program starts, a menu appears in the terminal.

From the menu, you can:

- Create a new habit
- Delete a habit
- Check off a habit
- View all habits
- View habits by periodicity
- View the habit with the longest streak
- Load predefined habits
- Exit the program

To view only daily or weekly habits, choose the option:

View habits by periodicity

Then select the periodicity you want to display.

## Running Tests

To run the unit tests:

pytest

## Author

Aydan Huseynli

Created for the IU module  
DLBDSOOFPP01 – Object-Oriented and Functional Programming with Python
