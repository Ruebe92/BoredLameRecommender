import json
import ml_models

def test_nmf_recommender_output_length():

    user_input = json.load(open('user2_input.json'))

    test_recommendation = ml_models.nmf_recommender(user_input,5)

    assert  len(test_recommendation) == 5


