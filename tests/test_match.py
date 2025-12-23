import pytest
from bracket_engine.models import Match
from bracket_engine.exceptions import BracketError


def test_opponent_propagation():
    m1 = Match()
    m2 = Match()
    wMatch = Match()
    lMatch = Match()

    m1._winnerTo = wMatch
    wMatch._opponent1From = m1
    m2._winnerTo = wMatch
    wMatch._opponent2From = m2
    m1._loserTo = lMatch
    lMatch._opponent1From = m1
    m2._loserTo = lMatch
    lMatch._opponent2From = m2

    m1._opponent1 = "Seed 1"
    m1._opponent2 = "Seed 4"
    m2._opponent1 = "Seed 2"
    m2._opponent2 = "Seed 3"

    m1.set_winner(1)
    m2.set_winner(2)

    assert m1.winning_side == 1
    assert m2.winning_side == 2
    assert wMatch.opponent1 == "Seed 1"
    assert wMatch.opponent2 == "Seed 3"
    assert lMatch.opponent1 == "Seed 4"
    assert lMatch.opponent2 == "Seed 2"


def test_winning_side_raises_error():
    m = Match()
    with pytest.raises(BracketError):
        m.set_winner(0)
        m.set_winner(3)
        m.set_winner(5)


def test_source_match_raises_error():
    m1 = Match()
    m1._opponent1From = Match()

    m2 = Match()
    m2._opponent1From = Match()
    m2._opponent2From = Match()

    m3 = Match()

    with pytest.raises(BracketError):
        m1.recieve_opponent("", Match())
        m2.recieve_opponent("", Match())
        m3.recieve_opponent("", Match())
