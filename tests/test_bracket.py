import pytest
from bracket_engine.builder.base import *
from bracket_engine.models import Match, LinkType


def generate_bracket():
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
    bracket, entries = generate_bracket()
    assert len(bracket.entry_matches) == 6
    assert bracket.max_level == 6
    for match in entries:
        assert match in bracket.entry_matches
    assert len(bracket.roots) == 1


def test_advanced_layers():
    bracket, entries = generate_bracket()
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
