from flask_app import app #defines app
from flask_app.controllers import burgers, restaurants #defines routes

if __name__ == "__main__":
    app.run(debug=True)