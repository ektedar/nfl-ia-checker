import json
from typing import TextIO

import requests
from bs4 import BeautifulSoup

# STATUSES = [
#     "Q",
#     "IA",
#     "O",
#     "IR",
#     "D"
# ]

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


def main():
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
    if player.parent.parent.parent.contents[0].text == "BN":
        return True
    return False


if __name__ == "__main__":
    print(main())
