from bracket_engine.models import Match


def find_all_matches_in_tree(root: Match) -> list[Match]:
    matches = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        matches.append(current)
        if current.opponent1_from:
            queue.append(current.opponent1_from)
        if current.opponent2_from:
            queue.append(current.opponent2_from)

    return matches


def sort_forest_by_level(level0_matches: list[Match]) -> list[list[Match]]:
    matches = [level0_matches]
    seen_matches = set(level0_matches)
    level = 0

    while matches[level]:
        matches.append([])
        new_matches = set({})
        for match in matches[level]:
            if match.winner_to: new_matches.add(match.winner_to)
            if match.loser_to: new_matches.add(match.loser_to)

        for match in new_matches:
            if match not in seen_matches:
                matches[level + 1].append(match)
                seen_matches.add(match)

        level += 1

    return matches
