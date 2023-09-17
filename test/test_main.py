import json
import os
import unittest
from io import StringIO

from bs4 import BeautifulSoup

from src import main


class TestMyFunctions(unittest.TestCase):

    def setUp(self):
        # Prepare test data for get_login_page
        self.login_info_json = {
            "url": "https://example.com",
            "cookies": {"session_id": "12345"},
            "headers": {"User-Agent": "Test-Agent"}
        }

        self.login_info_json_string = StringIO(
            json.dumps(self.login_info_json)
        )
        self.parser = 'html.parser'

    def test_get_login_page_local(self):
        with open('local_temp.json', 'w') as f:
            json.dump(self.login_info_json, f, indent=4)

        soup = main.get_login_page('local_temp.json',
                                   local=True)
        self.assertIsInstance(soup,
                              BeautifulSoup)

    def test_get_login_page_non_local(self):
        soup = main.get_login_page(self.login_info_json_string,
                                   local=False)
        self.assertIsInstance(soup,
                              BeautifulSoup)

    def test_benched(self):
        with open(os.path.join('test',
                               'test_benched_element.html'),
                  'r',
                  encoding='utf-8') as file:
            data = file.read()
        html_content = BeautifulSoup(data)
        player_html = html_content.find('strong', string='Q')
        self.assertTrue(main._benched(player_html))


if __name__ == '__main__':
    unittest.main()
