To use this application:
1. Generate an API key from TMDB(https://developer.themoviedb.org/docs/getting-started)
2. Create a .env file in the same directory as main.py
3. Add the API key to the .env file using the variable API_KEY(i.e API_KEY = 1eq27nu3i1wsdioq213wd)
4. Run main.py
```markdown
# Movie Wishlist Web App(in-progress)


## Project Structure
/movie-wishlist-app
│
├── /app
│   ├── __init__.py          # Initialize your Flask app and configure it (database, TMDb API key, etc.)
│   ├── models.py            # Define your database models (e.g., Movie, User, etc.)
│   ├── auth.py              # Handle user authentication (login, logout, registration)
│   ├── /templates/          # HTML templates for rendering pages
│   │   ├── base.html        # Base template for common structure (e.g., navbar, footer)
│   │   ├── index.html       # Homepage that shows the user's movie wishlist
│   │   ├── search_results.html # Template for displaying search results
│   │   ├── add_movie.html   # Template for showing movie details when adding to wishlist (optional)
│   │   ├── login.html       # Template for user login
│   │   ├── register.html    # Template for user registration
│   │   └── update_progress.html # Template for updating progress of movies (optional)
│   ├── /static/             # Static files (CSS, JavaScript, images)
│   │   ├── /css/            # Custom CSS files
│   │   ├── /js/             # Custom JavaScript files (e.g., for AJAX search, form handling)
│   │   └── /img/            # Images (e.g., movie posters, icons)
│
├── /migrations/             # Database migrations (for Flask-Migrate if using migrations)
│
├── /instance/               # Configurations and secrets (e.g., API keys)
│   └── config.py            # Config file with sensitive details like TMDb API key
│
├── run.py                   # Entry point to start your Flask app
└── requirements.txt         # List of dependencies (Flask, SQLAlchemy, Flask-WTF, etc.)
