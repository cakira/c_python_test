import unittest
import webcolors

from color_add import color_add

from environment import environment


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
