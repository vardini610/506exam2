import json
from pathlib import Path


def clean_squad(squad):
    """Converts a player's "Squad" value (e.g. "es Spain") to a two-item tuple
    comprising the following items:

    1  Upper case two-letter country abbreviation (e.g., "ES")
    2. squad name (e.g., "Spain")

    Parameters:
        squad (str): comprises a two-letter country abbreviation and squad name

    Returns:
        tuple: "Squad" element converted to a two-item tuple
    """

    # TODO 2.3
    pass


def format_player_position(position):
    """Reformats player's position string by converting the comma (",") delimiter that
    separates multiple positions to a pipe (|), e.g., "MF,DF" -> "MF|DF".

    Parameters:
        position (str): player's position string

    Returns:
        str: reformatted position string
    """

    # TODO 2.1
    pass


def get_multi_position_players(players):
    """Returns players who play multiple positions. Evaluates the "position" value
    for the presence of multiple positions (e.g., "DF", "FW", "GK", "MF").

    Parameters:
        players (list): list of dictionaries each representing one player

    Returns:
        list: list of dictionaries each representing one player who play multiple positions
    """

    # TODO 4.1
    pass


def get_player_shooting_numbers(player, shooting_keys):
    """Returns a player's shots, shots on target, and goals scored. All values
    are converted from strings to integers before being returned to the caller.

    Parameters:
        player (dict): a dictionary containing player data
        shooting_keys (list): list of keys representing shooting statistics

    Returns:
        list: player's shooting statistics (shots, shots on target, and goals)
    """

    # TODO 8.1
    pass


def get_team(players, squad):
    """Returns members of a country's team.

    Parameters:
        players (list): list of dictionaries of player data
        squad (str): country/squad name

    Returns:
        list: team members who represent the < squad >
    """

    # TODO 5.1
    pass


def get_team_names(players):
    """Returns a list of team/squad names that correspond to the countries participating
    in the World Cup. Duplicate names are filtered out of the list returned to the caller.

    Parameters:
        players (list): list of dictionaries of player data

    Returns:
        list: countries represented by the players in the < players > list
    """

    # TODO 7.1
    pass


def get_top_scorer(players):
    """Returns the top scorer from the < players > list. Filters out players
    that did not score a goal and excludes them from consideration. Ties between
    top scorers are accommodated.

    Parameters:
        players (list): list of dictionaries of player data

    Returns:
        list: list of dictionaries of one or more top scorers
    """

    # TODO 6.1
    pass


def read_json(filepath, encoding="utf-8"):
    """Reads a JSON file and converts it to a Python dictionary.

    Parameters:
        filepath (str): a path to the JSON file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """
    with open(filepath, "r", encoding=encoding) as file_obj:
        data = json.load(file_obj)
    return data


def thin_player(player, keep_keys):
    """Accepts a dictionary representation of a player and a list of desired keys.
    Creates an empty dictionary. Loops through the keys and values of < player >.

    For each key-value pair, if the key is in < keep_keys >, the key-value pair is added to
    the empty dictionary.

    Parameters:
        player (dict): a dictionary representing a player
        keep_keys (list): a list of keys to keep

    Returns:
        dict: a dictionary containing only the key-value pairs specified in < keep_keys >
    """

    # TODO 1.3
    pass


def write_json(filepath, data, encoding="utf-8", indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file

        data (dict)/(list): the data to be encoded as JSON and written to
        the file

        encoding (str): name of encoding used to encode the file

        indent (int): number of "pretty printed" indention spaces applied to
        encoded JSON

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=indent)


def main():
    """Program entry point. Orchestrates workflow.

    Parameters:
        None

    Returns:
        None
    """
    print("Problem Set 5 \n")

    # PROBLEM 01
    print("\nPROBLEM 1")

    # TODO 1.1

    # TODO 1.2

    # TODO 1.4
    keep_keys = ["id", "player", "position", "squad", "stats"]

    # TODO 1.5
    # print(f"\n1.4 players[-1] = {players[-1]}")  # last player
    # assert players[-1] == {
    #     "id": 619,
    #     "player": "Claudia Zornoza",
    #     "position": "MF",
    #     "squad": "es Spain",
    #     "stats": {"90s": 0.4, "goals": 0, "shots": 0, "shots_on_target": 0},
    # }

    # PROBLEM 02
    print("\nPROBLEM 2")

    # TODO 2.2
    # assert "MF|DF" == format_player_position("MF,DF")
    # assert "GK" == format_player_position("GK")

    # TODO 2.4
    # assert ("NG", "Nigeria") == clean_squad("ng Nigeria")
    # assert ("ZA", "South Africa") == clean_squad("za South Africa")

    # PROBLEM 03
    print("\nPROBLEM 3")

    # TODO 3.1

    # TODO 3.2

    # PROBLEM 04
    print("\nPROBLEM 4")

    # TODO 4.2

    # TODO 4.3

    # PROBLEM 05
    print("\nPROBLEM 5")

    # TODO 5.2

    # TODO 5.3

    # PROBLEM 06
    print("\nPROBLEM 6")

    # TODO 6.2

    # TODO 6.3
    # print(f"\n6.4 top scorer(s) (n={len(top_scorers)}) = {top_scorers}")

    # PROBLEM 07
    print("\nPROBLEM 7")

    # TODO 7.2

    # TODO 7.3

    # TODO 7.4
    # print(f"\n7.4 countries = {countries}")
    # assert len(countries) == 32

    # TODO 7.5-9

    # TODO 7.10

    # PROBLEM 08
    print("\nPROBLEM 8")

    shooting_keys = ["goals", "shots", "shots_on_target"]

    # TODO 8.2

    # TODO 8.3
    # print(
    #     f"\n8.4 goals = {goals}",
    #     f"shots = {shots}",
    #     f"shots_on_target = {shots_on_target}",
    #     sep="\n",
    # )
    # assert goals == 1
    # assert shots == 10
    # assert shots_on_target == 4



if __name__ == "__main__":
    main()
