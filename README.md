# Flask Sign-In Application

This is a simple Flask-based sign-in application that uses an SQLite database to manage users, their passwords, and points. The application allows users to log in with their credentials and view their points.

## Features

- User authentication with username and password.
- Displays points for the logged-in user.
- Preloaded users for testing purposes.

## Dependencies

The project uses the following Python packages:

- **Flask**: A lightweight web framework.
- **Flask-SQLAlchemy**: Adds support for SQL databases.
  
All dependencies are managed via a virtual environment.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/SignIn_using_Flask.git
cd SignIn_using_Flask
```

### 2. Create a Virtual Environment
```bash
python3 -m virtualenv env
```

### 3. Activate the Virtual Environment
*On Linux/Mac:
```bash
source env/bin/activate
```

*On Windows:
```bash
.\env\Scripts\activate
```

### 4. Install Dependencies
```bash
pip3 install flask flask-sqlalchemy
```

### 5. Run the Application
```bash
python3 app.py
```
The application will start running at localhost:5000 on the browser.

## Testing Credentials

Here are some preloaded users you can use to test the login functionality:

| Username   | Password      | Points |
|------------|---------------|--------|
| JohnDoe    | password123   | 100    |
| JaneSmith  | password456   | 200    |
| Alice      | password789   | 300    |

## Project Structure

```bash
.
├── app.py               # Main application file
├── instance
│   └── site.db          # SQLite database
├── static
│   └── css
│       └── main.css     # CSS for styling
├── templates
│   ├── base.html        # Base template for the application
│   ├── home.html        # User info page
│   └── index.html       # Login page template
├── env/                 # Virtual environment (not pushed to repo)
├── requirements.txt     # List of Python dependencies (create if missing)
└── README.md            # This file
```



