from typing import Optional
from exceptions import BracketError


class Match:
    def __init__(self, qualified_number=0):
        self._opponent1 = None
        self._opponent2 = None
        self._winning_side = 0
        self._winnerTo: Optional['Match'] = None
        self._loserTo: Optional['Match'] = None
        self._opponent1From: Optional['Match'] = None
        self._opponent2From: Optional['Match'] = None
        self._qualified_number = qualified_number

    @property
    def opponent1(self):
        return self._opponent1

    @property
    def opponent2(self):
        return self._opponent2

    @property
    def winner(self) -> int:
        return self._winning_side

    @property
    def winnerTo(self) -> Optional['Match']:
        return self._winnerTo

    @property
    def loserTo(self) -> Optional['Match']:
        return self._loserTo

    @property
    def opponent1From(self) -> Optional['Match']:
        return self._opponent1From

    @property
    def opponent2From(self) -> Optional['Match']:
        return self._opponent2From

    @property
    def qualified_number(self) -> int:
        return self.qualified_number

    def recieve_opponent(self, opponent, source_match: 'Match'):
        if source_match == self._opponent1From:
            self._opponent1 = opponent
        elif source_match == self._opponent2From:
            self._opponent2 = opponent
        else:
            raise BracketError("Source match is unknown as a provider for this match.")

    def set_winner(self, winning_side: int):
        if winning_side not in (1, 2):
            raise BracketError(f"Invalid winning side: {winning_side}. Must be 1 or 2.")

        self._winning_side = winning_side

        winner = self._opponent1 if winning_side == 1 else self._opponent2
        loser = self._opponent1 if winning_side == 2 else self._opponent2

        if self._winnerTo:
            self._winnerTo.recieve_opponent(winner, self)
        if self._loserTo:
            self._loserTo.recieve_opponent(loser, self)
