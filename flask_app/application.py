from flask import Flask, render_template, request
import ml_models
import pandas as pd
from data_import import get_games, get_images_from_game_list

app = Flask(__name__)

NUMBER_OF_GAMES = 12
NUMBER_OF_RECOM = 4
RANKING_TYPE = 'num_user_ratings'
MODEL = "NMF" # "NMF" or "CoSim"

@app.route("/index")
@app.route("/")
def index():
    
    game_list, image_list = get_games(RANKING_TYPE,NUMBER_OF_GAMES)

    return render_template("index.html", games_html= zip(game_list, image_list))

@app.route("/greet/<name>")
def greet(name):

    return render_template("greeting.html", name_html=name)

@app.route("/recommend")
def recommend():

    user_input = dict(request.args)
    
    if MODEL == "NMF":
        game_list = ml_models.nmf_recommender(user_input, NUMBER_OF_RECOM)
    if MODEL == "CoSim":
        game_list = ml_models.cosim_recommender(user_input, NUMBER_OF_RECOM)

    image_list = get_images_from_game_list(game_list)

    return render_template("recommendations.html", results_html = zip(game_list, image_list))


if __name__ == "__main__":

    app.run(debug=True, port=5000)
