**Student Name:** Jumana Abufares
**Student Number:** 101 294 295

## Project Overview
The Student Management System is a Python application that connects to a PostgreSQL database and performs CRUD (Create, Read, Update, Delete) operations on student rows using SQL queries.
The application supports four functions:
- `getAllStudents()` – Execute a SELECT query to retrieve all rows from the students table.
- `addStudent()` – Execute an INSERT query to add a new row.
- `updateStudentEmail()` – Execute an UPDATE query to edit a student's email.
- `deleteStudent()` – Execute a DELETE query to remove a student row.

## Setup Instructions
1. Install Python and the required libraries: `pip install "psycopg[binary]" python-dotenv`
2. Connect to the Carleton University VPN when working off campus.
3. Set up a PostgreSQL database named `student_management` on the Carleton OpenStack instance.
4. Run the provided SQL script to create the `students` table and insert the initial rows.
5. Create a `.env` file in the project directory: `PASSWORD=postgresql_pwd`
6. Add a `.env` file in `.gitignore` to prevent uploading credentials to GitHub.

## Building and Running
**1: Start the SSH tunnel**
Open a Windows PowerShell terminal and run:
`ssh -N -o ExitOnForwardFailure=yes -L 127.0.0.1:5433:127.0.0.1:5432 student@134.117.131.55`
Enter your SSH password and keep terminal open.

**2: Run the application**
Open another PowerShell terminal, navigate to the folder containing `main.py`, and run: `python main.py`
The application connects to PostgreSQL through `localhost` on port `5433`.

Successful Connection:
When the application successfully connects to the PostgreSQL database, the following message is displayed:
	Starting DB connection...
	DB Connected!
	**demonstration video recording: https://drive.google.com/file/d/1nGx1lhhMGrgFTcSJaxXAyM2x0lmtRb7Y/view?usp=sharing**
