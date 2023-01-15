from app import app
#python func to render templates from html
from flask import render_template
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/favorites')
def favorites():
    movies = ['Napoleon Dynamite', 'Scott Pilgrim vs. The World', 'Nutty Professor', 'Hero', 'Good Burger']
    return render_template('favorites.html', movies=movies)