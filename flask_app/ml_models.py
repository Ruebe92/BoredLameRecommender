"""Module for ML Algorithms"""

# TO-DO: Get movies from file or from database

from faker import Faker


def simple_recommender(num):
    fake = Faker()
    fake_names = [fake.name() for i in range(num)]
    return fake_names


def nmf_recommender(user_input, no_of_recommendations):
    Id_input = json.load(open("game_ids.json"))
    user_ratings = pd.DataFrame(user_input, index=['DAU'], columns=Id_input.values())
    user_ratings = user_ratings.fillna(0)
    user_P = nmf_model.transform(user_ratings)
    user_R = pd.DataFrame(np.dot(user_P, nmf_model.components_), index=['DAU'], columns=Id_input.values())
    recommendations = user_R.drop(columns=user_input.keys())
    recommendations = recommendations.T.sort_values(by='DAU', ascending=False)
    return recommendations.iloc[:no_of_recommendations]

def cosim_recommender():
    pass


if __name__ == "__main__":
    print(simple_recommender(5))