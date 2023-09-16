import json
from typing import TextIO

import requests
from bs4 import BeautifulSoup

STATUSES = {
    "Q": "Questionable",
    "IA": "Inactive",
    "O": "Out",
    "IR": "Injured Reserved",
    "D": "Doubtful"
}


def get_login_page(cookie_sess_page: TextIO) -> BeautifulSoup:
    """Returns the login page of the provided session.
    This function is expecting a JSON file with the 
    cookie information that includes the login session
    of the desired page. The file must exists locally.

    Parameters
    ----------
    cookie_sess_page : JSON file
        The JSON file that has all the cookie information
        for the site to be logged in.

    Returns
    -------
    BeautifulSoup
        The souped object of the page.
    """
    with open(cookie_sess_page, 'r') as f:
        data = json.load(f)

    response = requests.get(data['url'],
                            cookies=data['cookies'],
                            headers=data['headers'])

    soup = BeautifulSoup(response.content,
                         'html.parser')

    return soup


def get_players_status() -> dict:
    """Returns a JSON object of all the players that 
    have the Questionable, Inactive, Doubtful, Injured
    Reserved Status.  Only returns the players who are
    starting.

    Returns
    -------
    dict
        A Dictionary object of all the affected players
    """
    team_page = get_login_page('login_info.json')
    output = {}
    for code, status in STATUSES.items():
        temp = []
        affected_players = team_page.find_all("strong",
                                              string=code)

        for player in affected_players:
            if not _benched(player):
                temp.append(player.parent.text)
        output[status] = temp

    return output


def _benched(player: BeautifulSoup) -> bool:
    """Helper function to check if the current player
    is benched or not

    Parameters
    ----------
    player : BeautifulSoup
        The Soup object of the current player

    Returns
    -------
    bool
        Returns True if benched
    """
    if player.parent.parent.parent.contents[0].text == "BN":
        return True
    return False


if __name__ == "__main__":
    print(get_players_status())
