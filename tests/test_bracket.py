import pytest
from bracket_engine.builder.base import *
from bracket_engine.models import Match, LinkType


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
