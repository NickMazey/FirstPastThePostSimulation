import random


class Voter:
    """
    Represents voters in the election
    Every voter has a list of party preferences
    """

    def __init__(self, preferences):
        self.preferences = preferences

    def vote(self, parties, previous_election_result):
        """
        Method to determine how the voter votes
        :param parties: the available parties to vote on
        :param previous_election_result: the result of the last election
        :return: the party the voter has chosen
        """
        for party in self.preferences:
            if party not in parties:
                self.preferences.remove(party)

        winning_party = -1
        for party in previous_election_result:
            if winning_party == -1:
                winning_party = party
            elif previous_election_result[party] > previous_election_result[winning_party]:
                winning_party = party

        if winning_party != self.preferences[0]:
            for party in self.preferences:
                if previous_election_result[party] > previous_election_result[self.preferences[0]]:
                    return party

        return self.preferences[0]
