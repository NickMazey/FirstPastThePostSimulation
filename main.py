import numpy as np
import utilities.generator as generator
from utilities.voter import Voter
import matplotlib.pyplot as plot


def main():
    number_of_parties = 8
    parties = []
    for i in range(number_of_parties):
        parties.append(i)
    number_of_voters = 10000
    voters = generator.generate_voters(number_of_voters, parties)
    election_number = 100
    previous_election_result = {party: number_of_voters for party in parties}
    for i in range(election_number):
        to_remove = []
        for party in parties:
            if previous_election_result[party] < len(voters) / 100:
                to_remove.append(party)
        for party in to_remove:
            parties.remove(party)

        election_result = {party: 0 for party in parties}
        for voter in voters:
            election_result[voter.vote(parties, previous_election_result)] += 1
        previous_election_result = election_result
        fig = plot.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('equal')
        values = [election_result[party] for party in parties]
        ax.pie(values, labels=parties, autopct='%1.2f%%')
        plot.pause(5)
        plot.close(1)


if __name__ == '__main__':
    main()
