
# URL Shortener Service

This is a simple URL shortening service built with Django. It allows users to create short URLs from long ones and provides functionality to redirect the user from a short URL to the original long URL. Additionally, the service tracks the number of times each short URL has been visited.

## Screenshot
![url](https://github.com/user-attachments/assets/11240624-9ac5-4a2a-86c7-0e5f0d1578f0)

## Features

- **Create Short URL**: Input a long URL and generate a shortened version.
- **Redirect**: Automatically redirect users to the original URL when they visit the short URL.
- **URL Hit Counter**: Keep track of how many times each short URL has been accessed.
- **Copy to Clipboard**: Easily copy the shortened URL to the clipboard after generating it.

## Technologies Used

- **Django**: The core web framework used for building the service.
- **SQLite**: The default database for development.
- **HTML/CSS/JavaScript**: Used for building the frontend with form handling and clipboard copy functionality.

## Setup Instructions

Follow these steps to set up the project locally:

### 1. Clone the repository
```bash
git clone <repo>
cd url_shortener
```

### 2. Create and activate a virtual environment
You can use `venv` to create a virtual environment for the project:
```bash
python -m venv env
env\Scripts\activate  # On Windows
```

### 3. Install required dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Run the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to access the URL Shortener.

## Usage

1. Enter a long URL in the input box.
2. Click "Shorten" to generate a short URL.
3. The short URL will be displayed, and you can copy it to the clipboard by clicking the "Copy Short URL to Clipboard" button.
4. Use the short URL to automatically redirect to the original URL.
5. The hit counter will track the number of times the short URL has been accessed.

## Project Structure

```
url_shortener/
│
├── shortener/
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates for the app
│   ├── static/             # CSS and JavaScript files
│   ├── views.py            # Core view logic for URL shortening and redirection
│   ├── models.py           # Database models
│   └── urls.py             # URL routing
│
├── manage.py               # Django project management
├── db.sqlite3              # SQLite database (created after migration)
└── requirements.txt        # Python dependencies
```


