import pandas as pd
import numpy as np
import random
from itertools import combinations

# Function to randomly pick two applicants
def pick_applicants(df):
    '''
    Input : a Pandas DataFrame
    '''
    assert df.index.name == "Name"
    # Drop NAs
    df.dropna(inplace=True)
    # Count # of rows
    num_rows = len(df)
    # Pick two applicants (pseudo-random)
    applicants = random.sample(set(list(df.index)), 2)
    random.shuffle(applicants)

    return applicants


# A Class to Represent a Given Applicant
class Applicant:
    '''
    Input : A DataFrame Row, applicant name
    '''

    # Initializer / Instance attributes
    def __init__(self, df, applicant_name):
        assert df.index.name == "Name"
        assert applicant_name in list(df.index), 'Name is Not in DF!'
        dff = df.loc[df.index == applicant_name].copy()
        self.name = applicant_name
        self.health = list(dff.Health)[0]
        self.damage = list(dff.Damage)[0]
        self.attacks = list(dff.Attacks)[0]
        self.dodge = list(dff.Dodge)[0]
        self.critical = list(dff.Critical)[0]
        self.initiative = list(dff.Initiative)[0]


def fight(round_num, applicant_pairing):
    log = pd.DataFrame({"Round": [], "Step": [], "Action": []})
    children = list()
    num_round_steps = max([applicant_pairing[0].attacks, applicant_pairing[1].attacks])

    random.shuffle(applicant_pairing)
    a = applicant_pairing[0]
    b = applicant_pairing[1]

    a_attacks_original = a.attacks
    b_attacks_original = b.attacks
    for _ in range(num_round_steps):
        if a.attacks > 0 and b.health > 0 and a.health > 0:
            # print(
            #     f'''{a.name} hits {b.name} for {a.damage} damage ({b.health}->{b.health-a.damage})  '''
            # )
            log = log.append(
                {
                    "Round": round_num,
                    "Step": _,
                    "Action": f'''{a.name} hits {b.name} for {a.damage} damage ({b.health}->{b.health-a.damage})  ''',
                },
                ignore_index=True,
            )

            a.attacks -= 1
            b.health -= a.damage

        # B HITS A
        # CHECK IF B HAS ATTACKS AND IF A CAN TAKE DAMAGE
        if b.attacks > 0 and a.health > 0 and b.health > 0:
            # print(
            #     f'''{b.name} hits {a.name} for {b.damage} damage ({a.health}->{a.health-b.damage})  '''
            # )
            log = log.append(
                {
                    "Round": round_num,
                    "Step": _,
                    "Action": f'''{b.name} hits {a.name} for {b.damage} damage ({a.health}->{a.health-b.damage})  ''',
                },
                ignore_index=True,
            )

            b.attacks -= 1
            a.health -= b.damage
    a.attacks = a_attacks_original
    b.attacks = b_attacks_original
    return log


def determine_winner(applicants):
    '''
    Input : List of Two applicants
    Returns : Name of Winner
    '''
    if applicants[0].health > applicants[1].health:
        return applicants[0].name
    if applicants[1].health > applicants[0].health:
        return applicants[1].name


def melee(df):
    '''
    Run all combinations
    '''
    output = {"Candidate 1": [], "Candidate 2": [], "Winner": []}
    comb = combinations(list(df.index), 2)
    for c in comb:
        applicants = [c[0], c[1]]
        applicant_pairing = list()
        for applicant in applicants:
            applicant_pairing.append(Applicant(df, applicant))
        applicant_1 = applicant_pairing[0]
        applicant_2 = applicant_pairing[1]

        round_num = 0
        while applicant_1.health > 0 and applicant_2.health > 0:
            fight(round_num, [applicant_1, applicant_2])
            round_num += 1

        winner = determine_winner(applicant_pairing)
        output["Candidate 1"].append(applicant_1.name)
        output["Candidate 2"].append(applicant_2.name)
        output["Winner"].append(winner)
    return pd.DataFrame(output)
