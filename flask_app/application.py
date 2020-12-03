from flask import Flask, render_template, request
import ml_models
import pandas as pd
from cleanup import structure_ratings

app = Flask(__name__)
# instantiating a Flask application
# "__name__" is a reference to the current script (application.py)




@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recommend")
def recommend():
    results = ml_models.simple_recommender(5)

    user_input = dict(request.args)
    df = structure_ratings(user_input, 'new_user')
    print(df)
        
    ### 1. Train your model (OR the model is already pre-trained)
    ### 2. Process the input, e.g. convert everything into numbers.... movie titles -> column numbers
    ### 3. Data Validation, e.g. spell check....
    ### 4. Convert the user input into an array of length of len(df.columns), ~9724
    ### 5. user_profile = nmf.transform(user_array). This user_profile is the "hidden feature profile" of the users for all hidden features
    ### 6. results = np.dot(user_profile, nmf.components_)
    ### 7. Sort the array, map the top N values to movie names
    ### 8. Return the titles. Also filter out movies the user has already seen.

    ##### BONUS: Insert new user data into the database.

    # results = ml_models.nmf_recommender(movies, ratings)

    return render_template("recommendations.html", results=results)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
