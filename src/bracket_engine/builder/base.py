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


def bracket_from_root_matches(roots: list[Match]) -> Bracket:
    match_list = set({})
    for root in roots:
        if root.winner_to or root.loser_to:
            raise BuildingError("Root match is connected to higher level match.")
        match_list.update(tree.find_all_matches_in_tree(root))
    match_list = list(match_list)

    entry_matches = []
    for match in match_list:
        if not (match.opponent1_from and match.opponent2_from):
            entry_matches.append(match)

    if tree.has_cycle(entry_matches):
        raise BuildingError("The bracket contains a cycle")

    matches = tree.sort_forest_by_level(roots)

    return Bracket(matches, roots, entry_matches)


def bracket_from_root_match(root: Match) -> Bracket:
    return bracket_from_root_matches([root])
