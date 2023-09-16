import json
from typing import TextIO

import requests
from bs4 import BeautifulSoup


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
    print(team_page.title)


if __name__ == "__main__":
    main()
