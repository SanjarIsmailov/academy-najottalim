# Academy Attendance Management System

## Overview
The **Academy Attendance Management System** is a Django-based web application designed to track and manage student attendance. The system allows administrators to mark student attendance, view attendance records, and manage student groups.

## Features
- Display all students with attendance status.
- Mark attendance using red/green buttons.
- Select a group and mark attendance for multiple students.
- Predefined 12 lessons for each student.

## Technologies Used
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL (configurable)
- **Frontend:** HTML, CSS, JavaScript (optional for dynamic UI)
- **Authentication:** Custom user model with `phone_number` and `date_of_birth`

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/academy-attendance.git
cd academy-attendance
```

### 2. Create and Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
python manage.py migrate
```

### 5. Create a Superuser (Admin Account)
```sh
python manage.py createsuperuser
```

### 6. Run the Server
```sh
python manage.py runserver
```
Access the system at `http://127.0.0.1:8000/`.

## Usage
1. **Login** using admin credentials.
2. **View student list** and manage attendance.
3. **Select a group** and mark attendance in bulk.
4. **Generate reports** (if implemented).

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License.
