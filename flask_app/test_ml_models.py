import json
import pytest

import ml_models


@pytest.mark.parametrize('user_input', ['user1_input.json','user2_input.json','user3_input.json'])
def test_nmf_recommender_output_length(user_input):

    user_input = json.load(open(user_input))

    test_recommendation = ml_models.nmf_recommender(user_input,5)

    assert  len(test_recommendation) == 5




