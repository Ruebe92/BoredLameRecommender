from flask import Flask, render_template, request
import ml_models
import pandas as pd
from cleanup import structure_ratings
from data_import import get_games

app = Flask(__name__)
# instantiating a Flask application
# "__name__" is a reference to the current script (application.py)



@app.route("/index")
@app.route("/")
def index():
    game_list = get_games(10)
    return render_template("index.html", games_html=game_list)

@app.route("/greet/<name>")
def greet(name):
    return render_template("greeting.html", name_html=name)

@app.route("/recommend")
def recommend():
    results = ml_models.simple_recommender(5)

    user_input = dict(request.args)

    df = structure_ratings(user_input, 'new_user')
    print(user_input)
    print(df)

    # results = ml_models.nmf_recommender(movies, ratings)

    return render_template("recommendations.html", results=results)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
