import random
from utilities.voter import Voter


def generate_voters(number, parties):
    """
    A method to generate a number of voters
    :param number: the number of voters to generate
    :param parties: a numpy array of the available parties
    :return: a numpy array of voters
    """
    voters = [0 for i in range(number)]
    for i in range(number):
        voters[i] = Voter(generate_preferences(parties))
    return voters


def generate_preferences(parties):
    first_half = []
    second_half = []
    for i in range(len(parties)):
        if i < len(parties) / 2:
            first_half.append(parties[i])
        else:
            second_half.append(parties[i])

    if random.randint(0, 1) == 0:
        random.shuffle(first_half)
        return first_half.copy()
    else:
        random.shuffle(second_half)
        return second_half.copy()
