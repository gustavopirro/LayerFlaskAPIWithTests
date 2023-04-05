from src.main.server import app
from src.model.config.db_config import db

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
    # initialize the app with the extension
    db.init_app(app)
