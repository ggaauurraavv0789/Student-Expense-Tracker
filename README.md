# Student Expense Tracker

## Overview :

A simple Python command-line project for managing daily expenses.

I made this project mainly for students who want to keep track of how much they spend and compare their spending with a monthly budget.

## Features :

* Add an expense
* View all expenses
* Delete an expense
* Set a monthly budget
* Check the remaining budget
* View a spending report
* Save expenses in a JSON file

## Technologies Used :

* Python
* JSON
* Command Line Interface (CLI)

## Project Structure :

* `main.py` - runs the main menu
* `expenses.py` - handles adding, viewing and deleting expenses
* `budget.py` - handles the budget
* `reports.py` - generates the spending report
* `data.py` - saves and loads expense data

## How to Run :

1. Open the project folder in Command Prompt.
2. Make sure Python is installed.
3. Run:

py main.py

4. Choose an option from the menu.

## How It Works :

The program shows a menu with different options. I can add expenses, view or delete them, set a budget and check how much money is left.

The expenses are stored in a JSON file, so they can be loaded again when the program is started.

## Testing :

I tested the main options of the program by adding expenses, viewing them, deleting them, setting a budget and generating the spending report.

I also restarted the program to check whether the saved expenses were loaded correctly.

## Future Improvements :

* Add dates to expenses
* Add monthly reports
* Add graphs
* Add search and filtering
