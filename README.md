💰 Personal Expense Tracker

A simple and practical Python-based Personal Expense Tracker that helps users record, organize, and monitor their daily expenses.

This project was developed as part of my Python programming practice to strengthen my understanding of functions, loops, data structures, file handling, and problem-solving.

📌 About the Project

Managing daily expenses is an important part of personal finance. The Personal Expense Tracker provides a simple command-line application for recording expenses and understanding spending habits.

Users can add expenses, view saved records, calculate total spending, analyze category-wise expenses, and delete records when needed.

Expense data is stored locally in a JSON file, allowing records to remain available after the application is closed.

✨ Features

- Add a new expense.
- View all recorded expenses.
- Calculate total spending.
- View category-wise expense summaries.
- Delete an expense using its ID.
- Automatically record the current date.
- Save expense records in a JSON file.
- Handle invalid amounts and menu inputs.
- Preserve saved data between program runs.

🛠️ Technologies Used

- Python 3
- JSON
- Python Standard Library

🧠 Concepts Practiced

- Variables and data types
- Functions
- Conditional statements
- While loops
- Lists and dictionaries
- User input and type conversion
- File handling
- JSON data storage
- Exception handling
- Date and time handling
- Basic problem-solving

📂 Project Structure

Personal-Expense-Tracker/
│
├── expense_tracker.py
├── expenses.json
└── README.md

File descriptions:

- "expense_tracker.py" — Main application.
- "expenses.json" — Local file used to store expense records.
- "README.md" — Project documentation.

The JSON file is created automatically if it does not exist.

⚙️ Requirements

- Python 3 installed on your computer.
- Visual Studio Code or another Python-compatible editor.

No external Python packages are required.

🚀 How to Run

1. Clone the repository

Replace "YOUR-USERNAME" with your GitHub username and use the exact repository name.

git clone https://github.com/katyayniyadav18/Personal-expense-tracker.git

2. Open the project folder

cd Personal-Expense-Tracker

3. Run the application

python expense_tracker.py

If your system uses the "python3" command, run:

python3 expense_tracker.py

🎮 How to Use

When you run the program, the following menu appears:

===================================
       PERSONAL EXPENSE TRACKER
===================================
1. Add Expense
2. View All Expenses
3. View Total Expenses
4. Category-wise Summary
5. Delete Expense
6. Exit
===================================

Enter the number corresponding to the action you want to perform.

Example

Suppose you record these expenses:

Category| Amount
Food| ₹100
Travel| ₹50
Shopping| ₹200
Total| ₹350

The application calculates the total spending as ₹350.

💾 Data Storage

Expenses are stored locally in "expenses.json" in JSON format.

Each record contains:

- Expense ID
- Amount
- Category
- Description
- Date

This makes it possible to retrieve saved expenses when the program runs again.

🔮 Future Improvements

Possible improvements for future versions include:

- Monthly expense reports
- Budget setting and tracking
- Search expenses by category or date
- Export reports to CSV
- Graphs and spending visualizations
- A graphical user interface using Tkinter
- A web-based dashboard using HTML, CSS, and JavaScript

🎯 Learning Objective

The main goal of this project is to practice Python programming through a useful real-world application while developing logical thinking and data management skills.

👩‍💻 Author

Katyayni Yadav

Aspiring developer | Python learner| Exploring AI/ML and Data Science

⭐ Acknowledgment

This project is part of my continuous learning journey in Python programming and software development.

If you find this project useful, feel free to explore the code and suggest improvements.
