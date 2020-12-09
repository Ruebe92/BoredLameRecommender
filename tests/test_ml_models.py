import json
import pytest

from flask_app import ml_models


@pytest.mark.parametrize('user_input', ['tests/user1_input.json','tests/user2_input.json','tests/user3_input.json'])
def test_nmf_recommender_output_length(user_input):

    user_input = json.load(open(user_input))

    test_recommendation = ml_models.nmf_recommender(user_input,5, path = "flask_app/")

    assert  len(test_recommendation) == 5




