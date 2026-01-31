import pytest
from bracket_engine.builder.base import *
from bracket_engine.models import Match, LinkType


def generate_bracket(bracket: int):
    if bracket == 1:
        # Ref: https://liquipedia.net/rocketleague/Rocket_League_Championship_Series/2021-22/Winter#Playoffs
        gf = Match()
        print(f"gf: {gf}")
        uf = Match()
        print(f"uf: {uf}")
        lf = Match()
        print(f"lf: {lf}")
        uf.connect_to(gf, LinkType.WINNER, 1)
        lf.connect_to(gf, LinkType.WINNER, 2)
        uf.connect_to(lf, LinkType.LOSER, 1)
        ls = Match()
        print(f"ls: {ls}")
        ls.connect_to(lf, LinkType.WINNER, 2)
        lq1 = Match()
        print(f"lq1: {lq1}")
        lq2 = Match()
        print(f"lq2: {lq2}")
        lq1.connect_to(ls, LinkType.WINNER, 1)
        lq2.connect_to(ls, LinkType.WINNER, 2)
        us1 = Match()
        print(f"us1: {us1}")
        us2 = Match()
        print(f"us2: {us2}")
        us1.connect_to(uf, LinkType.WINNER, 1)
        us2.connect_to(uf, LinkType.WINNER, 2)
        us1.connect_to(lq1, LinkType.LOSER, 1)
        us2.connect_to(lq2, LinkType.LOSER, 1)
        lr21 = Match()
        print(f"lr21: {lr21}")
        lr22 = Match()
        print(f"lr22: {lr22}")
        lr21.connect_to(lq1, LinkType.WINNER, 2)
        lr22.connect_to(lq2, LinkType.WINNER, 2)
        lr11 = Match()
        print(f"lr11: {lr11}")
        lr12 = Match()
        print(f"lr12: {lr12}")
        lr13 = Match()
        print(f"lr13: {lr13}")
        lr14 = Match()
        print(f"lr14: {lr14}")
        lr11.connect_to(lr21, LinkType.WINNER, 1)
        lr12.connect_to(lr21, LinkType.WINNER, 2)
        lr13.connect_to(lr22, LinkType.WINNER, 1)
        lr14.connect_to(lr22, LinkType.WINNER, 2)

        return bracket_from_root_match(gf), [us1, us2]

    elif bracket == 2:
        q1 = Match(qualified_number=1)
        print(f"q1: {q1}")
        q2 = Match(qualified_number=2)
        print(f"q2: {q2}")
        m1 = Match()
        print(f"m1: {m1}")
        m2 = Match()
        print(f"m2: {m2}")
        m3 = Match()
        print(f"m3: {m3}")
        m4 = Match()
        print(f"m4: {m4}")
        m1.connect_to(q1, LinkType.WINNER, 1)
        m2.connect_to(q1, LinkType.WINNER, 2)
        m3.connect_to(q2, LinkType.WINNER, 1)
        m4.connect_to(q2, LinkType.WINNER, 2)

        return bracket_from_root_matches([q1, q2]), [m1, m2, m3, m4]

    elif bracket == 3:
        # Ref: https://liquipedia.net/rocketleague/Rocket_League_Championship_Series/2026/Boston_Major/Europe/Open_3#Group_Stage
        us1 = Match(qualified_number=1)
        print(f"us1: {us1}")
        us2 = Match(qualified_number=1)
        print(f"us2: {us2}")
        ls1 = Match(qualified_number=1)
        print(f"ls1: {ls1}")
        ls2 = Match(qualified_number=1)
        print(f"ls2: {ls2}")
        us1.connect_to(ls2, LinkType.LOSER, 1)
        us2.connect_to(ls1, LinkType.LOSER, 1)
        lq1 = Match()
        print(f"lq1: {lq1}")
        lq2 = Match()
        print(f"lq2: {lq2}")
        lq1.connect_to(ls1, LinkType.WINNER, 2)
        lq2.connect_to(ls2, LinkType.WINNER, 2)
        uq1 = Match()
        print(f"uq1: {uq1}")
        uq2 = Match()
        print(f"uq2: {uq2}")
        uq3 = Match()
        print(f"uq3: {uq3}")
        uq4 = Match()
        print(f"uq4: {uq4}")
        uq1.connect_to(us1, LinkType.WINNER, 1)
        uq2.connect_to(us1, LinkType.WINNER, 2)
        uq3.connect_to(us2, LinkType.WINNER, 1)
        uq4.connect_to(us2, LinkType.WINNER, 2)
        uq1.connect_to(lq1, LinkType.LOSER, 1)
        uq2.connect_to(lq1, LinkType.LOSER, 2)
        uq3.connect_to(lq2, LinkType.LOSER, 1)
        uq4.connect_to(lq2, LinkType.LOSER, 2)

        return bracket_from_root_matches([ls1, ls2]), [uq1, uq2, uq3, uq4]

    elif bracket == 4:
        # Ref: https://liquipedia.net/counterstrike/Intel_Extreme_Masters/2025/Chengdu#Group_Stage
        uf = Match(qualified_number=2)
        print(f"uf: {uf}")
        lf = Match(qualified_number=1)
        print(f"lf: {lf}")
        us1 = Match()
        print(f"us1: {us1}")
        us2 = Match()
        print(f"us2: {us2}")
        us1.connect_to(uf, LinkType.WINNER, 1)
        us2.connect_to(uf, LinkType.WINNER, 2)
        ls1 = Match()
        print(f"ls1: {ls1}")
        ls2 = Match()
        print(f"ls2: {ls2}")
        ls1.connect_to(lf, LinkType.WINNER, 1)
        ls2.connect_to(lf, LinkType.WINNER, 2)
        us1.connect_to(ls2, LinkType.LOSER, 1)
        us2.connect_to(ls1, LinkType.LOSER, 1)
        lq1 = Match()
        print(f"lq1: {lq1}")
        lq2 = Match()
        print(f"lq2: {lq2}")
        lq1.connect_to(ls1, LinkType.WINNER, 2)
        lq2.connect_to(ls2, LinkType.WINNER, 2)
        uq1 = Match()
        print(f"uq1: {uq1}")
        uq2 = Match()
        print(f"uq2: {uq2}")
        uq3 = Match()
        print(f"uq3: {uq3}")
        uq4 = Match()
        print(f"uq4: {uq4}")
        uq1.connect_to(us1, LinkType.WINNER, 1)
        uq2.connect_to(us1, LinkType.WINNER, 2)
        uq3.connect_to(us2, LinkType.WINNER, 1)
        uq4.connect_to(us2, LinkType.WINNER, 2)
        uq1.connect_to(lq1, LinkType.LOSER, 1)
        uq2.connect_to(lq1, LinkType.LOSER, 2)
        uq3.connect_to(lq2, LinkType.LOSER, 1)
        uq4.connect_to(lq2, LinkType.LOSER, 2)

        return bracket_from_root_matches([uf, lf]), [uq1, uq2, uq3, uq4]

    elif bracket == 5:
        # Ref: https://liquipedia.net/valorant/VCT/2026/EMEA_League/Kickoff#Results
        lf = Match(qualified_number=1)
        print(f"lf: {lf}")
        mf = Match(qualified_number=1)
        print(f"mf: {mf}")
        mf.connect_to(lf, LinkType.LOSER, 1)
        uf = Match(qualified_number=1)
        print(f"uf: {uf}")
        uf.connect_to(mf, LinkType.LOSER, 1)
        ls = Match()
        print(f"ls: {ls}")
        ls.connect_to(lf, LinkType.WINNER, 2)
        ms = Match()
        print(f"ms: {ms}")
        ms.connect_to(mf, LinkType.WINNER, 2)
        ms.connect_to(ls, LinkType.LOSER, 1)
        lq = Match()
        print(f"lq: {lq}")
        lq.connect_to(ls, LinkType.WINNER, 2)
        lr31 = Match()
        print(f"lr31: {lr31}")
        lr32 = Match()
        print(f"lr32: {lr32}")
        lr31.connect_to(lq, LinkType.WINNER, 1)
        lr32.connect_to(lq, LinkType.WINNER, 2)
        mq1 = Match()
        print(f"mq1: {mq1}")
        mq2 = Match()
        print(f"mq2: {mq2}")
        mq1.connect_to(ms, LinkType.WINNER, 1)
        mq2.connect_to(ms, LinkType.WINNER, 2)
        mq1.connect_to(lr31, LinkType.LOSER, 1)
        mq2.connect_to(lr32, LinkType.LOSER, 1)
        us1 = Match()
        print(f"us1: {us1}")
        us2 = Match()
        print(f"us2: {us2}")
        us1.connect_to(uf, LinkType.WINNER, 1)
        us2.connect_to(uf, LinkType.WINNER, 2)
        us1.connect_to(mq1, LinkType.LOSER, 1)
        us2.connect_to(mq2, LinkType.LOSER, 1)
        lr21 = Match()
        print(f"lr21: {lr21}")
        lr22 = Match()
        print(f"lr22: {lr22}")
        lr21.connect_to(lr31, LinkType.WINNER, 2)
        lr22.connect_to(lr32, LinkType.WINNER, 2)
        mr21 = Match()
        print(f"mr21: {mr21}")
        mr22 = Match()
        print(f"mr22: {mr22}")
        mr21.connect_to(mq1, LinkType.WINNER, 2)
        mr22.connect_to(mq2, LinkType.WINNER, 2)
        mr21.connect_to(lr22, LinkType.LOSER, 1)
        mr22.connect_to(lr21, LinkType.LOSER, 1)
        lr11 = Match()
        print(f"lr11: {lr11}")
        lr12 = Match()
        print(f"lr12: {lr12}")
        lr11.connect_to(lr21, LinkType.WINNER, 2)
        lr12.connect_to(lr22, LinkType.WINNER, 2)
        mr11 = Match()
        print(f"mr11: {mr11}")
        mr12 = Match()
        print(f"mr12: {mr12}")
        mr13 = Match()
        print(f"mr13: {mr13}")
        mr14 = Match()
        print(f"mr14: {mr14}")
        mr11.connect_to(mr21, LinkType.WINNER, 1)
        mr12.connect_to(mr21, LinkType.WINNER, 2)
        mr13.connect_to(mr22, LinkType.WINNER, 1)
        mr14.connect_to(mr22, LinkType.WINNER, 2)
        mr11.connect_to(lr11, LinkType.LOSER, 1)
        mr12.connect_to(lr11, LinkType.LOSER, 2)
        mr13.connect_to(lr12, LinkType.LOSER, 1)
        mr14.connect_to(lr12, LinkType.LOSER, 2)
        uq1 = Match()
        print(f"uq1: {uq1}")
        uq2 = Match()
        print(f"uq2: {uq2}")
        uq3 = Match()
        print(f"uq3: {uq3}")
        uq4 = Match()
        print(f"uq4: {uq4}")
        uq1.connect_to(us1, LinkType.WINNER, 1)
        uq2.connect_to(us1, LinkType.WINNER, 2)
        uq3.connect_to(us2, LinkType.WINNER, 1)
        uq4.connect_to(us2, LinkType.WINNER, 2)
        uq1.connect_to(mr14, LinkType.LOSER, 1)
        uq2.connect_to(mr13, LinkType.LOSER, 1)
        uq3.connect_to(mr12, LinkType.LOSER, 1)
        uq4.connect_to(mr11, LinkType.LOSER, 1)
        ur11 = Match()
        print(f"ur11: {ur11}")
        ur12 = Match()
        print(f"ur12: {ur12}")
        ur13 = Match()
        print(f"ur13: {ur13}")
        ur14 = Match()
        print(f"ur14: {ur14}")
        ur11.connect_to(uq1, LinkType.WINNER, 2)
        ur12.connect_to(uq2, LinkType.WINNER, 2)
        ur13.connect_to(uq3, LinkType.WINNER, 2)
        ur14.connect_to(uq4, LinkType.WINNER, 2)
        ur11.connect_to(mr11, LinkType.LOSER, 2)
        ur12.connect_to(mr12, LinkType.LOSER, 2)
        ur13.connect_to(mr13, LinkType.LOSER, 2)
        ur14.connect_to(mr14, LinkType.LOSER, 2)

        return bracket_from_root_match(lf), [ur11, ur12, ur13, ur14, uq1, uq2, uq3, uq4]


