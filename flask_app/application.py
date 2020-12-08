from flask import Flask, render_template, request
import ml_models
import pandas as pd
# from cleanup import structure_ratings
from data_import import get_games

app = Flask(__name__)
# instantiating a Flask application
# "__name__" is a reference to the current script (application.py)

NUMBER_OF_GAMES = 12
NUMBER_OF_RECOM = 4

@app.route("/index")
@app.route("/")
def index():
    
    game_list, image_list = get_games('rank',NUMBER_OF_GAMES)

    return render_template("index.html", games_html= zip(game_list, image_list))

@app.route("/greet/<name>")
def greet(name):
    return render_template("greeting.html", name_html=name)

@app.route("/recommend")
def recommend():
    results = ml_models.simple_recommender(5)

    user_input = dict(request.args)

    results = ml_models.nmf_recommender(user_input, NUMBER_OF_RECOM)

    return render_template("recommendations.html", results=results)


if __name__ == "__main__":

    app.run(debug=True, port=5000)
