"""Module for ML Algorithms"""

# TO-DO: Get movies from file or from database

from faker import Faker


def simple_recommender(num):
    fake = Faker()
    fake_names = [fake.name() for i in range(num)]
    return fake_names


def nmf_recommender():
    """Write your own code for NMF Here"""
    pass


def cosim_recommender():
    pass


if __name__ == "__main__":
    print(simple_recommender(5))