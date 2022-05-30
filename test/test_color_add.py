from os import environ
import unittest

from color_add import color_add
from color_add.color_add import Color

from environment import environment


class TestColorAdd(unittest.TestCase):

    def test_add_black_and_black(self):
        environment.add('black', 'black')
        color = color_add.get_result()
        expected_color = Color(0, 0, 0)

        self.assertEqual(expected_color, color)