def test_basic_bracket_building():
    s1 = Match()
    s2 = Match()
    gf = Match()

    s1.connect_to(gf, LinkType.WINNER, 1)
    s2.connect_to(gf, LinkType.WINNER, 2)

    bracket = bracket_from_root_match(gf)

    assert bracket.max_level == 2
    assert s1 in bracket.entry_matches
    assert s2 in bracket.entry_matches
    assert len(bracket.entry_matches) == 2


def test_advanced_bracket_building():
    bracket, entries = generate_bracket(1)
    assert len(bracket.match_list) == 14
    assert len(bracket.entry_matches) == 6
    assert bracket.max_level == 6
    for match in entries:
        assert match in bracket.entry_matches
    assert len(bracket.roots) == 1


def test_advanced_layers():
    bracket, entries = generate_bracket(1)
    for match in entries:
        match.set_as_layer_1_entry()
        assert match.layer == 1

    bracket.calculate_layers()

    assert bracket.roots[0].layer == 1

    upper = []
    lower = []
    other = []

    for match in bracket.match_list:
        if match.layer == 1:
            upper.append(match)
        elif match.layer == 2:
            lower.append(match)
        else:
            other.append(match)

    assert len(upper) == 4
    assert len(lower) == 10
    assert len(other) == 0

    entry_layer_1 = []
    entry_layer_2 = []
    other = []
    for match in bracket.entry_matches:
        if match.layer == 1:
            entry_layer_1.append(match)
        elif match.layer == 2:
            entry_layer_2.append(match)
        else:
            other.append(match)

    assert len(entry_layer_1) == 2
    assert len(entry_layer_2) == 4
    assert len(other) == 0

    for match in entries:
        assert match in entry_layer_1


