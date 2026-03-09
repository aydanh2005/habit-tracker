# Habit Tracker CLI Application

This project is a command-line Habit Tracker application developed in Python using Object-Oriented Programming principles. The application allows users to create and manage habits, track their completion, and analyze habit streaks.

This project was developed as part of the IU International University portfolio project for the module:

**DLBDSOOFPP01 – Object-Oriented and Functional Programming with Python**

---

## Features

- Create and manage habits  
- Track habit completion  
- Analyze habit streaks  
- View habits by periodicity (daily or weekly)  
- Predefined habits for testing and demonstration  
- Data stored using SQLite  
- Unit testing implemented with pytest  

---

## Technologies Used

- Python 3.11  
- SQLite database  
- pytest for unit testing  
- Object-Oriented Programming (OOP)  

---

## Project Structure

```text
habit-tracker/
├── src/
│   ├── main.py        # CLI entry point of the application
│   ├── habit.py       # Habit class and habit logic
│   ├── db.py          # Database management
│   └── analytics.py   # Habit analysis functions
├── tests/
│   └── test_habits.py # Unit tests
└── README.md

---


## How to Run the Application

Clone the repository:

git clone https://github.com/aydanh2005/habit-tracker.git

Navigate to the project folder:

cd habit-tracker

Run the application:

python src/main.py

---

## How to Use the Habit Tracker

After starting the program, a CLI menu will appear allowing you to manage habits.

You can perform the following actions:

Create a habit  
Enter a habit name and select its periodicity (daily or weekly).

Check off a habit  
Record the completion of a habit for the current period.

View all habits  
Display all stored habits and their details.

View habits by periodicity  
Filter habits to display only daily habits or only weekly habits.

Analyze habits  
Use the analytics functions to calculate habit streaks, including the longest streak.

Delete habits  
Remove habits from the tracker when they are no longer needed.

---

## Running Tests

To run the unit tests:

pytest

The tests verify the core functionality of the application, including habit creation, completion tracking, streak calculation, and database operations.

---

## Author

Aydan Huseynli

Created for the IU module  
DLBDSOOFPP01 – Object-Oriented and Functional Programming with Python
