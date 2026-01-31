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
        self._layer = 0

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

    @property
    def layer(self) -> int:
        return self._layer

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

    def set_as_layer_1_entry(self):
        if self._opponent1_from and self._opponent2_from:
            raise BracketError("Trying to set layer 1 entry on match that is not an entry match.")
        self._layer = 1

    def calculate_layer(self, preceding_match: 'Match'):
        if not (preceding_match == self._opponent1_from or preceding_match == self._opponent2_from):
            raise BracketError(f"Trying to calculate layer from not connected match.\nself: {self}\n"
                               f"preceding_match: {preceding_match}\nopponent1_from: {self.opponent1_from}\n"
                               f"opponent2_from: {self.opponent2_from}")
        if preceding_match.winner_to == self:
            self._layer = preceding_match.layer
        else:
            self._layer = preceding_match.layer + 1

    def backtrack_layer(self, next_match: 'Match'):
        if not next_match == self._winner_to:
            raise BracketError("Backtracking not possible: No winner_to connection found.")
        self._layer = next_match.layer


class Bracket:
    def __init__(self, matches: list[list[Match]], roots: list[Match], entry_matches: list[Match]):
        self._matches = matches
        self._roots = roots
        self._entry_matches = entry_matches

    @property
    def matches_by_level(self):
        return self._matches

    @property
    def roots(self):
        return self._roots

    @property
    def entry_matches(self):
        return self._entry_matches

    @property
    def max_level(self) -> int:
        return len(self._matches)

    @property
    def match_list(self) -> list[Match]:
        match_list = []
        for level in self._matches:
            match_list += level

        return match_list

    def calculate_layers(self):
        # based on assumption that winner stays in layer and loser moves exactly 1 layer down
        layer_1_entries = []
        seen_matches = set({})
        for match in self._entry_matches:
            if match.layer == 1:
                layer_1_entries.append(match)
                seen_matches.add(match)

        losing_matches = []
        queue = layer_1_entries
        while queue:
            match = queue.pop(0)
            winner_to = match.winner_to
            if winner_to and winner_to not in seen_matches:
                winner_to.calculate_layer(match)
                seen_matches.add(winner_to)
                queue.append(winner_to)
            loser_to = match.loser_to
            if loser_to and loser_to not in seen_matches:
                loser_to.calculate_layer(match)
                losing_matches.append(loser_to)
                seen_matches.add(loser_to)

            if not queue:
                while losing_matches:
                    loser_match = losing_matches.pop(0)
                    queue.append(loser_match)
                    for preceding_match in [loser_match.opponent1_from, loser_match.opponent2_from]:
                        if preceding_match and preceding_match not in seen_matches:
                            preceding_match.backtrack_layer(loser_match)
                            losing_matches.append(preceding_match)
                            seen_matches.add(preceding_match)
                            queue.append(preceding_match)
