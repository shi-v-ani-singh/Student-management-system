# Student Management System 🏫

A Python GUI application built using Tkinter that allows users to manage student records with a MySQL database. The system provides functionalities to add, view, and delete student records, all within an easy-to-use graphical interface.

## Features ✨
- Add new student records with details like name, email, contact, gender, date of birth, and stream.
- Display all student records in a tabular format with the option to scroll.
- Delete selected student records from the database.
- Reset the input fields after data entry.
- Real-time data manipulation and storage using a MySQL database.

## Tech Stack 🛠️
- **Python** (for the backend logic)
- **Tkinter** (for the GUI)
- **MySQL** (for the database)

## Prerequisites 📦
- Python 3.x
- MySQL server
- Required Python packages:
  - `mysql-connector-python`
  - `tkcalendar`
  - `tkinter`

## Installation and Setup ⚙️

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-management-system.git
   cd student-management-system
   ```

2. Install the required packages:
   ```bash
   pip install mysql-connector-python tkcalendar
   ```

3. Set up your MySQL database:
   - Create a MySQL database:
     ```sql
     CREATE DATABASE kryptora2;
     ```
   - The system will automatically create the required `STUDENT_MANAGEMENT` table when run for the first time.

4. Run the application:
   ```bash
   python student_management_system.py
   ```

## Screenshots 📸
![sms](https://github.com/user-attachments/assets/a2a06964-67ad-4686-85b9-8c3c3c73bc1d)


## Functionality 🖥️
- **Add Record**: Allows the user to input student details (name, email, contact, gender, DOB, and stream) and add them to the database.
- **Delete Record**: Removes the selected student entry from the database and the GUI table.
- **Clear Record**: Resets all input fields to default values.
- **Remove DB**: Clears the displayed data from the table view without affecting the database.

