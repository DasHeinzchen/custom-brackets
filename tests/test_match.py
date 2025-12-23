import pytest
from bracket_engine.models import Match, LinkType
from bracket_engine.exceptions import BracketError


def test_connection_logic():
    m1 = Match()
    m2 = Match()

    m1.connect_to(m2, LinkType.WINNER, 1)
    assert m1.winner_to == m2
    assert m1.loser_to is None
    assert m2.opponent1_from == m1
    assert m2.opponent2_from is None

    m1.disconnect(m2)
    m1.connect_to(m2, LinkType.LOSER, 1)
    assert m1.winner_to is None
    assert m1.loser_to == m2
    assert m2.opponent1_from == m1
    assert m2.opponent2_from is None

    m1.disconnect(m2)
    m1.connect_to(m2, LinkType.WINNER, 2)
    assert m1.winner_to == m2
    assert m1.loser_to is None
    assert m2.opponent1_from is None
    assert m2.opponent2_from == m1

    m1.disconnect(m2)
    m1.connect_to(m2, LinkType.LOSER, 2)
    assert m1.winner_to is None
    assert m1.loser_to == m2
    assert m2.opponent1_from is None
    assert m2.opponent2_from == m1


def test_connection_raises_error():
    m1 = Match()
    m2 = Match()
    with pytest.raises(BracketError):
        m1.connect_to(m2, LinkType.WINNER, 3)
        m1.disconnect(m2)


def test_opponent_propagation():
    m1 = Match()
    m2 = Match()
    wMatch = Match()
    lMatch = Match()

    m1.connect_to(wMatch, LinkType.WINNER, 1)
    m2.connect_to(wMatch, LinkType.WINNER, 2)
    m1.connect_to(lMatch, LinkType.LOSER, 1)
    m2.connect_to(lMatch, LinkType.LOSER, 2)

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
    m1._opponent1_from = Match()

    m2 = Match()
    m2._opponent1_from = Match()
    m2._opponent2_from = Match()

    m3 = Match()

    with pytest.raises(BracketError):
        m1.recieve_opponent("", Match())
        m2.recieve_opponent("", Match())
        m3.recieve_opponent("", Match())