def test_qual_bracket_building():
    bracket, entries = generate_bracket(2)
    assert len(bracket.match_list) == 6
    assert len(bracket.entry_matches) == 4
    assert bracket.max_level == 2
    for match in entries:
        assert match in bracket.entry_matches
    assert len(bracket.roots) == 2


def test_qual_layers():
    bracket, entries = generate_bracket(2)
    for match in entries:
        match.set_as_layer_1_entry()

    bracket.calculate_layers()

    for match in bracket.match_list:
        assert match.layer == 1


def test_group1_bracket_building():
    bracket, entries = generate_bracket(3)
    assert len(bracket.match_list) == 10
    assert len(bracket.entry_matches) == 4
    assert bracket.max_level == 3
    for match in entries:
        assert match in bracket.entry_matches
    assert len(bracket.roots) == 2


def test_group1_layers():
    bracket, entries = generate_bracket(3)
    for match in entries:
        match.set_as_layer_1_entry()

    bracket.calculate_layers()

    upper = []
    lower = []
    other = []

    for match in bracket.match_list:
        if match.layer == 1:
            upper.append(match)
        elif match.layer == 2:
            lower.append(match)
        else:
            other.append(match)

    assert len(upper) == 6
    assert len(lower) == 4
    assert len(other) == 0

    entry_layer_1 = []
    entry_layer_2 = []
    other = []
    for match in bracket.entry_matches:
        if match.layer == 1:
            entry_layer_1.append(match)
        elif match.layer == 2:
            entry_layer_2.append(match)
        else:
            other.append(match)

    assert len(entry_layer_1) == 4
    assert len(entry_layer_2) == 0
    assert len(other) == 0

    for match in entries:
        assert match in entry_layer_1


