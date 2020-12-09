import json
import pytest

from flask_app import ml_models


@pytest.mark.parametrize('user_input', ['user1_input.json','user2_input.json','user3_input.json'])
def test_nmf_recommender_output_length(user_input):

    user_input = json.load(open(user_input))

    test_recommendation = ml_models.nmf_recommender(user_input,5, model_path = "flask_app/nmf_model.sav", game_ids_path = "flask_app/game_ids.json")

    assert  len(test_recommendation) == 5




