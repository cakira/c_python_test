import unittest
import webcolors

from environment import environment
from color_add import color_add


class TestColorAdd(unittest.TestCase):

    def test_add_black_and_black(self):
        environment.set_colors('black', 'black')
        color_result = color_add.get_result()
        color_name_result = webcolors.hex_to_name(color_result)
        self.assertEqual('black', color_name_result)

    def test_add_red_and_black(self):
        environment.set_colors('red', 'black')
        color_result = color_add.get_result()
        color_name_result = webcolors.hex_to_name(color_result)
        self.assertEqual('red', color_name_result)

    def test_add_red_and_lime(self):
        environment.set_colors('red', 'lime')
        color_result = color_add.get_result()
        color_name_result = webcolors.hex_to_name(color_result)
        self.assertEqual('yellow', color_name_result)

    def test_add_white_and_lime(self):
        environment.set_colors('white', 'lime')
        color_result = color_add.get_result()
        color_name_result = webcolors.hex_to_name(color_result)
        self.assertEqual('white', color_name_result)
