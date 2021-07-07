import numpy as np
import utilities.generator as generator
from utilities.voter import Voter
import matplotlib.pyplot as plot


def main():
    parties = [0, 1, 2, 3, 4, 5, 6, 7]
    voters = generator.generate_voters(10000, parties)
    election_number = 100
    previous_election_result = {party: 0 for party in parties}
    for i in range(election_number):
        election_result = {party: 0 for party in parties}
        for voter in voters:
            election_result[voter.vote(parties, previous_election_result)] += 1
        for party in parties:
            if election_result[party] < len(voters) / 100:
                parties.remove(party)
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