def test_group2_bracket_building():
    bracket, entries = generate_bracket(4)
    assert len(bracket.match_list) == 12
    assert len(bracket.entry_matches) == 4
    assert bracket.max_level == 3
    for match in entries:
        assert match in bracket.entry_matches
    assert len(bracket.roots) == 2


def test_group2_layers():
    bracket, entries = generate_bracket(4)
    for match in entries:
        match.set_as_layer_1_entry()

    bracket.calculate_layers()

    upper = []
    lower = []
    other = []

    for match in bracket.match_list:
        if match.layer == 1:
            upper.append(match)
        elif match.layer == 2:
            lower.append(match)
        else:
            other.append(match)

    assert len(upper) == 7
    assert len(lower) == 5
    assert len(other) == 0

    entry_layer_1 = []
    entry_layer_2 = []
    other = []
    for match in bracket.entry_matches:
        if match.layer == 1:
            entry_layer_1.append(match)
        elif match.layer == 2:
            entry_layer_2.append(match)
        else:
            other.append(match)

    assert len(entry_layer_1) == 4
    assert len(entry_layer_2) == 0
    assert len(other) == 0

    for match in entries:
        assert match in entry_layer_1


def test_triple_qual_bracket_building():
    bracket, entries = generate_bracket(5)
    assert len(bracket.match_list) == 30
    assert len(bracket.entry_matches) == 8
    assert bracket.max_level == 6
    for match in entries:
        assert match in bracket.entry_matches
    assert len(bracket.roots) == 1


def test_triple_qual_layers():
    bracket, entries = generate_bracket(5)
    for match in entries:
        match.set_as_layer_1_entry()

    bracket.calculate_layers()

    upper = []
    mid = []
    lower = []
    other = []

    for match in bracket.match_list:
        if match.layer == 1:
            upper.append(match)
        elif match.layer == 2:
            mid.append(match)
        elif match.layer == 3:
            lower.append(match)
        else:
            other.append(match)

    assert len(upper) == 11
    assert len(mid) == 10
    assert len(lower) == 9
    assert len(other) == 0

    entry_layer_1 = []
    entry_layer_2 = []
    entry_layer_3 = []
    other = []
    for match in bracket.entry_matches:
        if match.layer == 1:
            entry_layer_1.append(match)
        elif match.layer == 2:
            entry_layer_2.append(match)
        elif match.layer == 3:
            entry_layer_3.append(match)
        else:
            other.append(match)

    assert len(entry_layer_1) == 8
    assert len(entry_layer_2) == 0
    assert len(entry_layer_3) == 0
    assert len(other) == 0

    for match in entries:
        assert match in entry_layer_1


def test_cycle_raises_error():
    final = Match()
    m1 = Match()
    m2 = Match()
    m3 = Match()
    m1.connect_to(m2, LinkType.WINNER, 1)
    m2.connect_to(m3, LinkType.LOSER, 1)
    m3.connect_to(m2, LinkType.WINNER, 2)
    m2.connect_to(final, LinkType.WINNER, 1)

    with pytest.raises(BuildingError):
        bracket = bracket_from_root_match(final)

