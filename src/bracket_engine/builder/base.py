from bracket_engine.exceptions import BuildingError
from bracket_engine.models import Match, Bracket
import bracket_engine.utils.tree_logic as tree


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
