from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import restaurant

# VISIBLE ROUTES
# Redirect from root path
@app.route('/')
def home():
    return redirect('/dojos')


# Dojos Page
@app.route('/dojos')
def dojos():
    return render_template('/new_dojo_all_dojos.html')


# Create Ninja page
@app.route('/create_ninja')
def create_ninja():
    return render_template('/new_ninja.html')


# View one Dojo and all it's Ninjas
@app.route('/show_dojo')
def show_dojo():
    return render_template('one_dojo.html')





# HIDDEN ROUTES

# Create Dojo
@app.route('/process_create_dojo')
def process_create_dojo():
    return redirect('/dojos')


# Create Ninja
@app.route('/process_create_ninja')
def create_ninja():
    return redirect('show_dojo')