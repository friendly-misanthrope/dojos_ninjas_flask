from flask_app import app #defines app
from flask_app.controllers import dojos_ninjas #defines routes

if __name__ == "__main__":
    app.run(debug=True)