from typing import Optional
from enum import Enum, auto
from .exceptions import BracketError


class LinkType(Enum):
    WINNER = auto()
    LOSER = auto()


class Match:
    def __init__(self, qualified_number=0):
        self._opponent1 = None
        self._opponent2 = None
        self._winning_side = 0
        self._winner_to: Optional['Match'] = None
        self._loser_to: Optional['Match'] = None
        self._opponent1_from: Optional['Match'] = None
        self._opponent2_from: Optional['Match'] = None
        self._qualified_number = qualified_number

    @property
    def opponent1(self):
        return self._opponent1

    @property
    def opponent2(self):
        return self._opponent2

    @property
    def winning_side(self) -> int:
        return self._winning_side

    @property
    def winner_to(self) -> Optional['Match']:
        return self._winner_to

    @property
    def loser_to(self) -> Optional['Match']:
        return self._loser_to

    @property
    def opponent1_from(self) -> Optional['Match']:
        return self._opponent1_from

    @property
    def opponent2_from(self) -> Optional['Match']:
        return self._opponent2_from

    @property
    def qualified_number(self) -> int:
        return self.qualified_number

    def recieve_opponent(self, opponent, source_match: 'Match'):
        if source_match == self._opponent1_from:
            self._opponent1 = opponent
        elif source_match == self._opponent2_from:
            self._opponent2 = opponent
        else:
            raise BracketError("Source match is unknown as a provider for this match.")

    def disconnect(self, target: 'Match'):
        if self._winner_to == target:
            self._winner_to = None
        elif self._loser_to == target:
            self._loser_to = None
        else:
            raise BracketError("Matches are not fully connected")

        if target.opponent1_from == self:
            target._opponent1_from = None
        elif target.opponent2_from == self:
            target._opponent2_from = None
        else:
            raise BracketError("Matches are not fully connected")

    def connect_to(self, target: 'Match', as_type: LinkType, target_slot: int):
        if target_slot not in (1, 2):
            raise BracketError(f"Invalid target slot: {target_slot}. Must be 1 or 2.")

        if as_type == LinkType.WINNER:
            self._winner_to = target
        else:
            self._loser_to = target

        if target_slot == 1:
            target._opponent1_from = self
        else:
            target._opponent2_from = self

    def set_winner(self, winning_side: int):
        if winning_side not in (1, 2):
            raise BracketError(f"Invalid winning side: {winning_side}. Must be 1 or 2.")

        self._winning_side = winning_side

        winner = self._opponent1 if winning_side == 1 else self._opponent2
        loser = self._opponent1 if winning_side == 2 else self._opponent2

        if self._winner_to:
            self._winner_to.recieve_opponent(winner, self)
        if self._loser_to:
            self._loser_to.recieve_opponent(loser, self)
