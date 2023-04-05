from src.main.server import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
