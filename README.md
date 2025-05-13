# Wordle Django

A web-based clone of the popular Wordle game, built with Django (Python) for the backend and HTML/JavaScript for the frontend.

## Features
- Random 5-letter word selection from a backend word list
- Secure, backend-driven game logic (solution is never exposed to the frontend)
- Color feedback matches official Wordle rules (handles duplicate letters)
- "New Game" button to start a fresh game
- Responsive, modern UI

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip

### Installation
```bash
# Clone the repository (if using version control)
cd ~/Documents/wordle_django

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python3 manage.py migrate

# Start the development server
python3 manage.py runserver
```
Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Project Structure
```
wordle_django/
├── game/
│   ├── templates/game/wordle.html
│   ├── views.py
│   ├── urls.py
│   └── ...
├── wordle_django/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── manage.py
└── requirements.txt
```

## How It Works
- **Backend:**
  - On first visit or "New Game," a random word is chosen and stored in the session.
  - Each guess is sent to the backend via AJAX, which checks the guess and returns color feedback.
  - The backend ensures the solution is never exposed until the game ends.
- **Frontend:**
  - Renders the board and handles user input.
  - Updates the board and messages based on backend responses.

## Customization
- **Add more words:**  Edit the `WORD_LIST` in `game/views.py`.
- **Change number of guesses:**  Update `MAX_GUESSES` in `game/views.py` and `maxGuesses` in the JS.
- **Improve UI:**  Edit `game/templates/game/wordle.html` (HTML/CSS/JS).

## License
MIT License

## Credits
- Inspired by the original [Wordle](https://www.nytimes.com/games/wordle/index.html)
- Built with Django 