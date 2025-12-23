from bracket_engine.exceptions import BuildingError
from bracket_engine.models import Match
import bracket_engine.utils.tree_logic as tree


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


def bracket_from_root_matches(roots: list[Match]) -> Bracket:
    match_list = []
    for root in roots:
        if root.winner_to or root.loser_to:
            raise BuildingError("Root match is connected to higher level match.")
        match_list += tree.find_all_matches_in_tree(root)

    entry_matches = []
    for match in match_list:
        if not (match.opponent1_from and match.opponent2_from):
            entry_matches.append(match)

    matches = tree.sort_forest_by_level(roots)

    return Bracket(matches, roots, entry_matches)


def bracket_from_root_match(root: Match) -> Bracket:
    return bracket_from_root_matches([root])
